import cv2
import os
import numpy as np

def main():
    """This script demonstrates a simplified pupil tracking simulation in a video,
    using a fixed ROI, thresholding, and contour analysis."""
    assets_path = os.path.join("..", "..", "_assets")
    video_path = os.path.join(assets_path, "eye_motion.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    print("Simulating pupil tracking. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        roi = frame[80:230, 230:450] # Fixed ROI for eye area
        h_roi, w_roi, _ = roi.shape

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        threshold = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV)[1]

        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(largest_contour) > 50: # Filter small noise
                x, y, w, h = cv2.boundingRect(largest_contour)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.line(roi, (center_x, 0), (center_x, h_roi), (0, 255, 0), 2)
                cv2.line(roi, (0, center_y), (w_roi, center_y), (0, 255, 0), 2)

        cv2.imshow("Original Frame", frame)
        cv2.imshow("ROI with Tracking", roi)
        cv2.imshow("Threshold Mask (Pupil)", threshold)

        if cv2.waitKey(80) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
