import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates fundamental morphological transformations in OpenCV:
    Erosion, Dilation, Opening, and Closing. These operations modify the
    shape and structure of objects in a binary image.
    """
    # --- 1. Setup Path and Create a Binary Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "text.png")
    
    # Load the image in grayscale
    gray_image = cv2.imread(img_path, 0)

    if gray_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Morphological operations work best on binary (black and white) images.
    # We'll apply a threshold to convert our grayscale image to a binary image.
    # THRESH_BINARY_INV makes the text white (foreground) and the background black.
    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

    # --- 2. Define the Kernel ---
    # The 'kernel' is a structuring element, a small matrix that defines the
    # neighborhood to be considered for each pixel during the operation.
    kernel = np.ones((3, 3), np.uint8)

    # --- 3. Apply Morphological Operations ---

    # 1. Erosion: Erodes away the boundaries of the foreground (white) object.
    # It's useful for removing small white noise.
    erosion = cv2.erode(binary_image, kernel, iterations=1)

    # 2. Dilation: Expands the area of the foreground object.
    # It can be used to join broken parts of an object or close small holes.
    dilation = cv2.dilate(binary_image, kernel, iterations=1)

    # 3. Opening: An erosion followed by a dilation.
    # This is very useful for removing small white noise spots ('salt' noise).
    opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    # 4. Closing: A dilation followed by an erosion.
    # This is useful for closing small black holes ('pepper' noise) in the foreground object.
    closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # --- 4. Display the Results for Comparison ---
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