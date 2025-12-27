import cv2
import numpy as np

def nothing(x):
    """
    Callback function for createTrackbar. It is executed whenever a
    trackbar value changes. We don't need it to do anything for this
    example, so we just 'pass'.
    """
    pass

# --- 1. Setup Canvas and Window ---
# Create a black image (canvas) to display the color.
# Create a named window which will hold both the canvas and the trackbars.
window_name = "Interactive Color Mixer"
canvas = np.zeros((300, 512, 3), dtype="uint8")
cv2.namedWindow(window_name)

# --- 2. Create Trackbars ---
# cv2.createTrackbar(trackbarName, windowName, default_value, max_value, onChange_callback)
cv2.createTrackbar("R", window_name, 0, 255, nothing)
cv2.createTrackbar("G", window_name, 0, 255, nothing)
cv2.createTrackbar("B", window_name, 0, 255, nothing)
cv2.createTrackbar("ON / OFF", window_name, 0, 1, nothing)

print("--- Interactive Color Mixer ---")
print("Adjust the R, G, B sliders to mix a color.")
print("Use the 'ON / OFF' switch to toggle the color.")
print("Press 'q' in the window to quit.")

while True:
    # Display the canvas, which will be updated with the new color in each loop iteration.
    cv2.imshow(window_name, canvas)

    # Wait for 1ms. If 'q' is pressed, break the loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # --- 3. Get Current Positions of Trackbars ---
    # cv2.getTrackbarPos(trackbarName, windowName) reads the current value of a slider.
    r = cv2.getTrackbarPos("R", window_name)
    g = cv2.getTrackbarPos("G", window_name)
    b = cv2.getTrackbarPos("B", window_name)
    switch = cv2.getTrackbarPos("ON / OFF", window_name)

    # --- 4. Update the Canvas Based on Trackbar Values ---
    if switch == 1:
        # If the switch is ON, set the entire canvas color to the BGR values.
        # Note that the trackbars are named R,G,B for user convenience,
        # but OpenCV uses the BGR order.
        canvas[:] = [b, g, r]
    else:
        # If the switch is OFF, keep the canvas black.
        canvas[:] = 0

# --- 5. Cleanup ---
# Close all OpenCV windows when the loop is exited.
cv2.destroyAllWindows()