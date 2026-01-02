import cv2
import numpy as np

def main():
    """This script demonstrates the use of cv2.add() for image addition."""
    # Create two images to be added
    circle_img = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.circle(circle_img, (256, 256), 60, (255, 0, 0), -1)

    rect_img = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.rectangle(rect_img, (150, 150), (350, 350), (0, 0, 255), -1)

    # cv2.add performs saturating arithmetic (clips values at 255).
    added_image = cv2.add(circle_img, rect_img)

    # Display the results
    cv2.imshow("Blue Circle", circle_img)
    cv2.imshow("Red Rectangle", rect_img)
    cv2.imshow("cv2.add() Result", added_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
