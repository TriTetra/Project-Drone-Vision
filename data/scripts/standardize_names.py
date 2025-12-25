import os 
import argparse
from tqdm import tqdm

def standardize_names(target_dir, prefix, start_index=0):
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"The directory {target_dir} does not exist.")
    
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    images = []

    files = os.listdir(target_dir)
    for f in files:
        if f.lower().endswith(valid_extensions):
            images.append(f)

    images.sort()

    print(f"Found {len(images)} image files in {target_dir}. Starting renaming process with prefix '{prefix}'...")

    confirm = input(f"Are you sure you want to proceed? This will rename all image files in the directory. (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled by user.")
        return
    
    count = 0
    for i, filename in enumerate(tqdm(images, desc="Renaming images")):
        old_img_path = os.path.join(target_dir, filename)
        file_name_no_ext, ext = os.path.splitext(filename)
        old_txt_path = os.path.join(target_dir, f"{file_name_no_ext}.txt")

        new_name_base = f"{prefix}_{str(i+start_index).zfill(4)}"
        new_img_name = new_name_base + ext
        new_txt_name = new_name_base + ".txt"

        new_img_path = os.path.join(target_dir, new_img_name)
        new_txt_path = os.path.join(target_dir, new_txt_name)

        if os.path.exists(new_img_path):
            if new_img_name != old_img_path:
                continue
            else:
                print(f"Skipping renaming for {old_img_path} as it would overwrite itself.")
                continue

        os.rename(old_img_path, new_img_path)
        if os.path.exists(old_txt_path):
            os.rename(old_txt_path, new_txt_path)

        count += 1

    print(f"Renaming completed. {count} files were renamed." )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standardize image and label file names in the specified directory.")
    parser.add_argument("--dir", type=str, help="Path to the directory containing image files.")
    parser.add_argument("--prefix", type=str, help="Prefix for the new file names.")
    parser.add_argument("--start_index", type=int, default=0, help="Starting index for numbering the files.")
    
    args = parser.parse_args()
    standardize_names(args.dir, args.prefix, args.start_index)