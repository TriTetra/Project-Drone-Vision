import cv2
import os
import numpy as np

# --- 1. Setup Paths and Load Image ---
assets_path = os.path.join("..", "_assets")
img_path = os.path.join(assets_path, "OpenCV.jpg")
image = cv2.imread(img_path)

if image is not None:
    print(f"Image loaded with shape: {image.shape}")

    # --- 2. Accessing a Single Pixel ---
    # You can get the color value of a pixel by accessing its row and column.
    # Note: OpenCV uses BGR (Blue, Green, Red) order.
    (b, g, r) = image[50, 50]
    print(f"Pixel at (50, 50) - Red: {r}, Green: {g}, Blue: {b}")

    # --- 3. Modifying a Single Pixel ---
    # You can change a pixel's value by assigning a new BGR tuple.
    # Let's set the pixel at (60, 60) to red.
    image[60, 60] = (0, 0, 255)
    print("Set the pixel at (60, 60) to pure Red.")

    # --- 4. Region of Interest (ROI) Manipulation ---
    # Using NumPy slicing, we can select a rectangular region of the image.
    # This creates a 'view' into the original image's data, not a copy.
    roi = image[100:200, 200:400]

    # When we modify the ROI, we are actually modifying the original image.
    # Let's set the entire ROI to green.
    roi[:, :] = (0, 255, 0)
    print("Set a rectangular ROI to pure Green.")
    
    # --- 5. Display the Final Result ---
    # The final image will show our modifications: the single red pixel 
    # and the large green rectangle (ROI).
    cv2.imshow("Pixel and ROI Operations", image)

    print("\nPress any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not load image from {img_path}")