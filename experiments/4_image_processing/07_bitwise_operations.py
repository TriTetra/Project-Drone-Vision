import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates the four fundamental bitwise operations in OpenCV:
    AND, OR, XOR, and NOT. These are essential for image masking and selecting
    regions of interest.
    """
    # --- 1. Setup Paths and Load Images ---
    # These images are simple black shapes on a white background, designed 
    # to clearly show the results of the logical operations.
    assets_path = os.path.join("..", "_assets")
    img1_path = os.path.join(assets_path, "bitwise_1.png")
    img2_path = os.path.join(assets_path, "bitwise_2.png")

    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    if image1 is None or image2 is None:
        print("Error: Could not load one or both of the bitwise images.")
        return

    # --- 2. Perform Bitwise Operations ---
    # We can think of white pixels as 1 (True) and black pixels as 0 (False).

    # Bitwise AND: The output pixel is white (1) only if the corresponding 
    # pixels in BOTH input images are white. This gives the intersection.
    result_and = cv2.bitwise_and(image1, image2)

    # Bitwise OR: The output pixel is white (1) if the corresponding pixel
    # in EITHER of the input images is white. This gives the union.
    result_or = cv2.bitwise_or(image1, image2)

    # Bitwise XOR: The output pixel is white (1) if the corresponding pixel 
    # is white in ONE of the images, but NOT BOTH.
    result_xor = cv2.bitwise_xor(image1, image2)

    # Bitwise NOT: Inverts the pixel colors of a single image. White becomes
    # black, and black becomes white.
    result_not_1 = cv2.bitwise_not(image1)
    result_not_2 = cv2.bitwise_not(image2)

    # --- 3. Display All Results ---
    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)
    cv2.imshow("1. AND (Intersection)", result_and)
    cv2.imshow("2. OR (Union)", result_or)
    cv2.imshow("3. XOR (Exclusive OR)", result_xor)
    cv2.imshow("4. NOT on Image 1", result_not_1)

    print("Displaying results of bitwise AND, OR, XOR, and NOT.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()