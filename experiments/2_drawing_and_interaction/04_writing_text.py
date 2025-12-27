import cv2
import numpy as np

# --- 1. Create a Blank Canvas ---
# Create a 512x512 white canvas to serve as our drawing surface.
canvas = np.zeros((512, 512, 3), dtype="uint8") + 255

# --- 2. Write Text on the Canvas ---
# The primary function for writing text is cv2.putText().
#
# Its full signature is:
# cv2.putText(image, text, org, fontFace, fontScale, color[, thickness[, lineType]])
#
# - image: The image to write on.
# - text: The string of text to be written.
# - org: The (x, y) coordinates of the bottom-left corner of the text string.
# - fontFace: The font type (e.g., cv2.FONT_HERSHEY_SIMPLEX).
# - fontScale: A factor multiplied by the font's base size to determine the final size.
# - color: The text color in BGR format (Blue, Green, Red).
# - thickness: The thickness of the lines that make up the text characters.
# - lineType: The algorithm used to draw the lines. cv2.LINE_AA is preferred as it gives anti-aliased (smoother) text.

# Example 1: A simple, standard font.
font_simple = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, "OpenCV", (10, 150), font_simple, 4, (0, 0, 0), 3, cv2.LINE_AA)

# Example 2: A more complex, serif-style font.
font_complex = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(canvas, "Machine Learning", (20, 300), font_complex, 1.5, (128, 0, 128), 2) # Purple color

# Example 3: An elegant, script-style font.
font_script = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(canvas, "Computer Vision", (30, 450), font_script, 2, (0, 128, 0), 3, cv2.LINE_AA) # Green color

# --- 3. Display the Result ---
cv2.imshow("Canvas with Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
