import os
import argparse
from tqdm import tqdm


def clean_labels(target_dir):

    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"The directory {target_dir} does not exist.")
    
    txt_files = []
    for file in os.listdir(target_dir):
        if file.lower().endswith('.txt'):
            txt_files.append(file)

    count = len(txt_files)
    if count == 0:
        raise ValueError(f"No .txt files found in the directory {target_dir}.")
    
    print(f"Found {count} .txt files in {target_dir}. Starting cleaning process...")

    confirm = input("Are you sure you want to proceed? This will delete all contents of the .txt files. (y/n): ")

    if confirm.lower() != 'y':
        print("Operation cancelled by user.")
        return
    
    for file in tqdm(txt_files, desc="Cleaning labels"):
        file_path = os.path.join(target_dir, file)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean label .txt files in the specified directory.")
    parser.add_argument("--dir", type=str, help="Path to the directory containing .txt label files.")
    
    args = parser.parse_args()
    clean_labels(args.dir)