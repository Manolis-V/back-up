# Backup Script

## Overview
This script is designed to create a backup of the directory it resides in. The backup is placed in a specified directory. It efficiently copies all files and folders, ensuring that only newly created or modified files are updated in the backup directory. This helps in minimizing redundant data transfer and storage.

## Features
- Full Directory Backup: Copies all files and subdirectories from the source directory.
- Incremental Backup: Only copies newly created or modified files, ensuring efficient use of storage space and time.
- Preserves Directory Structure: Maintains the exact directory structure in the backup location.
- Configurable Backup Location: The backup directory path is specified within the script.

## Prerequisites
- Python 3.x
- Necessary permissions to read from the source directory and write to the backup directory.

# Usage
1. Clone or Download the Script:

```bash
git clone https://github.com/yourusername/backup-script.git
cd backup-script
```
2. Configure the Backup Directory: Open the script in a text editor and specify the path to your desired backup directory by modifying the `backup_directory` variable.

```python
backup_directory = '/path/to/your/backup/directory'
```
3. Run the Script: Execute the script from the command line.

```bash
python backup_script.py
```
# Example
Given the following source directory structure:

```
/source-directory
|-- file1.txt
|-- file2.txt
\-- subdirectory
    |-- file3.txt
```
After running the script, the backup directory will have the same structure:

```
/backup-directory
|-- file1.txt
|-- file2.txt
\-- subdirectory
    |-- file3.txt
```
If `file1.txt` is modified or a new file `file4.txt` is added to the source directory, running the script again will update `file1.txt` and add `file4.txt` to the backup directory without copying the unmodified files.

Notes
Ensure that the script has appropriate read/write permissions for the source and backup directories.
Running the script periodically will keep the backup directory up-to-date with minimal data transfer.
