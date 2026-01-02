import cv2
import os

def main():
    """This script reads an image and prints its core properties."""
    # Construct a relative path to the assets directory
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "forest.jpg")
    
    image = cv2.imread(img_path)
    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # Extract properties from the image object
    height, width, _ = image.shape
    channels = image.shape[2] if len(image.shape) == 3 else 1
    total_pixels = image.size
    data_type = image.dtype

    # Print the collected properties to the console
    print("--- Image Properties ---")
    print(f"Dimensions: {width}x{height}")
    print(f"Channels: {channels}")
    print(f"Total Pixels: {total_pixels:,}")
    print(f"Data Type: {data_type}")

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
