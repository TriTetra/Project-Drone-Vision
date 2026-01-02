import cv2
import os
import numpy as np

def main():
    """This script demonstrates how to detect circles in an image
    using the Hough Circle Transform (cv2.HoughCircles)."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "coins.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray, 5) # Reduce noise

    # Detect Circles using HoughCircles
    circles = cv2.HoughCircles(
        image=gray_blurred,
        method=cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=200,
        param2=30, # Lower to detect more, less-perfect circles
        minRadius=40,
        maxRadius=80
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center_x, center_y, radius = i[0], i[1], i[2]
            cv2.circle(image, (center_x, center_y), radius, (0, 255, 0), 2) # Outer green circle
            cv2.circle(image, (center_x, center_y), 2, (0, 0, 255), 3)       # Center red dot
    else:
        print("No circles were found with the current parameters.")

    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
