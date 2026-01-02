import cv2
import os

scale_percent = 100
original_image = None

def mouse_callback(event, x, y, flags, param):
    """Callback function for mouse events."""
    global scale_percent
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            scale_percent += 10
        else:
            scale_percent = max(10, scale_percent - 10)
        print(f"Current scale: {scale_percent}%")

def main():
    global original_image
    
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "helicopter.jpg")
    original_image = cv2.imread(img_path)

    if original_image is None:
        print(f"Error: Could not load image from {img_path}")
        return
        
    window_name = "Interactive Zoom (Scroll Mouse Wheel)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(window_name, mouse_callback)
    
    print("--- Interactive Zoom ---")
    print("Use the mouse scroll wheel inside the window to zoom in and out.")
    print("Press 'q' to quit.")

    while True:
        new_width = int(original_image.shape[1] * scale_percent / 100)
        new_height = int(original_image.shape[0] * scale_percent / 100)
        resized_img = cv2.resize(original_image, (new_width, new_height))
        
        cv2.imshow(window_name, resized_img)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
