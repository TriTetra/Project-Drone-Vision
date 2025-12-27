import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates corner detection using the Shi-Tomasi method,
    which is implemented in OpenCV as cv2.goodFeaturesToTrack().
    Corners are strong, stable features in an image, useful for tracking, 
    image matching, and object recognition.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "contour.png")
    image = cv2.imread(img_path)
    
    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Pre-process the Image for the Detector ---
    # The Shi-Tomasi corner detector works on single-channel grayscale images.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # The function also requires the input image to be of type float32.
    gray = np.float32(gray)

    # --- 3. Detect Corners with goodFeaturesToTrack ---
    # cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
    # - image: Input 8-bit or floating-point 32-bit, single-channel image.
    # - maxCorners: The maximum number of corners to return. If more are found, the strongest are returned.
    # - qualityLevel: A value between 0-1. It represents the minimum quality of a corner.
    #   A corner with a quality measure less than (qualityLevel * best_corner_quality) is rejected.
    # - minDistance: The minimum possible Euclidean distance between the corners detected.
    corners = cv2.goodFeaturesToTrack(image=gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
    
    if corners is not None:
        # The output 'corners' is a numpy array of [[x, y]] coordinates.
        # We convert it to integers to use for drawing.
        corners = np.int0(corners)
        print(f"Detected {len(corners)} strong corners.")

        # --- 4. Visualize the Detected Corners ---
        # We loop over each detected corner and draw a small circle on the original color image.
        for corner in corners:
            # The corner array has a shape like [[[x, y]]], so we use .ravel() to flatten it to [x, y].
            x, y = corner.ravel()
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)  # Draw a small, solid red circle
    else:
        print("No corners were detected with the current parameters.")

    # --- 5. Display the Result ---
    cv2.imshow("Shi-Tomasi Corner Detection", image)
    print("\nPress any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
