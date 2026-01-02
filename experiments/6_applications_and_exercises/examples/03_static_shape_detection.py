import cv2
import os
import numpy as np

def detect_and_label_shapes(image):
    """Finds contours, approximates their shape, and labels them."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv2.contourArea(cnt) < 100:
            continue

        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        cv2.drawContours(image, [approx], 0, (0, 0, 0), 3)
        
        x, y, w, h = cv2.boundingRect(approx)

        shape_name = ""
        num_vertices = len(approx)
        
        if num_vertices == 3:
            shape_name = "Triangle"
        elif num_vertices == 4:
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                shape_name = "Square"
            else:
                shape_name = "Rectangle"
        elif num_vertices == 5:
            shape_name = "Pentagon"
        else:
            shape_name = "Circle"
            
        cv2.putText(image, shape_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            
    return image

if __name__ == "__main__":
    assets_path = os.path.join("..", "..", "_assets")
    img1_path = os.path.join(assets_path, "polygons.png")
    img2_path = os.path.join(assets_path, "polygons2.jpg")

    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)
    
    if image1 is not None and image2 is not None:
        result1 = detect_and_label_shapes(image1)
        result2 = detect_and_label_shapes(image2)
        
        cv2.imshow("Shape Detection on Image 1", result1)
        cv2.imshow("Shape Detection on Image 2", result2)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error loading one or both images.")
