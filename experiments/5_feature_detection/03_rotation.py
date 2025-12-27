import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to rotate an image around a chosen center point
    using OpenCV's transformation functions.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Get the dimensions of the image (height, width)
    (rows, cols) = image.shape[:2]

    # --- 2. Calculate the Rotation Matrix ---
    # To rotate an image, we first define the transformation matrix using
    # cv2.getRotationMatrix2D(center, angle, scale).
    # - center: The point (x, y) around which the image is rotated.
    # - angle: The angle of rotation in degrees. Positive values mean counter-clockwise.
    # - scale: An optional scaling factor. 1.0 means the image is kept at the same size.
    
    center_point = (cols / 2, rows / 2)  # Rotate around the image's geometric center
    rotation_angle = 45                  # Rotate by 45 degrees
    scale_factor = 1.0                   # No scaling
    
    # This function computes the 2x3 matrix for the affine transformation.
    rotation_matrix = cv2.getRotationMatrix2D(center_point, rotation_angle, scale_factor)
    print("Calculated Rotation Matrix:\n", rotation_matrix)

    # --- 3. Apply the Rotation using warpAffine ---
    # We apply the calculated matrix to our image using the same cv2.warpAffine
    # function we used for translation.
    # The output size is specified as a (width, height) tuple.
    output_size = (cols, rows)
    rotated_image = cv2.warpAffine(image, rotation_matrix, output_size)

    # --- 4. Display the Results ---
    cv2.imshow("Original Image", image)
    cv2.imshow(f"Rotated by {rotation_angle} Degrees", rotated_image)

    print("Image was rotated using cv2.getRotationMatrix2D and cv2.warpAffine.")
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
