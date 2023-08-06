import copy
import os
from datetime import datetime
from pathlib import Path
from typing import List, Union

import git
import pandas as pd
import pyarrow as pa
import pyarrow.types
import yaml
from git.exc import InvalidGitRepositoryError

from gantry.dataset.constants import (
    ARTIFACTS,
    DATASET_CONFIG_FILE,
    DATASET_README_FILE,
    DEFAULT_DS_CONF,
    TABULAR_MANIFESTS,
    UserDtype,
)


def _arrow_to_datasets_dtype(arrow_type: pa.DataType) -> str:
    """
    _arrow_to_datasets_dtype takes a pyarrow.DataType and converts it to a Gantry Dataset dtype.
    """
    if pyarrow.types.is_null(arrow_type):
        return UserDtype.UNKNOWN.value
    elif pyarrow.types.is_boolean(arrow_type):
        return UserDtype.BOOLEAN.value
    elif (
        pyarrow.types.is_int8(arrow_type)
        or pyarrow.types.is_int16(arrow_type)
        or pyarrow.types.is_int32(arrow_type)
        or pyarrow.types.is_int64(arrow_type)
        or pyarrow.types.is_uint8(arrow_type)
        or pyarrow.types.is_uint16(arrow_type)
        or pyarrow.types.is_uint32(arrow_type)
        or pyarrow.types.is_uint64(arrow_type)
    ):
        return UserDtype.INTEGER.value
    elif (
        pyarrow.types.is_float16(arrow_type)
        or pyarrow.types.is_float32(arrow_type)
        or pyarrow.types.is_float64(arrow_type)
    ):
        return UserDtype.FLOAT.value
    elif pyarrow.types.is_string(arrow_type):
        return UserDtype.TEXT.value
    elif pyarrow.types.is_large_string(arrow_type):
        return UserDtype.TEXT.value
    elif pyarrow.types.is_timestamp(arrow_type):
        # treat it as text to bypass wrong type inference
        return UserDtype.TEXT.value
    else:
        raise ValueError(
            f"PyArrow type {arrow_type} does not have a Gantry datasets dtype equivalent."
        )


def get_inferred_type(seq: Union[List, pd.Series]) -> str:
    inferred_type = _arrow_to_datasets_dtype(pa.array(seq).type)
    return inferred_type


def get_creation_time(p: Path) -> str:
    return datetime.fromtimestamp(p.stat().st_ctime).strftime("%Y-%m-%d %H:%M:%S")


def create_local_dataset(working_dir: str, dataset_name: str):
    """
    create_local_dataset creates a local dataset directory with config and readme files.
    Local dataset will be use for LLM user testing and it will not support versioning.

    Args:
        working_dir (Path): dataset working directory
        dataset_name (str): dataset name
    """
    local_dataset_path = Path(working_dir) / dataset_name
    os.makedirs(local_dataset_path / ARTIFACTS, exist_ok=True)
    os.makedirs(local_dataset_path / TABULAR_MANIFESTS, exist_ok=True)

    dataset_config = copy.deepcopy(DEFAULT_DS_CONF)
    dataset_config["dataset_name"] = dataset_name
    yaml.safe_dump(
        dataset_config,
        (local_dataset_path / DATASET_CONFIG_FILE).open(mode="w"),
    )

    (local_dataset_path / DATASET_README_FILE).touch(exist_ok=True)


def is_git_repo(path: str):
    try:
        _ = git.Repo(path).git_dir
        return True
    except InvalidGitRepositoryError:
        return False
