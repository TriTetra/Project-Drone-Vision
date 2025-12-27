import cv2
import os
import numpy as np

def main():
    """
    This script demonstrates a practical computer vision pipeline: detecting lines
    of a specific color (yellow) in a video. This is a common approach for tasks
    like lane detection.
    """
    # --- 1. Setup Video Capture ---
    assets_path = os.path.join("..", "_assets")
    video_path = os.path.join(assets_path, "line.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    print("Detecting yellow lines in the video. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error reading frame.")
            break

        # --- PIPELINE STEP 1: Convert to HSV Color Space ---
        # We convert from BGR to HSV for more reliable color detection, as the Hue
        # channel is less affected by lighting changes than BGR values.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # --- PIPELINE STEP 2: Create a Mask for Yellow Color ---
        # These values define the range for yellow in the HSV space.
        lower_yellow = np.array([18, 94, 140], dtype=np.uint8)
        upper_yellow = np.array([48, 255, 255], dtype=np.uint8)
        # inRange creates a binary image where white pixels represent the color we want.
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # --- PIPELINE STEP 3: Edge Detection on the Mask ---
        # We apply Canny edge detection to the mask, not the original image.
        # This ensures we only find the edges of the yellow objects.
        edges = cv2.Canny(mask, 75, 150)

        # --- PIPELINE STEP 4: Hough Transform on the Edges ---
        # Now, we find line segments on our filtered edge map.
        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=40, maxLineGap=5)

        # --- PIPELINE STEP 5: Draw Detected Lines on Original Frame ---
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                # Draw the detected line on the original color frame for visualization.
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # --- 6. Display Results ---
        cv2.imshow("Original Frame with Detected Lines", frame)
        # Uncomment the lines below to see the intermediate steps of the pipeline
        # cv2.imshow("Yellow Color Mask", mask)
        # cv2.imshow("Edges on Mask", edges)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
            
    # --- Cleanup ---
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
