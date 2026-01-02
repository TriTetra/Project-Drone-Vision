import cv2
import os
import numpy as np

def main():
    """This script demonstrates applying an Affine Transformation to an image
    to perform a translation (shifting its position)."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    rows, cols, _ = image.shape
    
    # Define the Transformation Matrix for Translation
    tx = 100  # Shift right by 100 pixels
    ty = 50   # Shift down by 50 pixels
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    # Apply the Affine Transformation (cv2.warpAffine expects (width, height) for output size)
    translated_image = cv2.warpAffine(image, M, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow(f"Translated by (x={tx}, y={ty})", translated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
