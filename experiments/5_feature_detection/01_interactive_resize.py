import cv2
import os

# --- Global variables ---
# These variables will be accessed and modified by the mouse callback function.
scale_percent = 100
original_image = None

def mouse_callback(event, x, y, flags, param):
    """
    This function is called whenever a mouse event happens in the window.
    We are only interested in the scroll wheel event.
    """
    global scale_percent

    # Check if the event is a mouse wheel scroll
    if event == cv2.EVENT_MOUSEWHEEL:
        # The 'flags' parameter contains information about the scroll direction.
        # A positive value means scrolling up (zoom in), a negative value means scrolling down (zoom out).
        if flags > 0:
            scale_percent += 10
        else:
            # Prevent zooming out too much by setting a minimum scale of 10%
            scale_percent = max(10, scale_percent - 10)
        
        print(f"Current scale: {scale_percent}%")

def main():
    """
    Sets up a window where an image can be interactively resized using the mouse scroll wheel.
    """
    global original_image
    
    # --- 1. Load the initial image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    original_image = cv2.imread(img_path)

    if original_image is None:
        print(f"Error: Could not load image from {img_path}")
        return
        
    # --- 2. Setup the window and callback ---
    window_name = "Interactive Zoom (Scroll Mouse Wheel)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # Connect the 'mouse_callback' function to our window
    cv2.setMouseCallback(window_name, mouse_callback)
    
    print("--- Interactive Zoom ---")
    print("Use the mouse scroll wheel inside the window to zoom in and out.")
    print("Press 'q' to quit.")

    # --- 3. Main Application Loop ---
    # The callback function will update 'scale_percent'.
    # This loop will re-render the image based on the current scale.
    while True:
        # Calculate new dimensions based on the current scale factor
        new_width = int(original_image.shape[1] * scale_percent / 100)
        new_height = int(original_image.shape[0] * scale_percent / 100)
        
        # Resize the original image to the new dimensions
        resized_img = cv2.resize(original_image, (new_width, new_height))
        
        # Display the resized image
        cv2.imshow(window_name, resized_img)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()