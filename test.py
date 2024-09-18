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


# Copy files from source to destination
for file_path in source_folder.iterdir():
    # If it's a file (not a folder), copy it
    temp = 0
    if file_path.is_file():
        
        for back_up_file_path in backup_folder_path.iterdir():
            if back_up_file_path.name == file_path.name and time.ctime(file_path.stat().st_mtime) < time.ctime(back_up_file_path.stat().st_mtime):
                print("not modified", file_path.name)
                temp = 1
                break
        if temp == 0:
            shutil.copy(file_path, backup_folder_path)
            print("copied", file_path.name)