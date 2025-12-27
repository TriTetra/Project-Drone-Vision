import cv2
import os
from matplotlib import pyplot as plt

def main():
    """
    This script demonstrates how to compute and display a color histogram for an image
    using OpenCV and Matplotlib. A histogram shows the distribution of pixel 
    intensities for each color channel.
    """
    # --- 1. Setup Path and Load Image ---
    assets_path = os.path.join("..", "_assets")
    img_path = os.path.join(assets_path, "smile.jpg")
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not load image from {img_path}")
        return

    # --- 2. Calculate and Plot the Histogram ---
    
    # A histogram plots the frequency (number of pixels) for each intensity value (0-255).
    # We will plot the histogram for each color channel (Blue, Green, Red) on the same graph.
    
    # Split the image into its respective B, G, R channels.
    channels = cv2.split(image)
    colors = ("b", "g", "r")

    # Create a new Matplotlib figure
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins (Pixel Intensity: 0-255)")
    plt.ylabel("Number of Pixels")

    # Loop over the image channels and plot the histogram for each
    for (channel, color) in zip(channels, colors):
        # .ravel() flattens the 2D image array into a 1D list, which is
        # the required input format for matplotlib's hist() function.
        # Parameters for hist(): data, number_of_bins, range_of_values.
        plt.hist(channel.ravel(), bins=256, range=[0, 256], color=color)
        plt.xlim([0, 256]) # Set the x-axis limits

    # --- 3. Display the Plot ---
    # plt.show() displays the matplotlib figure in a new interactive window.
    print("Displaying the color histogram in a Matplotlib window...")
    plt.show()

if __name__ == "__main__":
    main()
