import cv2
import numpy as np

def main():
    """
    This script demonstrates the use of cv2.add() to combine two images.
    """
    # --- 1. Create two images to be added ---

    # Create a white canvas (512x512) and draw a solid blue circle on it.
    circle_img = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.circle(circle_img, (256, 256), 60, (255, 0, 0), -1)  # Blue in BGR

    # Create a second white canvas and draw a solid red rectangle on it.
    rect_img = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.rectangle(rect_img, (150, 150), (350, 350), (0, 0, 255), -1)  # Red in BGR

    # --- 2. Add the images using cv2.add() ---
    # cv2.add performs saturating arithmetic. This means that if the sum of
    # pixel values in a channel is greater than 255, the value is clipped to 255.
    # For example, in the overlapping area:
    # Blue channel: 255 (from circle) + 0 (from rect) = 255
    # Red channel: 0 (from circle) + 255 (from rect) = 255
    # The result is (255, 0, 255), which is Magenta.
    added_image = cv2.add(circle_img, rect_img)

    # Inspect the pixel value in the center, where the shapes overlap.
    center_pixel_value = added_image[256, 256]
    print(f"Pixel value at the center (256, 256) of the added image: {center_pixel_value}")
    print("This BGR value corresponds to Magenta (Blue + Red).")

    # --- 3. Display the results ---
    cv2.imshow("Blue Circle", circle_img)
    cv2.imshow("Red Rectangle", rect_img)
    cv2.imshow("cv2.add() Result", added_image)

    print("\nPress any key to close all windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()