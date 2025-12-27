import cv2
import os

# --- 1. Setup Path and Load Image ---
assets_path = os.path.join("..", "_assets")
img_path = os.path.join(assets_path, "basketball.jpg")
image = cv2.imread(img_path)

# --- 2. Check if Image was Loaded ---
if image is not None:
    print(f"Original image shape: {image.shape}")

    # --- 3. Select a Region of Interest (ROI) ---
    # We use NumPy array slicing to select a rectangular area.
    # The format is [startY:endY, startX:endX].
    # These coordinates were chosen to select the face in the basketball.jpg image.
    roi_face = image[350:500, 0:150]

    # --- 4. Copy the ROI to a New Location ---
    # We can assign the pixel data from the ROI to another slice of the same size.
    # This effectively copies the ROI's content to a new part of the image.
    # The destination slice MUST have the same dimensions as the ROI.
    # The ROI shape is (150, 150, 3), so we select a 150x150 area at the top right.
    image[0:150, 400:550] = roi_face
    print("Copied the ROI to the top-right corner of the image.")

    # --- 5. Display the Results ---
    # We can view the original ROI and the final image with the ROI copied.
    cv2.imshow("Original ROI (The Face)", roi_face)
    cv2.imshow("Image with ROI Copied", image)

    print("\nPress any key to close all windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not load image from {img_path}")