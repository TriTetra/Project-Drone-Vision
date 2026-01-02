import cv2

def main():
    """This script demonstrates real-time edge detection using the Canny
    edge detection algorithm on a live webcam feed."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("--- Canny Edge Detection on Live Video ---")
    print("Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        flipped_frame = cv2.flip(frame, 1)

        # Apply Canny Edge Detection (threshold1, threshold2)
        # Edges with gradient > threshold2 are sure edges.
        # Edges between threshold1 and threshold2 are accepted if connected to sure edges.
        edges = cv2.Canny(flipped_frame, 100, 200)

        cv2.imshow("Original Webcam Feed", flipped_frame)
        cv2.imshow("Canny Edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
