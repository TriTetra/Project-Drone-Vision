import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates how to detect circles in an image using the
    Hough Circle Transform, implemented as cv2.HoughCircles().
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "coins.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Pre-processing ---
    # The Hough Circle Transform works on grayscale images.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Applying a median blur is crucial. It reduces noise in the image, which 
    # can lead to the detection of false circles. A 5x5 kernel is often a good start.
    gray_blurred = cv2.medianBlur(gray, 5)

    # --- 3. Detect Circles using HoughCircles ---
    # cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
    # - image:     Input 8-bit, single-channel grayscale image.
    # - method:    Detection method. Currently, only cv2.HOUGH_GRADIENT is available.
    # - dp:        Inverse ratio of the accumulator resolution to the image resolution.
    #              dp=1 means the accumulator has the same resolution as the input image.
    # - minDist:   Minimum distance between the centers of detected circles.
    # - param1:    The higher threshold for the internal Canny edge detector.
    # - param2:    The accumulator threshold for circle centers at the detection stage.
    #              A smaller value means more (and potentially false) circles will be detected.
    # - minRadius: Minimum circle radius to detect.
    # - maxRadius: Maximum circle radius to detect.
    #
    # Finding the right parameters often requires experimentation.
    circles = cv2.HoughCircles(
        image=gray_blurred,
        method=cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=200,
        param2=30,  # Lower this value to detect more, less-perfect circles
        minRadius=40,
        maxRadius=80
    )

    # --- 4. Visualize the Detected Circles ---
    if circles is not None:
        # Convert the (x, y, r) coordinates and radius to integers.
        circles = np.uint16(np.around(circles))
        print(f"Found {len(circles[0, :])} circles.")
        
        # Loop over the detected circles
        for i in circles[0, :]:
            center_x, center_y, radius = i[0], i[1], i[2]
            # Draw the outer circle boundary in green
            cv2.circle(image, (center_x, center_y), radius, (0, 255, 0), 2)
            # Draw the center of the circle in red
            cv2.circle(image, (center_x, center_y), 2, (0, 0, 255), 3)
    else:
        print("No circles were found with the current parameters.")

    # --- 5. Display the Result ---
    cv2.imshow("Detected Circles", image)
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()