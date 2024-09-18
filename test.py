import shutil
from pathlib import Path
import time

# Specify the source and destination folders
source_folder = Path('C:/Users/manol/Documents/git/back-up')
destination_folder = Path('C:/Users/manol/Documents/back-ups')

# Create a timestamped backup folder
backup_folder_name = f"backup_{Path(source_folder).name}"
backup_folder_path = destination_folder / backup_folder_name
# Check if the destination folder exists; if not, create it
backup_folder_path.mkdir(parents=True, exist_ok=True)


def copy_files(file_path, backup_folder_path):

    for back_up_file_path in backup_folder_path.iterdir():

        if back_up_file_path.name == file_path.name and time.ctime(file_path.stat().st_mtime) < time.ctime(back_up_file_path.stat().st_mtime):
            print("\033[33mnot modified", file_path.name, "\033[0m")
            return

    shutil.copy(file_path, backup_folder_path)
    print("\033[32mcopied", file_path.name, "\033[0m")
# \033[31m red

def handle_folders(temp_source_folder, backup_folder_path):
    
    for file_path in temp_source_folder.iterdir():

        if file_path.is_file():
            copy_files(file_path, backup_folder_path)

        if file_path.is_dir() and file_path.name != '.git':
            backup_folder_path_folder = backup_folder_path / file_path.name
            backup_folder_path_folder.mkdir(parents=True, exist_ok=True)
            handle_folders(file_path, backup_folder_path_folder)


# Copy files from source to destination
for file_path in source_folder.iterdir():
    
    # handling files
    if file_path.is_file():
        copy_files(file_path, backup_folder_path)

    # handling folders
    if file_path.is_dir() and file_path.name != '.git':
        backup_folder_path_folder = backup_folder_path / file_path.name
        backup_folder_path_folder.mkdir(parents=True, exist_ok=True)
        handle_folders(file_path, backup_folder_path_folder)