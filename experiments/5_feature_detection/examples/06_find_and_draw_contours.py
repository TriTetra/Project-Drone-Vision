import cv2
import os
import numpy as np

def main():
    """This script demonstrates finding contours in an image and drawing them."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print(f"Found {len(contours)} contours.")

    cv2.drawContours(image, contours, -1, (0, 255, 0), 3) # Draw all contours in green

    cv2.imshow("Contours Found and Drawn", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
