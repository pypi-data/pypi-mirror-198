import pytest

from gantry.llm import EvaluationRun


def dataset_pytest_iter(dataset, tag, metrics):
    """
    A pytest fixture that iterates over the test data of a dataset.
    It will return a tuple of (input, label, join_key, run) for each test data point.

    Args:
        dataset (_type_): testing dataset
        tag (_type_): test run tag
        metrics (_type_): eval metrics
    """
    run = EvaluationRun(dataset, metrics=metrics)
    run.start(tag=tag)
    run._update_tags()

    def decorator(test_func):
        @pytest.mark.parametrize("input, label, join_key", run.test_data)
        @pytest.mark.parametrize("run", [run])
        def wrapper(input, label, join_key, run, *args, **kwargs):
            return test_func(input, label, join_key, run, *args, **kwargs)

        return wrapper

    return decorator
