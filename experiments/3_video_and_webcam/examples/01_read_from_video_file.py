import cv2
import os

def play_video_from_file(video_path):
    """Plays a video file until it ends or 'q' is pressed."""
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}")
        return

    print(f"Playing video: {os.path.basename(video_path)}. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Video Playback', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    assets_path = os.path.join("..", "..", "_assets")
    video_to_play = os.path.join(assets_path, "video.mp4")
    
    play_video_from_file(video_to_play)
