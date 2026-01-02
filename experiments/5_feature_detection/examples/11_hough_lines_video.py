import cv2
import os
import numpy as np

def main():
    """This script demonstrates detecting lines of a specific color (yellow) in a video."""
    assets_path = os.path.join("..", "..", "_assets")
    video_path = os.path.join(assets_path, "line.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    print("Detecting yellow lines in the video. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define range for yellow color in HSV
        lower_yellow = np.array([18, 94, 140], dtype=np.uint8)
        upper_yellow = np.array([48, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        edges = cv2.Canny(mask, 75, 150)
        
        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=40, maxLineGap=5)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        cv2.imshow("Original Frame with Detected Lines", frame)
        # cv2.imshow("Yellow Color Mask", mask) # Uncomment to see the mask
        # cv2.imshow("Edges on Mask", edges) # Uncomment to see the edges

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
