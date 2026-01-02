import cv2
import os

def main():
    """This script demonstrates converting an image between BGR, RGB, HSV, and Grayscale color spaces."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "klon.jpg")
    
    bgr_image = cv2.imread(img_path)
    if bgr_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Perform Color Space Conversions
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

    # Display the Results
    cv2.imshow("Original BGR Image", bgr_image)
    
    # IMPORTANT NOTE: cv2.imshow() expects BGR. RGB image will look blueish.
    cv2.imshow("RGB Image (Looks Blueish)", rgb_image)
    
    cv2.imshow("HSV Image", hsv_image)
    cv2.imshow("Grayscale Image", gray_image)

    print("Displaying image in various color spaces. Press any key to quit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
