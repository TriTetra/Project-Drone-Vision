import cv2
import os
import numpy as np

def main():
    """This script demonstrates how to calculate and display various properties of contours:
    area, perimeter, moments, and centroid."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for i, c in enumerate(contours):
        if cv2.contourArea(c) > 100: # Filter small contours
            M = cv2.moments(c)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0 # Handle zero area contours
            
            area = cv2.contourArea(c)
            perimeter = cv2.arcLength(c, True)

            cv2.drawContours(image, [c], -1, (0, 255, 0), 2) # Green contour
            cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1) # Red centroid
            
            text = f"A:{int(area)} P:{int(perimeter)}"
            cv2.putText(image, text, (cX - 50, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow("Contour Properties", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
