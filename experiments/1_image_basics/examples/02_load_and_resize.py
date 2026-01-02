import cv2
import os

def main():
    """
    This script demonstrates loading an image, resizing it to a fixed
    size, and displaying both the original and the result.
    """
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "cat.jpg")
    
    original_image = cv2.imread(img_path)
    if original_image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    print(f"Original image shape: {original_image.shape}")

    # Resize the image to a fixed 300x300 pixel square
    target_size = (300, 300)
    resized_image = cv2.resize(original_image, target_size)
    print(f"Resized image shape: {resized_image.shape}")

    # Display both images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Resized Image", resized_image)
    
    print("Press any key to close windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
