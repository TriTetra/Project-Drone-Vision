import cv2

def show_webcam_feed(device_index=0):
    """
    Opens the default webcam, displays the feed in a window, and exits when 'q' is pressed.

    Parameters:
        device_index (int): The index of the video capturing device to open. 
                          0 is typically the default built-in webcam.
    """
    # Create a VideoCapture object. The argument is the device index.
    cap = cv2.VideoCapture(device_index)

    # Check if the webcam was opened successfully.
    if not cap.isOpened():
        print(f"Error: Could not open webcam at index {device_index}.")
        return

    print("--- Live Webcam Feed ---")
    print("Press 'q' in the video window to quit.")

    while True:
        # Capture frame-by-frame from the webcam.
        # 'ret' is a boolean indicating if the frame was captured successfully.
        # 'frame' is the captured image.
        ret, frame = cap.read()

        # if a frame was not captured correctly, break the loop.
        if not ret:
            print("Error: Can't receive frame from webcam. Exiting...")
            break

        # Flipping the frame horizontally (around the y-axis) using cv2.flip.
        # A second argument of 1 means horizontal flip. This creates an intuitive "mirror" view.
        flipped_frame = cv2.flip(frame, 1)

        # Display the resulting flipped frame.
        cv2.imshow('Webcam Feed', flipped_frame)

        # Wait for 1ms. If the 'q' key is pressed during this time, break the loop.
        # A short waitKey delay is essential for live video to feel real-time.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # --- Cleanup ---
    # When the loop is finished, release the capture object to free the webcam resource.
    print("Closing webcam feed.")
    cap.release()
    # Destroy all of the HighGUI windows.
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Call the function to start the webcam feed.
    show_webcam_feed()
