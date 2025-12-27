import cv2
import os

def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resizes an image to a specific width or height while maintaining the aspect ratio.

    Parameters:
        image (numpy.ndarray): The image to be resized.
        width (int, optional): The target width in pixels. Defaults to None.
        height (int, optional): The target height in pixels. Defaults to None.
        inter (int, optional): The interpolation method to use. Defaults to cv2.INTER_AREA.

    Returns:
        numpy.ndarray: The resized image.
    """
    dimension = None
    (h, w) = image.shape[:2]

    # If both width and height are None, return the original image
    if width is None and height is None:
        return image

    # If width is None, calculate the new dimensions based on the target height
    if width is None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    # Otherwise, calculate the new dimensions based on the target width
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    # Resize the image using the calculated dimensions and interpolation method
    resized = cv2.resize(image, dimension, interpolation=inter)
    return resized

# The following block will only run when this script is executed directly
if __name__ == "__main__":
    # --- 1. Setup Path ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "cat.jpg")

    # --- 2. Read Image ---
    original_image = cv2.imread(img_path)

    if original_image is not None:
        # --- 3. Resize Image ---
        # Resize the image to a height of 600px while maintaining the aspect ratio
        resized_img = resize_with_aspect_ratio(original_image, height=600)

        # --- 4. Display Images ---
        cv2.imshow("Original Image", original_image)
        cv2.imshow("Resized (Aspect Ratio Preserved)", resized_img)

        print("Press any key to close all windows...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Error: Could not load image from {img_path}")