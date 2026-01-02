import cv2
import os
from matplotlib import pyplot as plt

def main():
    """This script demonstrates how to compute and display a color histogram for an image."""
    assets_path = os.path.join("..", "..", "_assets")
    img_path = os.path.join(assets_path, "smile.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    channels = cv2.split(image)
    colors = ("b", "g", "r")

    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")

    for (channel, color) in zip(channels, colors):
        plt.hist(channel.ravel(), bins=256, range=[0, 256], color=color)
        plt.xlim([0, 256])

    print("Displaying the color histogram in a Matplotlib window...")
    plt.show()

if __name__ == "__main__":
    main()
