import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates a common and powerful technique: isolating an object
    in a video based on its color. It uses the HSV color space, which is often
    more robust for color detection than the default BGR space.
    """
    # --- 1. Setup Video Capture ---
    assets_path = os.path.join("..", "_assets")
    video_path = os.path.join(assets_path, "dog.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    print("Isolating white objects in the video. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error reading frame.")
            break

        # --- Pipeline Step 1: Convert to HSV Color Space ---
        # We convert from BGR to HSV (Hue, Saturation, Value) because it's easier
        # to define a color range in HSV. Hue represents the color itself, which
        # is more stable under changing lighting conditions than BGR values.
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # --- Pipeline Step 2: Define Color Range and Create Mask ---
        # Here, we define the range for the color white in HSV.
        # White has a low saturation and high value, while hue can be anything.
        sensitivity = 15
        lower_white = np.array([0, 0, 255 - sensitivity])
        upper_white = np.array([255, sensitivity, 255])
        
        # cv2.inRange() creates a binary mask. Pixels in the hsv_frame that fall
        # within the [lower_white, upper_white] range are set to 255 (white),
        # and all other pixels are set to 0 (black).
        mask = cv2.inRange(hsv_frame, lower_white, upper_white)

        # --- Pipeline Step 3: Apply the Mask ---
        # cv2.bitwise_and() performs a bitwise AND between the original frame and
        # itself, but only in the regions where the 'mask' is white (255).
        # This effectively "cuts out" the object of the desired color.
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # --- 4. Display Results ---
        cv2.imshow("1. Original Frame", frame)
        cv2.imshow("2. Binary Mask", mask)
        cv2.imshow("3. Isolated Object", result)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # --- 5. Cleanup ---
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()