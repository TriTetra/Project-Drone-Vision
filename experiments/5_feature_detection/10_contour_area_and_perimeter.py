import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to calculate basic geometric properties of contours,
    specifically the area using cv2.contourArea() and the perimeter (arc length)
    using cv2.arcLength().
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
    print(f"Found {len(contours)} contours to analyze.")

    # --- 3. Analyze and Visualize Each Contour ---
    # Loop over each contour found in the image.
    for i, c in enumerate(contours):
        # Calculate the area of the contour using cv2.contourArea().
        area = cv2.contourArea(c)

        # The moment 'm00' also gives the area. This can be used for verification.
        M = cv2.moments(c)
        
        # To avoid division by zero, only process contours with a non-zero area.
        if M["m00"] > 0:
            # Calculate the perimeter (or arc length) of the contour.
            # The second argument (True) specifies that the shape is a closed contour.
            perimeter = cv2.arcLength(c, closed=True)

            # Find the centroid to place the text label
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # --- 4. Visualize the Results on the Image ---
            # Draw the contour itself in green
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # Create a text label with the calculated properties
            text = f"Area: {int(area)}, Peri: {int(perimeter)}"
            # Put the text label on the image near the centroid of the contour
            cv2.putText(image, text, (cX - 60, cY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            print(f"--- Contour {i+1} ---")
            print(f"  - Area: {area:.2f}")
            print(f"  - Perimeter: {perimeter:.2f}")

    # --- 5. Display the final image with all annotations ---
    cv2.imshow("Contour Properties (Area and Perimeter)", image)
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()