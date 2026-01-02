import cv2
import os
import numpy as np

def main():
    """This script demonstrates a simple, manual method for background subtraction
    (Static Frame Differencing) to detect motion."""
    assets_path = os.path.join("..", "..", "_assets")
    video_path = os.path.join(assets_path, "car.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    ret, first_frame = cap.read()
    if not ret:
        print("Error: Could not read the first frame.")
        cap.release()
        return
        
    target_size = (640, 480)
    first_frame = cv2.resize(first_frame, target_size)
    background_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    background_gray = cv2.GaussianBlur(background_gray, (21, 21), 0)

    print("Detecting motion by differencing from the first frame. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_frame = cv2.resize(frame, target_size)
        current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        current_gray = cv2.GaussianBlur(current_gray, (21, 21), 0)

        frame_diff = cv2.absdiff(background_gray, current_gray)
        _, motion_mask = cv2.threshold(frame_diff, 50, 255, cv2.THRESH_BINARY)
        motion_mask = cv2.dilate(motion_mask, None, iterations=2) # Fill in holes

        cv2.imshow("Original Video", current_frame)
        cv2.imshow("Motion Mask", motion_mask)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
