import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to find the Convex Hull of a shape using 
    cv2.convexHull(). The Convex Hull can be visualized as a rubber band 
    stretched around the contour of a shape. It is the smallest convex polygon 
    that encloses all points of the shape.
    """
    # --- 1. Setup and Pre-processing ---
    assets_path = os.path.join("..", "_assets")
    # We use 'star.png' because it is a non-convex shape, which clearly
    # shows the difference between the contour and its convex hull.
    img_path = os.path.join(assets_path, "star.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return
            
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # --- 2. Find Contours ---
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # --- 3. Find the Convex Hull of the Largest Contour ---
    if len(contours) > 0:
        # To avoid noise, we find the largest contour by area and assume it's our target shape.
        main_contour = max(contours, key=cv2.contourArea)

        # cv2.convexHull() finds the convex hull of a set of points (our contour).
        hull = cv2.convexHull(main_contour)
        
        # --- 4. Visualize the Result ---
        # To clearly see the difference, we will draw both the original contour
        # and the convex hull on the same image with different colors.

        # Draw the original contour in green
        cv2.drawContours(image, [main_contour], -1, (0, 255, 0), 3)
        # Draw the convex hull in red
        cv2.drawContours(image, [hull], -1, (0, 0, 255), 3)

        cv2.imshow("Convex Hull Demonstration", image)
        print("Original contour is drawn in Green.")
        print("The Convex Hull is drawn in Red, like a 'rubber band' around the shape.")
        print("\nPress any key to quit.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No contours were found in the image.")

if __name__ == "__main__":
    main()
