import os
from box.exceptions import BoxValueError
from src.textSummerizer.logging import logger
import yaml 
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox

from pathlib import Path

from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path):
    try:
        with open(path_to_yaml, "r") as file:
            content = yaml.safe_load(file)

        if not content or not isinstance(content, dict):  # Validate the YAML content
            raise ValueError(f"The YAML file at {path_to_yaml} is empty or not a valid dictionary.")

        logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
        return ConfigBox(content)

    except BoxValueError as e:
        raise ValueError(f"Error converting YAML content to ConfigBox: {e}")
    except Exception as e:
        raise ValueError(f"Failed to read YAML file at {path_to_yaml}: {e}")
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    
    
