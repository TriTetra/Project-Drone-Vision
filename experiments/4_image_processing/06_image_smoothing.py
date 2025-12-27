import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates and compares four common image smoothing (blurring)
    techniques available in OpenCV, which are used to reduce image noise.
    """
    # --- 1. Setup Path and Load a Noisy Image ---
    assets_path = os.path.join("..", "_assets")
    # We use 'filter.png' as it's a good example image with salt-and-pepper noise.
    img_path = os.path.join(assets_path, "filter.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Apply Different Smoothing Filters ---

    # 1. Averaging Filter (cv2.blur)
    # This is the simplest filter. It takes the average of all pixels under a 
    # kernel area and replaces the central element. (5, 5) is the kernel size.
    avg_blur = cv2.blur(image, (5, 5))

    # 2. Gaussian Filter (cv2.GaussianBlur)
    # Similar to averaging, but uses a weighted Gaussian kernel. Pixels closer 
    # to the center of the kernel have more 'weight', resulting in a more natural blur.
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

    # 3. Median Filter (cv2.medianBlur)
    # Computes the median of all the pixels under the kernel window and the central 
    # pixel is replaced with this median value. Highly effective against 'salt-and-pepper' noise.
    median_blur = cv2.medianBlur(image, 5)

    # 4. Bilateral Filter (cv2.bilateralFilter)
    # An advanced filter that is highly effective at noise removal while preserving edges.
    # It considers both the spatial distance and the intensity difference between pixels.
    bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

    # --- 3. Display the Results for Comparison ---
    cv2.imshow("Original Image", image)
    cv2.imshow("1. Averaging Blur", avg_blur)
    cv2.imshow("2. Gaussian Blur", gaussian_blur)
    cv2.imshow("3. Median Blur (Effective for Noise)", median_blur)
    cv2.imshow("4. Bilateral Filter (Edge Preserving)", bilateral_blur)

    print("Displaying the original image and the results of various blur filters.")
    print("Notice how Median Blur removes the black dots, and Bilateral Blur keeps text sharp.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()