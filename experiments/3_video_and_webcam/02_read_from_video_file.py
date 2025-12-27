import cv2
import os

def play_video_from_file(video_path):
    """
    Opens and plays a video from a file in a window.
    The video plays until it ends or until the 'q' key is pressed.

    Parameters:
        video_path (str): The full path to the video file.
    """
    # Create a VideoCapture object using the provided file path.
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully.
    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return  # Exit the function if the video cannot be opened.

    print(f"Playing video: {os.path.basename(video_path)}")
    print("Press 'q' in the video window to quit.")

    # Loop as long as the video capture object is open.
    while cap.isOpened():
        # Read the next frame from the video.
        # 'ret' is a boolean that is True if a frame was read successfully, False otherwise.
        # 'frame' contains the image data of the frame.
        ret, frame = cap.read()

        # If 'ret' is False, we have reached the end of the video or an error occurred.
        if not ret:
            print("End of video reached or error reading frame.")
            break

        # Here, you could perform any desired processing on the frame.
        # Example: frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the current frame in a window named 'Video Playback'.
        cv2.imshow('Video Playback', frame)

        # Wait for 25 milliseconds for a key press.
        # This delay creates a playback speed of about 40 FPS (1000ms / 25ms = 40 FPS).
        # If the 'q' key is pressed, break the loop.
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # --- Cleanup ---
    # Always release the VideoCapture object to free up resources.
    cap.release()
    # Destroy all windows created by OpenCV.
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Construct the path to the video in the shared assets folder
    assets_path = os.path.join("..", "_assets")
    video_to_play = os.path.join(assets_path, "video.mp4")
    
    # Call the function to play the video
    play_video_from_file(video_to_play)
