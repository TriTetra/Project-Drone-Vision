import cv2
import numpy as np

# Videonun dosya yolunu belirtin
path = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\08_Exercises\\sources\\car.mp4"

# Video yakalama nesnesini başlatın
cap = cv2.VideoCapture(path)

# Tıklanılan noktaları saklayacak bir liste oluşturun
circles = []

# Fare tıklama olayını işleyen bir fonksiyon tanımlayın
def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Tıklanılan noktanın koordinatlarını listeye ekleyin
        circles.append((x, y))

# "Frame" adında bir pencere oluşturun ve fare tıklama olayını bağlayın
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

# Video akışını okuyun ve tıklanılan noktaları görselde gösterin
while 1:
    ret, frame = cap.read()
    
    # Görüntüyü yeniden boyutlandırın
    frame = cv2.resize(frame, (640, 480))
    
    # Daireleri görselde gösterin
    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), -1)
    
    # Frame'i gösterin
    cv2.imshow("Frame", frame)
    
    # ESC tuşuna basıldığında döngüyü sonlandırın
    key = cv2.waitKey(1)
    if key == 27:
        break
    # "h" tuşuna basıldığında tıklanılan noktaları temizleyin
    elif key == ord("h"):
        circles = []

# Video akışını serbest bırakın ve tüm pencereleri kapatın
cap.release()
cv2.destroyAllWindows()
