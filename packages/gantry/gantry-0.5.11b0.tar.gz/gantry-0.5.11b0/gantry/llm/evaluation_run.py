import copy
import datetime
import difflib
import json
from enum import Enum
from pathlib import Path

import evaluate
import openai
import pandas as pd

JOIN_KEY = "join_key"
INPUTS_PREFIX = "inputs."


class LLM_METRICS(str, Enum):
    EXACT_MATCH = "exact_match"


class EvaluationRun:
    def __init__(
        self,
        evaluation_dataset,
        run_identifier=None,
        label_column="label",
        metrics=[LLM_METRICS.EXACT_MATCH.value],
    ):
        self.evaluation_dataset = evaluation_dataset
        self.run_identifier = run_identifier
        self.label_column = label_column
        self.llm_eval_path = (
            Path(evaluation_dataset.workspace)
            / evaluation_dataset.dataset_name
            / "artifacts"
            / "eval"
        )
        if self.run_identifier:
            self.llm_eval_artifacts_path = self.llm_eval_path / self.run_identifier
        self._metrics = metrics

    def start(self, tag=None):
        self.__temp_open_ai_completion_create = openai.Completion.create
        self.run_tag = tag
        if not self.run_identifier:
            self.run_identifier = self._generate_run_identifier()
        self._init_paths()
        self._init_logging()
        self._trace_openai_calls()
        return self

    def finish(self):
        self._log_data_to_dataset()
        self._remove_openai_trace()

    @property
    def inputs(self):
        evaluation_stream = self.evaluation_dataset.get_huggingface_dataset(streaming=True)
        for eval in evaluation_stream:
            self.query_join_keys.append(eval[JOIN_KEY])
            inputs = copy.deepcopy(eval)
            inputs = {
                input: value for input, value in inputs.items() if input.startswith(INPUTS_PREFIX)
            }
            # Return only the inputs with the prefix "inputs." removed
            yield self._strip_inputs_prefix(inputs)

    @property
    def test_data(self):
        evaluation_stream = self.evaluation_dataset.get_huggingface_dataset(streaming=True)
        for eval in evaluation_stream:
            self.query_join_keys.append(eval[JOIN_KEY])
            inputs = copy.deepcopy(eval)
            inputs = {
                input: value for input, value in inputs.items() if input.startswith(INPUTS_PREFIX)
            }
            # Return input, label, join_key
            yield self._strip_inputs_prefix(inputs), eval[self.label_column], eval[JOIN_KEY]

    @property
    def metrics(self):
        labels = self.results[self.label_column].tolist()
        predictions = self.results[self.get_run_name_formatted_with_tags()].tolist()
        return evaluate.combine(self._metrics).compute(
            references=labels,
            predictions=predictions,
            ignore_case=True,
            ignore_punctuation=True,
        )

    @property
    def results(self) -> pd.DataFrame:
        return self.results_with_join_key.drop(columns=[JOIN_KEY])

    @property
    def results_with_join_key(self) -> pd.DataFrame:
        self.evaluation_dataset.label_column = self.label_column
        evaluation_results_df = self.evaluation_dataset.get_huggingface_dataset().to_pandas()
        eval_records = {}
        with (self.llm_eval_artifacts_path / "outputs.jsonl").open() as f:
            for line in f.readlines():
                data = json.loads(line)
                eval_records.update(data)
        evaluation_results_df[
            self.get_run_name_formatted_with_tags()
        ] = evaluation_results_df.apply(
            lambda x: x[JOIN_KEY] in eval_records and eval_records[x[JOIN_KEY]]["output"].strip(),
            axis=1,
        )
        return evaluation_results_df

    def compare_to_runs(self, tags=None, run_ids=None):
        runs = []
        if tags:
            runs += [EvaluationRun.from_tag(self.evaluation_dataset, tag) for tag in tags]
        if run_ids:
            runs += [EvaluationRun(self.evaluation_dataset, run_id) for run_id in run_ids]
        # If no tags or identifiers are provided, compare to all runs
        if not runs:
            runs = [
                EvaluationRun(self.evaluation_dataset, run.name)
                for run in self.llm_eval_path.iterdir()
                if run.is_dir() and run.name != self.run_identifier
            ]
        results = self.results_with_join_key
        for run in runs:
            results = results.merge(
                run.results_with_join_key[[run.get_run_name_formatted_with_tags(), JOIN_KEY]],
                on=JOIN_KEY,
                how="outer",
            )
        return results.drop(columns=[JOIN_KEY])

    def diff_outputs(self, run_id=None, tag=None):
        if run_id and tag:
            raise ValueError("Provide either run_id or run_tag, not both")
        if not run_id and not tag:
            raise ValueError("Provide either run_id or run_tag")
        run_ids = [run_id] if run_id else None
        tags = [tag] if tag else None
        results = self.compare_to_runs(tags=tags, run_ids=run_ids)
        if run_id:
            run = EvaluationRun(self.evaluation_dataset, run_id)
        if tag:
            run = EvaluationRun.from_tag(self.evaluation_dataset, tag)
        outputs = results[self.get_run_name_formatted_with_tags()].tolist()
        outputs_to_compare = results[run.get_run_name_formatted_with_tags()].tolist()
        input_cols = [col for col in results.columns if col.startswith(INPUTS_PREFIX)]
        input_dicts = results[input_cols].to_dict(orient="records")
        for input, output, output_to_compare in zip(input_dicts, outputs, outputs_to_compare):
            if output != output_to_compare:
                print("Inputs:")
                print(self._strip_inputs_prefix(input))
                print("-----------------")
                diff = difflib.context_diff(
                    [output + "\n"],
                    [output_to_compare + "\n"],
                    fromfile=self.get_run_name_formatted_with_tags(),
                    tofile=run.get_run_name_formatted_with_tags(),
                )
            diff_str = "".join(diff)
            print(diff_str)

    def add_tag(self, tag):
        tags = self._get_tags()
        tags[tag] = self.run_identifier
        with open(self._construct_tags_path(self.evaluation_dataset), "w") as f:
            json.dump(tags, f)

    @classmethod
    def from_tag(cls, dataset, tag):
        run = cls(dataset)
        tags = run._get_tags()
        run_identifier = tags.get(tag)
        if not run_identifier:
            raise KeyError(f"Run with tag {tag} not found")
        return EvaluationRun(dataset, run_identifier)

    def _strip_inputs_prefix(self, inputs):
        return {input[len(INPUTS_PREFIX) :]: value for input, value in inputs.items()}

    def _generate_run_identifier(self):
        curr_time_str_identifier = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"run_{curr_time_str_identifier}"

    @staticmethod
    def _construct_tags_path(dataset):
        return Path(dataset.workspace) / dataset.dataset_name / "artifacts" / "eval" / "tags.json"

    def get_run_name_formatted_with_tags(self):
        tags = self._get_all_tags_for_run()
        if tags:
            return f"{self.run_identifier}_output ({', '.join(tags)})"
        return self.run_identifier

    def _get_all_tags_for_run(self):
        tags = self._get_tags()
        return [tag for tag, run_id in tags.items() if run_id == self.run_identifier]

    def _init_paths(self):
        self.llm_eval_artifacts_path = self.llm_eval_path / self.run_identifier
        self.llm_eval_artifacts_path.mkdir(parents=True, exist_ok=True)
        self.tags_path = self._construct_tags_path(self.evaluation_dataset)
        self.tags_path.touch(exist_ok=True)

    def _init_logging(self):
        self.query_join_keys = []
        self.outputs = []
        self.metadata = {}

    @staticmethod
    def _extract_open_ai_completion_create_args(**kwargs):
        fields = ["model", "prompt", "max_tokens", "temperature"]
        return {field: kwargs.get(field, None) for field in fields}

    @staticmethod
    def _extract_open_ai_completion_response(resp):
        # Assume only one choice for now
        # TODO: Handle multiple choices
        return {
            "output": resp["choices"][0]["text"],
        }

    def _gantry_openai_completion_create(self, *args, **kwargs):
        gantry_data = self._extract_open_ai_completion_create_args(**kwargs)
        resp = self.__temp_open_ai_completion_create(*args, **kwargs)
        gantry_data.update(self._extract_open_ai_completion_response(resp))
        self._update_run_data(gantry_data)

        return resp

    def _update_outputs(self, gantry_data):
        self.outputs.append(gantry_data["output"])

    def _update_metadatas(self, gantry_data):
        # Only need to set it once
        if self.metadata:
            return
        metadata_dict = copy.deepcopy(gantry_data)
        metadata_dict.pop("output")
        metadata_dict.pop("prompt")
        self.metadata = metadata_dict

    def _update_run_data(self, gantry_data):
        self._update_outputs(gantry_data)
        self._update_metadatas(gantry_data)

    def _update_tags(self):
        tags = self._get_tags()
        # Always set current run to latest
        tags["latest"] = self.run_identifier
        if self.run_tag:
            tags[self.run_tag] = self.run_identifier

        with open(self.tags_path, "w") as f:
            json.dump(tags, f)

    def _get_tags(self):
        tags = {}
        tags_text = self._construct_tags_path(self.evaluation_dataset).read_text()
        if tags_text:
            tags = json.loads(tags_text)
        return tags

    def _log_data_to_dataset(self):
        # Then store the query outputs as jsonl file
        output_file_path = Path(self.llm_eval_artifacts_path) / "outputs.jsonl"
        # match outputs with query ids
        outputs = []
        for i, join_key in enumerate(self.query_join_keys):
            outputs.append(
                {
                    join_key: {
                        "output": self.outputs[i],
                    }
                }
            )
        with open(output_file_path, "w") as f:
            for output in outputs:
                json.dump(output, f)
                f.write("\n")
        # Then store the metadata as json file
        metadata_file_path = Path(self.llm_eval_artifacts_path) / "metadata.json"
        with open(metadata_file_path, "w") as f:
            json.dump(self.metadata, f)

        self._update_tags()
        if self.evaluation_dataset._api_client:
            self.evaluation_dataset.push_version(
                message=f"Add evaluation run {self.run_identifier}",
            )

    def _trace_openai_calls(self):
        openai.Completion.create = self._gantry_openai_completion_create

    def _remove_openai_trace(self):
        if hasattr(self, "__temp_open_ai_completion_create"):
            openai.Completion.create = self.__temp_open_ai_completion_create

    def __repr__(self):
        return self.results.to_markdown()

    def __del__(self):
        # rebind openAI completion create to original function
        self._remove_openai_trace()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.finish()

    def log_output(self, output, join_key):
        output_file_path = Path(self.llm_eval_artifacts_path) / "outputs.jsonl"
        with open(output_file_path, "a+") as f:
            json.dump({join_key: {"output": output}}, f)
            f.write("\n")

    def log_metadata(self):
        metadata_file_path = Path(self.llm_eval_artifacts_path) / "metadata.json"
        if not metadata_file_path.exists():
            with open(metadata_file_path, "w") as f:
                json.dump(self.metadata, f)
