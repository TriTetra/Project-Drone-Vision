import cv2
import os

def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    """Resizes an image to a target width or height while maintaining aspect ratio."""
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    return cv2.resize(image, dimension, interpolation=inter)

if __name__ == "__main__":
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "cat.jpg")
    
    original_image = cv2.imread(img_path)

    if original_image is not None:
        # Resize the image to a height of 600px, maintaining the aspect ratio
        resized_img = resize_with_aspect_ratio(original_image, height=600)

        cv2.imshow("Original Image", original_image)
        cv2.imshow("Resized (Aspect Ratio Preserved)", resized_img)
        
        print("Press any key to close windows.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Error: Could not load image from {img_path}")
