import cv2
import numpy as np

def main():
    """
    This script demonstrates image blending (weighted addition) using cv2.addWeighted().
    """
    # --- 1. Create Two Images to be Blended ---

    # Create a white canvas and draw a solid blue circle on it.
    image1 = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.circle(image1, (256, 256), 60, (255, 0, 0), -1)  # Blue circle

    # Create a second white canvas and draw a solid red rectangle on it.
    image2 = np.zeros((512, 512, 3), np.uint8) + 255
    cv2.rectangle(image2, (150, 150), (350, 350), (0, 0, 255), -1)  # Red rectangle

    # --- 2. Blend the Images Using cv2.addWeighted() ---
    # This function calculates the weighted sum of two arrays using the formula:
    # result = alpha * image1 + beta * image2 + gamma
    #
    # - alpha: Weight for the first image.
    # - beta:  Weight for the second image.
    # - gamma: A scalar added to each sum (often left at 0).
    #
    # To create a smooth blend or transparency effect, alpha + beta usually equals 1.0.
    alpha = 0.7  # 70% weight for the first image
    beta = 0.3   # 30% weight for the second image
    gamma = 0
    
    blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

    # --- 3. Display the Results ---
    cv2.imshow("Image 1 (Weight: 0.7)", image1)
    cv2.imshow("Image 2 (Weight: 0.3)", image2)
    cv2.imshow("Blended Result", blended_image)

    print("Two images have been blended using cv2.addWeighted().")
    print("\nPress any key to close all windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()