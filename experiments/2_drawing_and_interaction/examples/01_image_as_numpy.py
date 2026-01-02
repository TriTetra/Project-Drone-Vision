import cv2
import numpy as np

def main():
    """
    This script demonstrates that an image is fundamentally a NumPy array
    and how to manipulate individual pixels to create a simple image.
    """
    canvas_height, canvas_width = 10, 10
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype="uint8")

    # Manipulate Individual Pixels
    canvas[0, 0] = (255, 255, 255)  # Top-left pixel to White
    canvas[0, 1] = (0, 0, 255)      # Second pixel to Red
    canvas[0, 2] = (0, 255, 0)      # Third pixel to Green
    canvas[0, 3] = (255, 0, 0)      # Fourth pixel to Blue

    # Enlarge for visualization as the original 10x10 image is too small to see.
    large_canvas = cv2.resize(canvas, (500, 500), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("A 10x10 Image, Enlarged to 500x500", large_canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
