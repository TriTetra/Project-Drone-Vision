import cv2
import numpy as np

def main():
    """This script demonstrates how to write text on an image using cv2.putText()."""
    canvas = np.zeros((512, 512, 3), dtype="uint8") + 255 # White canvas

    # Example 1: Simple font
    font_simple = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, "OpenCV", (10, 150), font_simple, 4, (0, 0, 0), 3, cv2.LINE_AA)

    # Example 2: A more complex font
    font_complex = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(canvas, "Machine Learning", (20, 300), font_complex, 1.5, (128, 0, 128), 2)

    # Example 3: A script-style font
    font_script = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(canvas, "Computer Vision", (30, 450), font_script, 2, (0, 128, 0), 3, cv2.LINE_AA)

    cv2.imshow("Canvas with Text", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
