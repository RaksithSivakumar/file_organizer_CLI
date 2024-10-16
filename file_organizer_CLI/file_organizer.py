import os
import shutil
import argparse
from datetime import datetime
import logging
import json

# Set up logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

undo_file = 'undo_data.json'

# Organize by file type
def organize_by_type(directory, move=False, recursive=False):
    undo_data = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_ext = filename.split('.')[-1].upper()
            folder = os.path.join(directory, file_ext + '_Files')
            os.makedirs(folder, exist_ok=True)
            dest_path = os.path.join(folder, filename)
            if move:
                shutil.move(file_path, dest_path)
            else:
                shutil.copy(file_path, dest_path)
            undo_data[file_path] = dest_path
            logging.info(f"Organized {filename} to {folder}")
        if not recursive:
            break
    save_undo_data(undo_data)

# Organize by date
def organize_by_date(directory, move=False, recursive=False):
    undo_data = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            created_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
            folder = os.path.join(directory, created_date)
            os.makedirs(folder, exist_ok=True)
            dest_path = os.path.join(folder, filename)
            if move:
                shutil.move(file_path, dest_path)
            else:
                shutil.copy(file_path, dest_path)
            undo_data[file_path] = dest_path
            logging.info(f"Organized {filename} to {folder}")
        if not recursive:
            break
    save_undo_data(undo_data)

# Save undo data
def save_undo_data(undo_data):
    with open(undo_file, 'w') as f:
        json.dump(undo_data, f)

# Undo the last organization
def undo_last_operation():
    if os.path.exists(undo_file):
        with open(undo_file, 'r') as f:
            undo_data = json.load(f)
        for dest, original in undo_data.items():
            if os.path.exists(dest):
                shutil.move(dest, original)
                logging.info(f"Undo: Moved {dest} back to {original}")
        os.remove(undo_file)
        print("Undo operation completed.")
    else:
        print("No undo data found.")
        logging.info("Undo operation attempted but no data found.")

# Interactive prompt for confirmation
def interactive_confirmation():
    choice = input("Do you want to proceed with organizing the files? (yes/no): ")
    return choice.lower() == 'yes'

# CLI setup with argparse
def main():
    parser = argparse.ArgumentParser(description="Organize files by type or date.")
    parser.add_argument('directory', help="Directory to organize")
    parser.add_argument('--type', action='store_true', help="Organize by file type")
    parser.add_argument('--date', action='store_true', help="Organize by file creation date")
    parser.add_argument('--move', action='store_true', help="Move files instead of copying")
    parser.add_argument('--recursive', action='store_true', help="Organize files recursively")
    parser.add_argument('--undo', action='store_true', help="Undo the last organization")
    parser.add_argument('--interactive', action='store_true', help="Interactive mode to confirm operations")

    args = parser.parse_args()

    # Undo operation
    if args.undo:
        undo_last_operation()
        return

    # Interactive confirmation
    if args.interactive and not interactive_confirmation():
        print("Operation canceled by user.")
        return

    # Organize by type or date
    if args.type:
        organize_by_type(args.directory, move=args.move, recursive=args.recursive)
    elif args.date:
        organize_by_date(args.directory, move=args.move, recursive=args.recursive)
    else:
        print("Please specify --type or --date")
        logging.info("No valid organization method specified.")

if __name__ == "__main__":
    main()
