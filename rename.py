import os
import shutil

def rename_images(root_folder):
    # Navigate through each sub-folder in the root directory
    for subdir, dirs, files in os.walk(root_folder):
        for dir_name in dirs:
            if dir_name in ['L', 'R']:  # Check if the directory is 'L' or 'R'
                full_dir_path = os.path.join(subdir, dir_name)
                image_files = sorted(os.listdir(full_dir_path))  # Sort to maintain order
                
                # Start the naming sequence from 1
                count = 1
                for file in image_files:
                    # Construct old and new file paths
                    old_file_path = os.path.join(full_dir_path, file)
                    new_file_name = f"{dir_name}{count}.JPG"
                    new_file_path = os.path.join(subdir, new_file_name)
                    
                    # Rename the file
                    shutil.move(old_file_path, new_file_path)
                    print(f"Renamed {old_file_path} to {new_file_path}")
                    count += 1

                # Remove the now-empty 'L' or 'R' directories
                os.rmdir(full_dir_path)

# Example usage
root_folder = 'data/IrisImage'
rename_images(root_folder)
