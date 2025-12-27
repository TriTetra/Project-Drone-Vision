import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates and compares two types of image thresholding:
    1. Simple (Global) Thresholding
    2. Adaptive Thresholding
    Thresholding is the simplest method of image segmentation, used to create a 
    binary (black and white) image from a grayscale one.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    
    # Load the image in grayscale directly by passing the flag '0'.
    gray_image = cv2.imread(img_path, 0)

    if gray_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Apply Simple (Global) Thresholding ---
    # cv2.threshold(src, thresh_value, max_value, type)
    # This method uses a single threshold value for the entire image. Any pixel with an 
    # intensity value greater than 'thresh_value' is set to 'max_value'.
    # It works well for images with uniform lighting.
    # The function returns the threshold value used and the thresholded image.
    ret, simple_thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # --- 3. Apply Adaptive Thresholding ---
    # cv2.adaptiveThreshold(src, max_value, adaptiveMethod, thresholdType, blockSize, C)
    # This method is useful for images with varying lighting conditions. The threshold for
    # a pixel is calculated based on the pixels in its local neighborhood ('blockSize').
    # - ADAPTIVE_THRESH_MEAN_C: Threshold is the mean of the neighborhood area minus the constant 'C'.
    # - blockSize: The size of the neighborhood area (e.g., 11x11). Must be an odd number.
    # - C: A constant subtracted from the calculated mean or weighted sum.
    adaptive_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # --- 4. Display the Results for Comparison ---
    cv2.imshow("Original Grayscale Image", gray_image)
    cv2.imshow("1. Simple Global Thresholding (thresh=150)", simple_thresh)
    cv2.imshow("2. Adaptive Mean Thresholding", adaptive_thresh)

    print("Displaying results of simple vs. adaptive thresholding.")
    print("Notice how adaptive thresholding can handle shadows and lighting changes better.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
