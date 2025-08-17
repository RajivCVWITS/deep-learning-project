import os
from box.exceptions import BoxValueError
import yaml
from src.deep_learning_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_dirs: list, verbose: bool = True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_dirs (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its content as a ConfigBox object.
    
    Args:
        path (Path): Path to the JSON file.
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file and returns its content.
    
    Args:
        path (Path): Path to the binary file.
    """
    with open(path, "rb") as bin_file:
        content = joblib.load(bin_file)
        logger.info(f"Binary file loaded successfully from: {path}")
        return content

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB.
    
    Args:
        path (Path): Path to the file.
        
    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage (imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        imgdata = f.read()
        return base64.b64encode(imgdata)
