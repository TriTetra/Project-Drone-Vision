import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to find and visualize Convexity Defects.
    A convexity defect is a deviation of a shape's contour from its convex hull.
    It's useful for analyzing the concave parts of a shape, e.g., the area 
    between fingers in a hand gesture recognition application.
    """
    # --- 1. Setup and Pre-processing ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "star.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # --- 2. Find the Main Contour ---
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # To avoid noise, find the largest contour by area and assume it's our target shape.
    main_contour = max(contours, key=cv2.contourArea)

    # --- 3. Find Convex Hull Indices and then the Defects ---
    # To find convexity defects, we first need the *indices* of the points that 
    # form the hull, not the points themselves. So, we pass `returnPoints=False`.
    hull_indices = cv2.convexHull(main_contour, returnPoints=False)
    
    # Now we can find the defects using the contour and the hull indices.
    defects = cv2.convexityDefects(main_contour, hull_indices)

    # --- 4. Visualize the Defects ---
    if defects is not None:
        print(f"Found {len(defects)} convexity defects.")
        # Each row in the 'defects' array contains:
        # [start_point_index, end_point_index, farthest_point_index, depth]
        for i in range(defects.shape[0]):
            s_idx, e_idx, f_idx, depth = defects[i, 0]
            
            # Get the (x, y) coordinates of these points from the original contour
            start_point = tuple(main_contour[s_idx][0])
            end_point = tuple(main_contour[e_idx][0])
            farthest_point = tuple(main_contour[f_idx][0])
            
            # Draw a green line connecting the start and end points of the hull segment
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)
            # Draw a red circle at the farthest point of the defect (the "bottom" of the concavity)
            cv2.circle(image, farthest_point, 5, (0, 0, 255), -1)
    else:
        print("No defects found for the main contour.")

    # --- 5. Display the final image ---
    cv2.imshow("Convexity Defects", image)
    print("\nThe green lines show the convex hull segments.")
    print("The red dots show the deepest points of the concavities (the defects).")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()