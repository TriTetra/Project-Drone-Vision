import cv2
import numpy as np

# --- 1. Create a Blank Canvas ---
# Create a 512x512 black canvas of type uint8 (8-bit integer, 0-255).
# We add 255 to every pixel to make the canvas white instead of black.
canvas = np.zeros((512, 512, 3), dtype="uint8") + 255

# --- 2. Draw Various Shapes on the Canvas ---

# Draw a blue line using: cv2.line(canvas, start_point, end_point, color, thickness)
cv2.line(canvas, (50, 50), (250, 250), (255, 0, 0), 5)

# Draw a red line
cv2.line(canvas, (50, 20), (170, 200), (0, 0, 255), 4)

# Draw a green outlined rectangle using: cv2.rectangle(canvas, top_left, bottom_right, color, thickness)
cv2.rectangle(canvas, (80, 80), (120, 120), (0, 255, 0), 2)

# Draw a filled rectangle by setting the thickness to -1
cv2.rectangle(canvas, (300, 300), (500, 500), (80, 120, 160), -1)

# Draw a gray circle using: cv2.circle(canvas, center_coordinates, radius, color, thickness)
cv2.circle(canvas, (200, 150), 80, (150, 150, 150), 4)

# Draw a triangle using cv2.polylines, which is used for any polygon.
# First, define the vertices of the triangle.
triangle_pts = np.array([[300, 100], [250, 150], [350, 150]], np.int32)
# Reshape points into the format required by polylines.
triangle_pts = triangle_pts.reshape((-1, 1, 2))
# Use cv2.polylines(canvas, [array_of_points], is_closed, color, thickness)
cv2.polylines(canvas, [triangle_pts], True, (0, 0, 0), 3)

# Draw a more complex polygon (a quadrilateral)
quad_pts = np.array([[110, 400], [330, 400], [350, 450], [290, 420]], np.int32)
quad_pts = quad_pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [quad_pts], True, (100, 0, 100), 5)

# --- 3. Display the Result ---
cv2.imshow("Canvas with Shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()