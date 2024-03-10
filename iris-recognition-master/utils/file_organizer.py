import os
import shutil
from glob import glob
from typing import List, Set

INPUT_DIR = "data/IrisImage"  # Updated input directory
TARGET_DIR = "data/original_renamed"  # Updated target directory

def _extract_user_ids(input_dir: str) -> Set[int]:
    """
    Extract user IDs from the directory names directly under the input directory.
    """
    user_dirs = glob(os.path.join(input_dir, "*"))
    return set(int(os.path.basename(user_path)) for user_path in user_dirs)

def create_empty_dir(target_dir: str) -> None:
    """
    Creates an empty directory. If the directory already exists, it deletes
    the existing directory and creates a new one.
    """
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)

def organize_files(input_dir: str = INPUT_DIR,
                   target_dir: str = TARGET_DIR,
                   user_ids: List[int] = None) -> None:
    """
    Organizes files by copying them from the input directory to the target directory
    with a new naming convention that includes the user ID and the original file name.
    """
    if user_ids is None:
        user_ids = list(_extract_user_ids(input_dir))

    create_empty_dir(target_dir)

    for user_id in user_ids:
        user_path = os.path.join(input_dir, str(user_id))
        pics = glob(os.path.join(user_path, "*.JPG"))
        for pic in pics:
            base_name = os.path.basename(pic)
            new_name = f"{user_id}_{base_name}"
            shutil.copyfile(pic, os.path.join(target_dir, new_name))

if __name__ == '__main__':
    organize_files()
