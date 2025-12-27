import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to apply an Affine Transformation to an image
    to perform a translation (i.e., shifting the image's position).
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Get the dimensions of the image (height, width)
    rows, cols, _ = image.shape

    # --- 2. Define the Transformation Matrix for Translation ---
    # For an affine transformation, we use a 2x3 matrix, M.
    # To perform a simple translation, the matrix is defined as:
    # M = [[1, 0, tx],
    #      [0, 1, ty]]
    # where 'tx' is the shift in the x-direction (horizontal) and
    # 'ty' is the shift in the y-direction (vertical).
    
    tx = 100  # Shift right by 100 pixels
    ty = 50   # Shift down by 50 pixels
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    # --- 3. Apply the Affine Transformation ---
    # cv2.warpAffine(source_image, transformation_matrix, output_image_size)
    # - src: The source image.
    # - M: The 2x3 transformation matrix.
    # - dsize: The size of the output image, as a (width, height) tuple.
    # Note: The original code incorrectly used (rows, cols). The correct format is (cols, rows).
    output_size = (cols, rows)
    translated_image = cv2.warpAffine(image, M, output_size)

    # --- 4. Display the Results ---
    cv2.imshow("Original Image", image)
    cv2.imshow(f"Translated by (x={tx}, y={ty})", translated_image)

    print("Image was translated using a custom Affine Transformation matrix.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()