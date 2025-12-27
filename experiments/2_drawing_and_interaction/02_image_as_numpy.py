import cv2
import numpy as np

# --- 1. An Image is a NumPy Array ---
# We can create a blank, black image from scratch using np.zeros.
# The shape is defined as (height, width, channels).
# The data type 'uint8' is standard for 8-bit color channels (0-255).
canvas_height = 10
canvas_width = 10
canvas = np.zeros((canvas_height, canvas_width, 3), dtype="uint8")

# --- 2. Manipulate Individual Pixels ---
# We can access and change the color of any pixel using its [row, column] index.
# The color is assigned as a (Blue, Green, Red) tuple.
print("Coloring the first four pixels in the top row...")
canvas[0, 0] = (255, 255, 255)  # Top-left pixel to White
canvas[0, 1] = (0, 0, 255)      # Second pixel to Red
canvas[0, 2] = (0, 255, 0)      # Third pixel to Green
canvas[0, 3] = (255, 0, 0)      # Fourth pixel to Blue

# --- 3. Visualize the Tiny Image ---
# The 10x10 image is too small to see clearly on a modern display.
# To visualize the pixels we just changed, we can resize the image to a much larger size.
# We use the 'INTER_NEAREST' interpolation method, which enlarges the image
# without blurring the pixels, keeping the sharp, blocky look.
large_canvas = cv2.resize(canvas, (500, 500), interpolation=cv2.INTER_NEAREST)

# --- 4. Display the Result ---
cv2.imshow("A 10x10 Image, Enlarged to 500x500", large_canvas)
print("A 10x10 canvas was created and its first 4 pixels were colored.")
print("It has been scaled up so you can see the individual pixels.")
print("\nPress any key to close the window.")
cv2.waitKey(0)
cv2.destroyAllWindows()
