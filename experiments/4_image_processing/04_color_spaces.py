import cv2
import os

def main():
    """
    This script demonstrates converting an image from the default BGR color space
    to other common color spaces like RGB, HSV, and Grayscale using cv2.cvtColor().
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "klon.jpg")
    
    # By default, cv2.imread loads an image in the BGR (Blue, Green, Red) color space.
    bgr_image = cv2.imread(img_path)

    if bgr_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Perform Color Space Conversions ---
    # The function for all conversions is cv2.cvtColor(source_image, conversion_code).

    # Convert from BGR to RGB. This is common when working with other libraries
    # like Matplotlib or PIL that expect RGB order.
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    # Convert from BGR to HSV (Hue, Saturation, Value).
    # HSV is excellent for color-based segmentation and filtering because the color (Hue)
    # is separated from brightness/intensity.
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # Convert from BGR to Grayscale.
    # Used when color information is not needed, simplifying many algorithms.
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)


    # --- 3. Display the Results ---
    cv2.imshow("Original BGR Image", bgr_image)
    
    # IMPORTANT NOTE: cv2.imshow() expects an image in BGR format. 
    # When we pass it an RGB image, it displays the channels as if they were BGR.
    # This causes the Red and Blue channels to appear swapped.
    cv2.imshow("RGB Image (Looks Blueish)", rgb_image)
    
    cv2.imshow("HSV Image", hsv_image)
    cv2.imshow("Grayscale Image", gray_image)

    print("Displaying image in various color spaces. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
