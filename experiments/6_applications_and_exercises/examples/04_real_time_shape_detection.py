import cv2
import numpy as np

def nothing(x):
    """Dummy callback function for trackbars."""
    pass

def main():
    """This script demonstrates real-time shape detection from a webcam feed,
    using trackbars for color isolation."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
        
    cv2.namedWindow("Settings")

    # Create trackbars for HSV color mask
    cv2.createTrackbar("Lower-Hue", "Settings", 0, 180, nothing)
    cv2.createTrackbar("Lower-Saturation", "Settings", 0, 255, nothing)
    cv2.createTrackbar("Lower-Value", "Settings", 0, 255, nothing)
    cv2.createTrackbar("Upper-Hue", "Settings", 180, 180, nothing)
    cv2.createTrackbar("Upper-Saturation", "Settings", 255, 255, nothing)
    cv2.createTrackbar("Upper-Value", "Settings", 255, 255, nothing)
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    print("--- Real-Time Shape Detection ---")
    print("Adjust trackbars to isolate a colored object. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        frame = cv2.flip(frame, 1)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Get current trackbar positions and create mask
        lh = cv2.getTrackbarPos("Lower-Hue", "Settings")
        ls = cv2.getTrackbarPos("Lower-Saturation", "Settings")
        lv = cv2.getTrackbarPos("Lower-Value", "Settings")
        uh = cv2.getTrackbarPos("Upper-Hue", "Settings")
        us = cv2.getTrackbarPos("Upper-Saturation", "Settings")
        uv = cv2.getTrackbarPos("Upper-Value", "Settings")

        lower_color = np.array([lh, ls, lv])
        upper_color = np.array([uh, us, uv])
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Clean up mask with morphological opening
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Find and Analyze Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 400: # Filter small contours
                epsilon = 0.02 * cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)
                
                x, y, w, h = cv2.boundingRect(approx)
                
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

                num_vertices = len(approx)
                if num_vertices == 3:
                    cv2.putText(frame, "Triangle", (x, y - 10), font, 1, (0, 0, 0), 2)
                elif num_vertices == 4:
                    cv2.putText(frame, "Rectangle", (x, y - 10), font, 1, (0, 0, 0), 2)
                elif num_vertices > 6:
                    cv2.putText(frame, "Circle", (x, y - 10), font, 1, (0, 0, 0), 2)
        
        cv2.imshow("Webcam", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
