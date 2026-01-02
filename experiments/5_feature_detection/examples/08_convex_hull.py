import cv2
import os
import numpy as np

def main():
    """This script demonstrates finding the Convex Hull of a shape.
    The Convex Hull is the smallest convex polygon enclosing a contour."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "star.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return
            
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        main_contour = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(main_contour)
        
        cv2.drawContours(image, [main_contour], -1, (0, 255, 0), 3) # Original contour in green
        cv2.drawContours(image, [hull], -1, (0, 0, 255), 3)         # Convex hull in red

        cv2.imshow("Convex Hull Demonstration", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No contours found in the image.")

if __name__ == "__main__":
    main()
