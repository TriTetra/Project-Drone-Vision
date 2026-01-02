import cv2
import os
import numpy as np

def main():
    """This script demonstrates and compares Standard and Probabilistic Hough Line Transforms."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "h_line.png")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    img_standard_hough = image.copy()
    img_probabilistic_hough = image.copy()

    # Method 1: Standard Hough Transform (returns rho, theta)
    lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=180)
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img_standard_hough, (x1, y1), (x2, y2), (0, 0, 255), 2) # Draw red lines

    # Method 2: Probabilistic Hough Line Transform (returns endpoints x1, y1, x2, y2)
    prob_lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    if prob_lines is not None:
        for line in prob_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img_probabilistic_hough, (x1, y1), (x2, y2), (0, 255, 0), 2) # Draw green lines

    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("1. Standard Hough (Red)", img_standard_hough)
    cv2.imshow("2. Probabilistic Hough (Green)", img_probabilistic_hough)

    print("Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
