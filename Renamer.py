import os
import uuid

def rename_files_in_directory():
    directory = input("Enter the directory: ")

    # First pass: rename all files to a random name
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.avi', '.mkv', '.flv', '.mov')):
                random_name = f"{uuid.uuid4()}{os.path.splitext(filename)[1]}"
                source = os.path.join(dirpath, filename)
                destination = os.path.join(dirpath, random_name)
                os.rename(source, destination)

    # Second pass: rename all files to the ordered name
    for dirpath, dirnames, filenames in os.walk(directory):
        for i, filename in enumerate(filenames):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.avi', '.mkv', '.flv', '.mov')):
                subfolder_name = os.path.basename(dirpath)  # Get the subfolder name
                new_name = f"{subfolder_name}_{i}{os.path.splitext(filename)[1]}"
                source = os.path.join(dirpath, filename)
                destination = os.path.join(dirpath, new_name)
                os.rename(source, destination)

rename_files_in_directory()