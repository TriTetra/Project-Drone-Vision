import cv2
import os

def main():
    """
    This script demonstrates selecting a Region of Interest (ROI) and
    copying it to another location within the same image using NumPy slicing.
    """
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "basketball.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Select an ROI (Region of Interest) using NumPy array slicing: [startY:endY, startX:endX]
    roi_face = image[350:500, 0:150]

    # Copy the ROI to a new location within the image.
    # The destination slice must have the same dimensions as the ROI.
    image[0:150, 400:550] = roi_face

    cv2.imshow("Original ROI", roi_face)
    cv2.imshow("Image with ROI Copied", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
