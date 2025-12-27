import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to visualize contours by drawing them on an image
    using the cv2.drawContours() function. It builds on the previous script where
    contours were found.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "contour1.png")
    image_to_draw_on = cv2.imread(img_path)

    if image_to_draw_on is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Find Contours (Prerequisite Step) ---
    # To draw contours, we first need to find them. This process is the same
    # as the previous script: convert to grayscale, then threshold to get a binary image.
    gray = cv2.cvtColor(image_to_draw_on, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print(f"Found {len(contours)} contours to draw.")

    # --- 3. Draw the Contours on the Original Image ---
    # cv2.drawContours(destination_image, contours_list, contour_index, color, thickness)
    # - destination_image: The image on which to draw the contours.
    # - contours_list: The Python list of contours from findContours.
    # - contour_index: The index of the contour to draw from the list. 
    #                  A special value of -1 means "draw all contours".
    # - color: The color to use for the contours, in BGR format.
    # - thickness: The thickness of the contour lines.
    
    # We will draw all found contours in blue with a thickness of 3 pixels.
    cv2.drawContours(image_to_draw_on, contours, -1, (255, 0, 0), 3)

    # --- 4. Display the Final Result ---
    cv2.imshow("Image with Contours Drawn", image_to_draw_on)
    print("All found contours have been drawn in blue on the original image.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()