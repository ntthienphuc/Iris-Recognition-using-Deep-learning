import os
import re
from glob import glob
from shutil import copyfile
from typing import List, Tuple

FILENAME_REGEX = r'^(\d+)_(L\d+|R\d+)\.JPG$'


def get_file_name(file_path: str) -> str:
    return os.path.basename(file_path)


def extract_user_sample_ids(image_path):
    image_filename = os.path.basename(image_path)
    match = re.match(FILENAME_REGEX, image_filename, re.IGNORECASE)
    if match:
        return match.groups()
    else:
        raise ValueError(f"Filename does not match expected pattern: {image_filename}")

def create_empty_dir(target_dir: str):
    """
    Create an empty directory, removing all files first if the target directory
    already exists.
    """
    if os.path.exists(target_dir):
        files = glob(target_dir + "/*")
        for file in files:
            os.remove(file)
    else:
        os.makedirs(target_dir)


def copy_dataset(file_paths: List[str], target_dir: str):
    for file_path in file_paths:
        file_name = get_file_name(file_path)
        copyfile(file_path, f"{target_dir}/{file_name}")
