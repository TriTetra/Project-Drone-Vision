'''
import math
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findMaxCountors(countors):
    max_i = 0
    max_area = 0

    for i in range(len(countors)):
        area_face = cv2.contourArea(countors[i])
        if max_area < area_face:
            max_area = area_face
            max_i = i
        
        try:
            c = countors[max_i]
        except:
            countors = [0]
            c = countors[0]

        return c

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[150:400,220:420] # -> rectangle = (x, y, width, height), frame[y1:y2,x1:x2]
    cv2.rectangle(frame,(220,150),(420,400),(255,0,0),0)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((3,3),np.uint8)
    mask1 = cv2.dilate(mask,kernel,iterations=1)
    mask2 = cv2.medianBlur(mask,15)

    countors,_ = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(countors) > 0 :

            c = findMaxCountors(countors)

            extLeft = tuple(c[c[:,:,0].argmin()][0])
            extRight = tuple(c[c[:,:,0].argmax()][0])
            extTop = tuple(c[c[:,:,1].argmin()][0])
            extBot = tuple(c[c[:,:,1].argmax()][0])

            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            cv2.circle(roi,extBot,5,(0,255,0),2)

            cv2.line(roi,extLeft,extTop,(255,0,0),2)
            cv2.line(roi,extTop,extRight,(255,0,0),2)
            cv2.line(roi,extRight,extBot,(255,0,0),2)
            cv2.line(roi,extBot,extLeft,(255,0,0),2)

            a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
            b = math.sqrt((extBot[0]-extRight[0])**2+(extBot[1]-extRight[1])**2)
            c = math.sqrt((extBot[0]-extTop[0])**2+(extBot[1]-extTop[1])**2)

            try:
                angle_ab = int(math.acos((a**2 + b**2-c**2)/(2*b*c))*57)
                cv2.putText(roi,str(angle_ab),(extRight[0]+10,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            except:
                cv2.putText(roi,"?",(extRight[0]+10,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)


    cv2.imshow("Frame",frame)
    cv2.imshow("Roi",roi)
    #cv2.imshow("HSV",hsv)
    cv2.imshow("Mask",mask)
    #cv2.imshow("Mask1",mask1)
    #cv2.imshow("Mask2",mask2)


    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

'''

import math
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findMaxCountors(countors):
    """
    Bu fonksiyon, bir kontür listesindeki en büyük alana sahip kontürü bulur.

    Args:
        countors: Bir kontürler listesi.

    Returns:
        En büyük alana sahip kontür.
    """
    max_i = 0  # En büyük alanlı kontürün indeksi
    max_area = 0  # En büyük alan değeri

    # Her kontür için alan hesaplanır ve en büyük alan ve indeksi takip edilir.
    for i in range(len(countors)):
        area_face = cv2.contourArea(countors[i])
        if max_area < area_face:
            max_area = area_face
            max_i = i

    # Hata yakalama bloğu, potansiyel IndexError hatasını ele alır.
    try:
        c = countors[max_i]  # En büyük alanlı kontür seçilir.
    except:
        countors = [0]  # Hata durumunda boş bir liste oluşturulur.
        c = countors[0]  # Boş listeden varsayılan olarak ilk eleman (0. indeks) seçilir.

    return c  # En büyük alanlı kontür döndürülür.

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Çerçeveyi yatay olarak çevirir (isteğe bağlı)

    roi = frame[150:400, 220:420]  # İlgi Alanı (ROI) tanımlanır
    cv2.rectangle(frame, (220, 150), (420, 400), (255, 0, 0), 0)  # ROI üzerine kırmızı bir dikdörtgen çizer

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # ROI'yi HSV renk uzayına dönüştürür
    lower_color = np.array([0, 45, 79], dtype=np.uint8)  # Cilt algılama için alt renk sınırları
    upper_color = np.array([17, 255, 255], dtype=np.uint8)  # Cilt algılama için üst renk sınırları

    mask = cv2.inRange(hsv, lower_color, upper_color)  # Cilt benzeri bölgeleri izole etmek için bir maske oluşturur
    kernel = np.ones((3, 3), np.uint8)  # Morfolojik işlemler için 3x3 çekirdek tanımlar
    mask1 = cv2.dilate(mask, kernel, iterations=1)  # Küçük delikleri doldurmak için maskeyi genişletir
    mask2 = cv2.medianBlur(mask, 15)  # Gürültüyü azaltmak için medyan bulanıklaştırma uygular

    countors, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Maskede kontürleri bulur

    if len(countors) > 0:  # En az bir kontür algılanırsa

        c = findMaxCountors(countors)  # En büyük alana sahip kontürü bulur

        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # En soldaki noktayı (minimum x-koordinatı) bulur
        extRight = tuple(c[c[:, :, 0].argmax()][0])  # En sağdaki noktayı (maksimum x-koordinatı) bulur
        extTop = tuple(c[c[:, :, 1].argmin()][0])  # En üstteki noktayı (minimum y-koordinatı) bulur
        extBot = tuple(c[c[:, :, 1].argmax()][0])  # En alttaki noktayı (maksimum y-koordinatı) bulur

        # Kontürün extrema (köşe noktaları) üzerine daireler çizer
        cv2.circle(roi,extLeft,5,(0,255,0),2) #yeşil daire
        cv2.circle(roi,extRight,5,(0,255,0),2)
        cv2.circle(roi,extTop,5,(0,255,0),2)
        cv2.circle(roi,extBot,5,(0,255,0),2)

        # Kontürün extrema (köşe noktaları) arasındaki çizgileri çizer
        cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)  # Mavi çizgi
        cv2.line(roi, extTop, extRight, (255, 0, 0), 2)  # Mavi çizgi
        cv2.line(roi, extRight, extBot, (255, 0, 0), 2)  # Mavi çizgi
        cv2.line(roi, extBot, extLeft, (255, 0, 0), 2)  # Mavi çizgi

        # Sağ üst köşeye açıyı hesaplar ve metin olarak ekler
        a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)  # Sağ üst kenar uzunluğu
        b = math.sqrt((extBot[0]-extRight[0])**2+(extBot[1]-extRight[1])**2)  # Sağ yan kenar uzunluğu
        c = math.sqrt((extBot[0]-extTop[0])**2+(extBot[1]-extTop[1])**2)  # Hipotenüs uzunluğu

        try:
            angle_ab = int(math.acos((a**2 + b**2 - c**2) / (2*b*c)) * 57)  # Açı (derece) hesaplanır
            cv2.putText(roi, str(angle_ab), (extRight[0]+10, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)  # Açı değeri yazdırılır
        except:
            cv2.putText(roi, "?", (extRight[0]+10, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)  # Hata durumunda soru işareti yazdırılır

    cv2.imshow("Frame", frame)
    cv2.imshow("Roi", roi)
    # cv2.imshow("HSV", hsv)  # HSV görüntülemeyi isteğe bağlı olarak kaldırabilirsiniz.
    # cv2.imshow("Mask", mask)  # Maskeyi görüntülemeyi isteğe bağlı olarak kaldırabilirsiniz.
    # cv2.imshow("Mask1", mask1)  # Aşamalı maskeyi görüntülemeyi isteğe bağlı olarak kaldırabilirsiniz.
    # cv2.imshow("Mask2", mask2)  # Bulanıklaştırılmış maskeyi görüntülemeyi isteğe bağlı olarak kaldırabilirsiniz.

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

