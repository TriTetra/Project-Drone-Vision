import cv2
import numpy as np

def nothing(x):
    """Dummy callback function for trackbars."""
    pass

def main():
    """This script provides an interactive HSV color calibration tool using webcam feed.
    Adjust the trackbars to find the HSV color range for a specific object."""
    cap = cv2.VideoCapture(0) # Open default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    window_name = "HSV Color Tuner"
    cv2.namedWindow(window_name)

    # Create trackbars for Lower and Upper HSV bounds
    cv2.createTrackbar("Lower H", window_name, 0, 180, nothing)
    cv2.createTrackbar("Lower S", window_name, 0, 255, nothing)
    cv2.createTrackbar("Lower V", window_name, 0, 255, nothing)
    cv2.createTrackbar("Upper H", window_name, 180, 180, nothing)
    cv2.createTrackbar("Upper S", window_name, 255, 255, nothing)
    cv2.createTrackbar("Upper V", window_name, 255, 255, nothing)

    print("--- HSV Color Calibration Tool ---")
    print("Adjust trackbars to isolate a desired color range. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1) # Flip for mirror effect
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get current trackbar positions
        lower_h = cv2.getTrackbarPos("Lower H", window_name)
        lower_s = cv2.getTrackbarPos("Lower S", window_name)
        lower_v = cv2.getTrackbarPos("Lower V", window_name)
        upper_h = cv2.getTrackbarPos("Upper H", window_name)
        upper_s = cv2.getTrackbarPos("Upper S", window_name)
        upper_v = cv2.getTrackbarPos("Upper V", window_name)

        lower_color = np.array([lower_h, lower_s, lower_v])
        upper_color = np.array([upper_h, upper_s, upper_v])

        mask = cv2.inRange(hsv_frame, lower_color, upper_color)
        result_frame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Original Feed", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", result_frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
