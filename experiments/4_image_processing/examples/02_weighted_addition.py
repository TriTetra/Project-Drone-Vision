import cv2
import numpy as np

def main():
    """This script demonstrates image blending (weighted addition) using cv2.addWeighted()."""
    # Create two images to be blended
    image1 = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.circle(image1, (256, 256), 60, (255, 0, 0), -1)

    image2 = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.rectangle(image2, (150, 150), (350, 350), (0, 0, 255), -1)

    # cv2.addWeighted(src1, alpha, src2, beta, gamma)
    alpha = 0.7
    beta = 0.3
    gamma = 0
    
    blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

    # Display the results
    cv2.imshow("Image 1 (Weight: 0.7)", image1)
    cv2.imshow("Image 2 (Weight: 0.3)", image2)
    cv2.imshow("Blended Result", blended_image)

    print("Two images blended using cv2.addWeighted(). Press any key to close all windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
