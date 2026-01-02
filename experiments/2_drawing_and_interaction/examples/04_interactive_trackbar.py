import cv2
import numpy as np

def nothing(x):
    """Dummy callback function for trackbars."""
    pass

def main():
    """This script demonstrates creating interactive trackbars to control
    the color of a canvas in real-time."""
    window_name = "Interactive Color Mixer"
    canvas = np.zeros((300, 512, 3), dtype="uint8")
    cv2.namedWindow(window_name)

    # Create trackbars for R, G, B color channels and an ON/OFF switch
    cv2.createTrackbar("R", window_name, 0, 255, nothing)
    cv2.createTrackbar("G", window_name, 0, 255, nothing)
    cv2.createTrackbar("B", window_name, 0, 255, nothing)
    cv2.createTrackbar("ON / OFF", window_name, 0, 1, nothing)

    print("--- Interactive Color Mixer ---")
    print("Adjust the R, G, B sliders to mix a color.")
    print("Use the 'ON / OFF' switch to toggle the color on and off.")
    print("Press 'q' to quit.")

    while True:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Get current positions of the trackbars
        r = cv2.getTrackbarPos("R", window_name)
        g = cv2.getTrackbarPos("G", window_name)
        b = cv2.getTrackbarPos("B", window_name)
        switch = cv2.getTrackbarPos("ON / OFF", window_name)

        # Update the canvas color based on trackbar values
        if switch == 1:
            canvas[:] = [b, g, r] # BGR order
        else:
            canvas[:] = 0

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
