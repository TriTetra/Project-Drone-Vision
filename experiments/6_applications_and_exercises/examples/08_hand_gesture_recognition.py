import cv2
import numpy as np
import math

def main():
    """This script demonstrates basic hand gesture recognition by detecting a skin-colored
    region, finding its extreme points, and calculating angles."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Detecting hand gesture and marking extreme points. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        roi = frame[150:400, 220:420] # Define ROI for hand
        cv2.rectangle(frame, (220,150), (420,400), (255,0,0), 2) # Draw ROI boundary on main frame

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 45, 79], dtype=np.uint8)
        upper_skin = np.array([17, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.dilate(mask, np.ones((3,3),np.uint8), iterations=1)
        mask = cv2.medianBlur(mask, 15)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(largest_contour) > 1000: # Filter small noise
                extLeft = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])
                extRight = tuple(largest_contour[largest_contour[:, :, 0].argmax()][0])
                extTop = tuple(largest_contour[largest_contour[:, :, 1].argmin()][0])
                # extBot = tuple(largest_contour[largest_contour[:, :, 1].argmax()][0]) # Not used for angle calc

                cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)
                cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
                cv2.circle(roi, extTop, 5, (0, 255, 0), 2)

                cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)
                cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
                cv2.line(roi, extRight, extLeft, (255, 0, 0), 2)

                # Angle calculation logic (between extLeft, extTop, extRight)
                a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
                b = math.sqrt((extTop[0]-extLeft[0])**2+(extTop[1]-extLeft[1])**2)
                c = math.sqrt((extRight[0]-extLeft[0])**2+(extRight[1]-extLeft[1])**2)
                
                try:
                    angle_ab = int(math.acos((a**2 + b**2 - c**2) / (2*b*c)) * 57)
                    cv2.putText(roi, str(angle_ab), (extRight[0]+10, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    if angle_ab > 70: # Example logic for simple gesture
                        cv2.rectangle(frame, (0, 0), (100, 100), (255, 0, 0), -1)
                except:
                    cv2.putText(roi, "?", (extRight[0]+10, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Webcam Feed", frame)
        cv2.imshow("Skin Mask", mask)
        cv2.imshow("Hand ROI", roi)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
