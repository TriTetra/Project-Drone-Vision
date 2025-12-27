import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates the first and most fundamental step of contour
    analysis: finding contours in a binary image using cv2.findContours().
    A contour is a curve joining all the continuous points along the boundary
    of an object, having the same color or intensity.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Pre-process the Image ---
    # The findContours function works on a binary (black and white) image.
    # Therefore, we must perform two pre-processing steps:
    # First, convert the image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Second, apply a threshold to create a binary image. Pixels above 127
    # will become 255 (white), and those below will become 0 (black).
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # --- 3. Find Contours ---
    # cv2.findContours(image, mode, method)
    # - image: The source binary image. The function may modify this image, so
    #          it's good practice to pass a copy if you need the original.
    # - mode: Contour retrieval mode. cv2.RETR_TREE retrieves all contours
    #         and reconstructs a full hierarchy of nested contours (e.g., shapes within shapes).
    # - method: Contour approximation method. cv2.CHAIN_APPROX_SIMPLE compresses
    #           horizontal, vertical, and diagonal segments, leaving only their end points.
    #           This saves memory.
    #
    # The function returns a list of the detected contours and their hierarchy.
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # The 'contours' variable is a Python list of all the contours in the image.
    # Each individual contour is a NumPy array of (x, y) coordinates of the boundary points.
    print(f"Successfully found {len(contours)} contours in the image.")
    
    if len(contours) > 0:
        # We can inspect the first contour to see it's a list of points.
        print(f"The first contour consists of {len(contours[0])} points.")

    # --- 4. Display the Intermediate Images ---
    # Note: We are NOT drawing the contours in this script, only finding them.
    # The next script will demonstrate how to visualize the found contours.
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image (Input for findContours)", binary_image)

    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()