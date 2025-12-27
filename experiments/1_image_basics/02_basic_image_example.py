import cv2
import os
import numpy as np

# --- 1. Define Paths ---
# Construct a relative path to the central assets directory.
# This makes the script portable and not dependent on a specific user's folder structure.
assets_path = os.path.join("..", "_assets")
cat_path = os.path.join(assets_path, "cat.jpg")
dog_path = os.path.join(assets_path, "dog.jpg")

# --- 2. Read Images ---
# cv2.imread() loads an image from the specified file path.
img_cat = cv2.imread(cat_path)
img_dog = cv2.imread(dog_path)

# --- 3. Examine Image Properties ---
# It's good practice to check if the image was loaded successfully before using it.
# The .shape attribute returns a tuple of (height, width, channels).
# The .dtype attribute shows the data type of the image's pixels.
print("--- Original Image Properties ---")
if img_cat is not None:
    print(f"Cat Image - Data Type: {img_cat.dtype}, Shape: {img_cat.shape}")
else:
    print(f"Error: Failed to load image at {cat_path}")

if img_dog is not None:
    print(f"Dog Image - Data Type: {img_dog.dtype}, Shape: {img_dog.shape}")
else:
    print(f"Error: Failed to load image at {dog_path}")

# --- 4. Resize Images ---
# cv2.resize() changes an image's dimensions to a new (width, height).
print("\n--- Resized Image Properties ---")
if img_cat is not None:
    resized_cat = cv2.resize(img_cat, (300, 300))
    print(f"Resized Cat - New Shape: {resized_cat.shape}")
    # cv2.imshow() displays an image in a new window.
    # The first argument is the window name, the second is the image to display.
    cv2.imshow("Resized Cat", resized_cat)

if img_dog is not None:
    resized_dog = cv2.resize(img_dog, (400, 400))
    print(f"Resized Dog - New Shape: {resized_dog.shape}")
    cv2.imshow("Resized Dog", resized_dog)

# --- 5. Wait for User Input to Close ---
# cv2.waitKey(0) waits indefinitely for any key to be pressed. 
# This is necessary to keep the image windows open until we are ready to close them.
if img_cat is not None or img_dog is not None:
    print("\nPress any key to close all image windows.")
    cv2.waitKey(0)
    # cv2.destroyAllWindows() closes all windows created by OpenCV.
    cv2.destroyAllWindows()