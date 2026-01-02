import cv2
import os
import numpy as np

def main():
    """This script demonstrates corner detection using the Shi-Tomasi method."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)
    
    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Detect Corners with goodFeaturesToTrack
    corners = cv2.goodFeaturesToTrack(image=gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
    
    if corners is not None:
        corners = np.int0(corners)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1) # Draw a red circle

    cv2.imshow("Shi-Tomasi Corner Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
