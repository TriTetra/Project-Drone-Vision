import cv2
import numpy as np

path1 = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\09_Exercise_second\\source\\aircraft.jpg"
path2 = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\09_Exercise_second\\source\\aircraft_compare.jpg"


img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(320,480))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(320,480))

img3 = cv2.medianBlur(img1,7)

if img1.shape == img2.shape:
    print("same size")
elif img1.shape != img2.shape:
    print("not same")
else:
    print("trg again")

diff = cv2.subtract(img1,img3)
b,g,r = cv2.split(diff)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(b) == 0 and cv2.countNonZero(b) == 0:
    print("completely equal")
else:
    print("Not completely equal")


cv2.imshow("Aircraft",img1)
cv2.imshow("Aircraft2",img2)
cv2.imshow("Difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()