import cv2

def show_webcam_feed(device_index=0):
    """Opens the default webcam, displays the feed, and exits when 'q' is pressed."""
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"Error: Could not open webcam at index {device_index}.")
        return

    print("--- Live Webcam Feed ---")
    print("Press 'q' in the video window to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        flipped_frame = cv2.flip(frame, 1)
        cv2.imshow('Webcam Feed', flipped_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_webcam_feed()
