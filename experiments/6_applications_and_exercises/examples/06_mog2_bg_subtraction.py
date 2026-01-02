import cv2
import os

def main():
    """This script demonstrates background subtraction using the MOG2 algorithm.
    MOG2 is robust to lighting changes and can model dynamic backgrounds."""
    assets_path = os.path.join("..", "..", "_assets")
    video_path = os.path.join(assets_path, "car.mp4")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    # Create background subtractor object (MOG2 algorithm)
    # varThreshold: Threshold on the squared Mahalanobis distance to decide if a pixel is foreground.
    subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

    print("Detecting motion using MOG2 background subtractor. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Apply background subtraction
        mask = subtractor.apply(frame)

        cv2.imshow("Original Video", frame)
        cv2.imshow("MOG2 Motion Mask", mask)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
