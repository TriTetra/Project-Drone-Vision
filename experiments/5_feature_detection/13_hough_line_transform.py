import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates and compares two methods for line detection
    using the Hough Transform in OpenCV:
    1. The Standard Hough Transform (cv2.HoughLines)
    2. The Probabilistic Hough Line Transform (cv2.HoughLinesP)
    """
    # --- 1. Setup and Pre-processing ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "h_line.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # The Hough Transform works on a binary image, so we must first find edges.
    # Canny edge detection is a common choice for this pre-processing step.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Create separate copies of the original image to draw the results on.
    img_standard_hough = image.copy()
    img_probabilistic_hough = image.copy()

    # --- 2. Method 1: Standard Hough Transform (cv2.HoughLines) ---
    # This method returns lines in a (rho, theta) format.
    # - rho: The distance from the top-left corner (0,0) to the line.
    # - theta: The angle of the line in radians.
    # We need to convert these polar coordinates to Cartesian to draw them.
    lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=180)
    
    if lines is not None:
        print(f"Found {len(lines)} lines with Standard Hough Transform.")
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            # Convert to Cartesian coordinates for drawing
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img_standard_hough, (x1, y1), (x2, y2), (0, 0, 255), 2) # Draw red lines

    # --- 3. Method 2: Probabilistic Hough Line Transform (cv2.HoughLinesP) ---
    # This is an optimized version that directly returns the endpoints (x1, y1, x2, y2)
    # of the detected line segments, which is often more convenient.
    # - minLineLength: Minimum length of line. Line segments shorter than this are rejected.
    # - maxLineGap: Maximum allowed gap between line segments to treat them as a single line.
    prob_lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    
    if prob_lines is not None:
        print(f"Found {len(prob_lines)} line segments with Probabilistic Hough Transform.")
        for line in prob_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img_probabilistic_hough, (x1, y1), (x2, y2), (0, 255, 0), 2) # Draw green lines

    # --- 4. Display All Results for Comparison ---
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edges (Input to Hough)", edges)
    cv2.imshow("1. Standard Hough Transform (Red)", img_standard_hough)
    cv2.imshow("2. Probabilistic Hough Transform (Green)", img_probabilistic_hough)

    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()