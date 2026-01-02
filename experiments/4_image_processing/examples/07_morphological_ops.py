import cv2
import os
import numpy as np

def main():
    """This script demonstrates fundamental morphological transformations:
    Erosion, Dilation, Opening, and Closing."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "text.png")
    
    gray_image = cv2.imread(img_path, 0)
    if gray_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(binary_image, kernel, iterations=1)
    dilation = cv2.dilate(binary_image, kernel, iterations=1)
    opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Original Binary Image", binary_image)
    cv2.imshow("1. Erosion (Thins)", erosion)
    cv2.imshow("2. Dilation (Thickens)", dilation)
    cv2.imshow("3. Opening (Removes salt noise)", opening)
    cv2.imshow("4. Closing (Closes pepper holes)", closing)

    print("Displaying results of morphological operations. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
