# File Organizer CLI

A Python command-line interface tool that organizes files in a specified directory by file type or creation date. This tool allows users to manage their files efficiently, providing options for recursive organization, file moving, and an interactive confirmation mode.

## Features

- **Organize by File Type**: Automatically sorts files into folders based on their type (e.g., `.txt`, `.pdf`, `.jpg`).
- **Organize by Creation Date**: Groups files into folders named by their creation date (YYYY-MM-DD).
- **Recursive Organization**: Traverses through subdirectories to organize files at all levels.
- **Move or Copy Files**: Option to move files instead of copying them.
- **Undo Last Operation**: Allows the user to revert the last organization operation.
- **Interactive Mode**: Prompts users for confirmation before executing file organization.
- **Logging**: Keeps track of file operations in a log file for user review.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of command-line operations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RaksithSivakumar/file_organizer.git```

2. Change to the project directory:

  ``` bash 
    cd file_organizer 
```

3. (Optional) Create a virtual environment and activate it:
``` bash 
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Usage

### Organize Files by Type

To organize files in a specified directory by their type:
``` bash 
python file_organizer.py /path/to/directory --type
```

### Organize Files by Creation Date

To organize files by their creation date:

``` bash 
python file_organizer.py /path/to/directory --date
```
Move Files Instead of Copying
To move files instead of copying them:

bash
Copy code
python file_organizer.py /path/to/directory --type --move
Recursive Organization
To organize files recursively within subdirectories:

```bash
python file_organizer.py /path/to/directory --type --recursive
```
### Undo Last Operation
To undo the last organization operation:

```bash
python file_organizer.py /path/to/directory --undo
```
### Interactive Mode
To use interactive mode for confirmation before organization:

```bash
python file_organizer.py /path/to/directory --type --interactive
```
## Logging

All file operations are logged in the file_organizer.log file. This log file contains timestamps and details of organized files for user review.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## Acknowledgments
This project utilizes Python's built-in libraries such as ```os```, ```shutil```, ```argparse```, and ```logging.```

### **Additional Notes**:
- You can replace the repository link in the installation section with the actual link to your GitHub repository.
- Feel free to adjust any sections to better reflect your style or additional project details.
- Ensure to create a `LICENSE` file if you're including a license.

This README will help users understand your project and how to use it effectively. Let me know if you need any modifications or additional sections!
