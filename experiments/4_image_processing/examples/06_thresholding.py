import cv2
import os
import numpy as np

def main():
    """This script demonstrates and compares simple (global) and adaptive thresholding."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    
    gray_image = cv2.imread(img_path, 0)
    if gray_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Simple (Global) Thresholding
    _, simple_thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # Adaptive Thresholding (useful for varying lighting)
    adaptive_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    cv2.imshow("Original Grayscale Image", gray_image)
    cv2.imshow("1. Simple Global Thresholding", simple_thresh)
    cv2.imshow("2. Adaptive Mean Thresholding", adaptive_thresh)

    print("Displaying results of simple vs. adaptive thresholding. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
