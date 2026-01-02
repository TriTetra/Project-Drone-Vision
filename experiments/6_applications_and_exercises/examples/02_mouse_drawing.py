import cv2
import numpy as np
import os

# List to store clicked points (circles)
clicked_points = []

def mouse_callback(event, x, y, flags, param):
    """Callback function to handle mouse events and store clicked points."""
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))

def main():
    """This script demonstrates how to capture mouse click events to draw on a video frame."""
    assets_path = os.path.join("..", "..", "_assets")
    video_path = os.path.join(assets_path, "car.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    window_name = "Drawing on Video"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("--- Mouse Drawing on Video ---")
    print("Click the left mouse button to draw circles.")
    print("Press 'h' to clear all drawn circles.")
    print("Press 'Esc' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.resize(frame, (640, 480))
        
        # Draw all clicked points as circles on the frame
        for center in clicked_points:
            cv2.circle(frame, center, 20, (255, 0, 0), -1) # Blue circles
        
        cv2.imshow(window_name, frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27: # Esc key
            break
        elif key == ord("h"): # 'h' key
            clicked_points.clear()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
