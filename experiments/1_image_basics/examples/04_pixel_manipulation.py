import cv2
import os

def main():
    """
    This script demonstrates accessing and modifying individual pixel values
    and manipulating a Region of Interest (ROI) in an image.
    """
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "OpenCV.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Access and modify a single pixel (BGR order)
    image[50, 50] = (0, 0, 255) # Set pixel at (50, 50) to Red
    
    # Manipulate a Region of Interest (ROI)
    # Note: Modifying the ROI directly modifies the original image.
    roi = image[100:200, 200:400]
    roi[:, :] = (0, 255, 0) # Set ROI to Green

    cv2.imshow("Pixel and ROI Operations", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
