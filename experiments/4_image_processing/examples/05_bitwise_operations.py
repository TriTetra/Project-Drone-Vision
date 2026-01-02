import cv2
import os
import numpy as np

def main():
    """This script demonstrates the four fundamental bitwise operations:
    AND, OR, XOR, and NOT. Essential for image masking."""
    assets_path = os.path.join("..", "..", "_assets")
    img1_path = os.path.join(assets_path, "bitwise_1.png")
    img2_path = os.path.join(assets_path, "bitwise_2.png")

    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    if image1 is None or image2 is None:
        print("Error: Could not load one or both images.")
        return

    result_and = cv2.bitwise_and(image1, image2) # Intersection
    result_or = cv2.bitwise_or(image1, image2)   # Union
    result_xor = cv2.bitwise_xor(image1, image2) # Exclusive OR
    result_not_1 = cv2.bitwise_not(image1)       # Invert Image 1

    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)
    cv2.imshow("1. AND (Intersection)", result_and)
    cv2.imshow("2. OR (Union)", result_or)
    cv2.imshow("3. XOR (Exclusive OR)", result_xor)
    cv2.imshow("4. NOT on Image 1", result_not_1)

    print("Displaying results of bitwise operations. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
