import cv2
import os
import numpy as np

def main():
    """This script demonstrates and compares four common image smoothing
    (blurring) techniques: Averaging, Gaussian, Median, and Bilateral."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "filter.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    avg_blur = cv2.blur(image, (5, 5))
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
    median_blur = cv2.medianBlur(image, 5) # Good for salt-and-pepper noise
    bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75) # Preserves edges

    cv2.imshow("Original Image", image)
    cv2.imshow("1. Averaging Blur", avg_blur)
    cv2.imshow("2. Gaussian Blur", gaussian_blur)
    cv2.imshow("3. Median Blur", median_blur)
    cv2.imshow("4. Bilateral Filter", bilateral_blur)

    print("Displaying results of various blur filters. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
