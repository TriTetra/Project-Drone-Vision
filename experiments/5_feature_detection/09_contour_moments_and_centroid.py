import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to calculate the 'moments' of a contour
    to find its geometric properties, such as its center of mass, also known
    as the 'centroid'.
    """
    # --- 1. Setup and Pre-processing ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # --- 2. Find Contours ---
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Found {len(contours)} contours.")

    # --- 3. Calculate Moments and Find Centroid for Each Contour ---
    # We will loop through each contour that was found.
    for c in contours:
        # cv2.moments() computes the spatial moments of the contour points.
        # It returns a dictionary of moment values.
        M = cv2.moments(c)
        
        # The moment 'm00' is the area of the contour. To avoid division by
        # zero, we must check if the area is non-zero.
        if M["m00"] != 0:
            # The centroid coordinates (cX, cY) can be calculated from the moments:
            # cX = M10 / M00
            # cY = M01 / M00
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # --- 4. Visualize the Results ---
            # Draw the contour itself in green
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # Draw a small red circle at the calculated centroid
            cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
            # Put a label "Center" near the centroid
            cv2.putText(image, "Center", (cX - 25, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            print("Skipping a contour with zero area.")

    # --- 5. Display the Final Image ---
    cv2.imshow("Centroids of Contours", image)
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()