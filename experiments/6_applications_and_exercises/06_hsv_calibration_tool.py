import cv2
import numpy as np

path = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\08_Exercises\\sources\\hsv.mp4"

# webcam için path yerine sadece 0 yazmak yeterlidir
cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
# cv2.createTrackbar(Kızak Adı,Trackbar Pencere Adı,ilk değer,son değeri,kullanmıyoruz)
cv2.createTrackbar("LH","Trackbar",0,180,nothing)
cv2.createTrackbar("LS","Trackbar",0,255,nothing)
cv2.createTrackbar("LV","Trackbar",0,255,nothing)
cv2.createTrackbar("UH","Trackbar",0,180,nothing)
cv2.createTrackbar("US","Trackbar",0,255,nothing)
cv2.createTrackbar("UV","Trackbar",0,255,nothing)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1) # webcam kullanırsak ekranı aynı şekilde döndürmek için
    frame = cv2.resize(frame,(480,640))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # her tarck bar için pencere içinde bir konum veriyoruz
    lh = cv2.getTrackbarPos("LH","Trackbar")
    ls = cv2.getTrackbarPos("LS","Trackbar")
    lv = cv2.getTrackbarPos("LV","Trackbar")
    uh = cv2.getTrackbarPos("UH","Trackbar")
    us = cv2.getTrackbarPos("US","Trackbar")
    uv = cv2.getTrackbarPos("UV","Trackbar")

    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    bitwise = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()