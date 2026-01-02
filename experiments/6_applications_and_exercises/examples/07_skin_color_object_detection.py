import cv2
import numpy as np

def main():
    """This script demonstrates detecting a skin-colored region in a webcam feed
    and finding its extreme points using contour analysis."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Detecting skin-colored region and marking extreme points. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        # Define a Region of Interest (ROI) for potential face/hand area
        roi = frame[150:400, 220:420] 
        cv2.rectangle(frame,(220,150),(420,400),(255,0,0),2) # Draw boundary for ROI

        # Convert ROI to HSV and apply skin color mask
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 45, 79], dtype=np.uint8)
        upper_skin = np.array([17, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Clean up mask (dilate then median blur)
        mask = cv2.dilate(mask, np.ones((3,3),np.uint8), iterations=1)
        mask = cv2.medianBlur(mask, 15)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            # Find the largest contour (assumed to be the main skin region)
            largest_contour = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(largest_contour) > 1000: # Filter small noise
                # Find extreme points of the largest contour
                extLeft = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])
                extRight = tuple(largest_contour[largest_contour[:, :, 0].argmax()][0])
                extTop = tuple(largest_contour[largest_contour[:, :, 1].argmin()][0])
                extBot = tuple(largest_contour[largest_contour[:, :, 1].argmax()][0])

                # Draw circles on extreme points within the ROI
                cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)
                cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
                cv2.circle(roi, extTop, 5, (0, 255, 0), 2)
                cv2.circle(roi, extBot, 5, (0, 255, 0), 2)

        cv2.imshow("Webcam Feed", frame)
        cv2.imshow("Skin Mask", mask)
        cv2.imshow("ROI (Processed)", roi)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
