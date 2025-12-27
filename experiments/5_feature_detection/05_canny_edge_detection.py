import cv2
import os

def main():
    """
    This script demonstrates real-time edge detection using the Canny
    edge detection algorithm on a live webcam feed.
    """
    # --- 1. Initialize Video Capture ---
    # The argument '0' refers to the default webcam.
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("--- Canny Edge Detection on Live Video ---")
    print("Displaying original feed and detected edges.")
    print("Press 'q' in a window to quit.")
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Flip the frame horizontally for an intuitive mirror-like view
        flipped_frame = cv2.flip(frame, 1)

        # --- 2. Apply Canny Edge Detection ---
        # cv2.Canny(image, threshold1, threshold2) is a multi-stage algorithm.
        #
        # - threshold1: The lower threshold for the hysteresis procedure.
        # - threshold2: The upper threshold for the hysteresis procedure.
        #
        # Any edges with an intensity gradient higher than threshold2 are considered 'sure' edges.
        # Any edges below threshold1 are considered non-edges and discarded.
        # Edges that lie between the two thresholds are accepted only if they are 
        # connected to a 'sure' edge. This helps to eliminate noise.
        low_threshold = 100
        high_threshold = 200
        edges = cv2.Canny(flipped_frame, low_threshold, high_threshold)

        # --- 3. Display the Results ---
        cv2.imshow("Original Webcam Feed", flipped_frame)
        cv2.imshow("Canny Edges", edges)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # --- 4. Cleanup ---
    print("Closing all windows and releasing the webcam.")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
