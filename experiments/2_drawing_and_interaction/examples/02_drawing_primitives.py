import cv2
import numpy as np

def main():
    """
    This script demonstrates how to draw various geometric shapes
    (lines, rectangles, circles, polygons) on a canvas using OpenCV.
    """
    # Create a 512x512 white canvas
    canvas = np.zeros((512, 512, 3), dtype="uint8") + 255

    # Draw a blue line
    cv2.line(canvas, (50, 50), (250, 250), (255, 0, 0), 5)

    # Draw a red line
    cv2.line(canvas, (50, 20), (170, 200), (0, 0, 255), 4)

    # Draw a green outlined rectangle
    cv2.rectangle(canvas, (80, 80), (120, 120), (0, 255, 0), 2)

    # Draw a filled rectangle
    cv2.rectangle(canvas, (300, 300), (500, 500), (80, 120, 160), -1)

    # Draw a gray circle
    cv2.circle(canvas, (200, 150), 80, (150, 150, 150), 4)

    # Draw a triangle using cv2.polylines
    triangle_pts = np.array([[300, 100], [250, 150], [350, 150]], np.int32)
    triangle_pts = triangle_pts.reshape((-1, 1, 2))
    cv2.polylines(canvas, [triangle_pts], True, (0, 0, 0), 3)

    # Draw a complex polygon (quadrilateral)
    quad_pts = np.array([[110, 400], [330, 400], [350, 450], [290, 420]], np.int32)
    quad_pts = quad_pts.reshape((-1, 1, 2))
    cv2.polylines(canvas, [quad_pts], True, (100, 0, 100), 5)

    cv2.imshow("Canvas with Shapes", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
