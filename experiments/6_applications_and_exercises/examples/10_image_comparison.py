import cv2
import os
import numpy as np

def main():
    """This script demonstrates how to compare two images for differences."""
    assets_path = os.path.join("..", "..", "_assets")
    path1 = os.path.join(assets_path, "aircraft.jpg")
    path2 = os.path.join(assets_path, "aircraft_compare.jpg")

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    if img1 is None or img2 is None:
        print("Error: Could not load one or both aircraft images.")
        return

    # Ensure both images are the same size for comparison
    target_size = (320, 480)
    img1_resized = cv2.resize(img1, target_size)
    img2_resized = cv2.resize(img2, target_size)

    # Convert to grayscale for simpler difference calculation
    gray1 = cv2.cvtColor(img1_resized, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the two grayscale images
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference to highlight significant changes
    # Pixels with a difference greater than 30 are set to 255 (white).
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Count non-zero pixels in the difference mask
    non_zero_pixels = cv2.countNonZero(thresh)

    print(f"Number of differing pixels: {non_zero_pixels}")

    if non_zero_pixels == 0:
        print("Images are completely identical.")
    else:
        print("Images are not identical (differences highlighted).")
    
    cv2.imshow("Aircraft 1", img1_resized)
    cv2.imshow("Aircraft 2", img2_resized)
    cv2.imshow("Differences Highlighted", thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
