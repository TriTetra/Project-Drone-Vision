import cv2
import os
import numpy as np

def main():
    """This script demonstrates how to rotate an image around a chosen center point."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    (rows, cols) = image.shape[:2]

    # Calculate the Rotation Matrix (center, angle, scale)
    center_point = (cols / 2, rows / 2)
    rotation_angle = 45
    scale_factor = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center_point, rotation_angle, scale_factor)

    # Apply the Rotation using warpAffine
    output_size = (cols, rows)
    rotated_image = cv2.warpAffine(image, rotation_matrix, output_size)

    cv2.imshow("Original Image", image)
    cv2.imshow(f"Rotated by {rotation_angle} Degrees", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()