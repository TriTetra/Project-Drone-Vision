import cv2
import os

# --- 1. Setup Path and Load Image ---
assets_path = os.path.join("..", "_assets")
img_path = os.path.join(assets_path, "forest.jpg")
image = cv2.imread(img_path)

# --- 2. Check if Image was Loaded ---
if image is not None:
    # --- 3. Get Image Properties ---

    # .shape returns a tuple: (height, width, number_of_channels)
    # For a BGR image, number_of_channels is 3.
    # For a grayscale image, the tuple is just (height, width).
    shape = image.shape
    height = image.shape[0]
    width = image.shape[1]
    
    # Check if the image is color or grayscale to determine channel count
    if len(image.shape) == 3:
        channels = image.shape[2]
    else:
        channels = 1
    
    # .size returns the total number of pixels (height * width * channels).
    total_pixels = image.size
    
    # .dtype returns the data type of the image's pixels (e.g., 'uint8' for 0-255).
    data_type = image.dtype

    # --- 4. Print Properties to the Console ---
    print("--- Image Properties ---")
    print(f"Filename: {os.path.basename(img_path)}")
    print(f"Dimensions (H x W): {height} x {width}")
    print(f"Number of Channels: {channels}")
    print(f"Total Number of Pixels: {total_pixels:,}") # Format with a comma for readability
    print(f"Data Type of Pixels: {data_type}")

    # --- 5. Display the Image ---
    cv2.imshow("Image", image)
    print("\nPress any key to close the image window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not load image from {img_path}")