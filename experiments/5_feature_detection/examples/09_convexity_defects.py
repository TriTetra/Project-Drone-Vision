import cv2
import os
import numpy as np

def main():
    """This script demonstrates finding and visualizing Convexity Defects.
    These are deviations of a contour from its convex hull."""
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

        hull_indices = cv2.convexHull(main_contour, returnPoints=False)
        defects = cv2.convexityDefects(main_contour, hull_indices)

        if defects is not None:
            for i in range(defects.shape[0]):
                s_idx, e_idx, f_idx, depth = defects[i, 0]
                
                start_point = tuple(main_contour[s_idx][0])
                end_point = tuple(main_contour[e_idx][0])
                farthest_point = tuple(main_contour[f_idx][0])
                
                cv2.line(image, start_point, end_point, (0, 255, 0), 2) # Green line
                cv2.circle(image, farthest_point, 5, (0, 0, 255), -1)   # Red circle
            else:
                print("No defects found.")

        cv2.imshow("Convexity Defects", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No contours found.")

if __name__ == "__main__":
    main()
