import cv2

# Görüntü dosya yollarını tanımla
img_first = "C:\\Users\\Dimoontri\\Desktop\\opencv_udemy\\08_Exercises\\sources\\polygons.png"
img_second = "C:\\Users\\Dimoontri\\Desktop\\opencv_udemy\\08_Exercises\\sources\\polygons2.jpg"

# Kullanılacak fontları tanımla
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX

# İki görüntüyü oku
img1 = cv2.imread(img_first)
img2 = cv2.imread(img_second)

# Görüntüleri gri tonlamaya çevir
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Görüntüleri eşikle (thresholding)
_, threshold1 = cv2.threshold(gray1, 240, 255, cv2.THRESH_BINARY)
_, threshold2 = cv2.threshold(gray2, 240, 255, cv2.THRESH_BINARY)

# Konturları bul
contours1, _ = cv2.findContours(threshold1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları işle
for cnt in contours1:
    # Kontur yaklaşık poligonunu hesapla
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    # Konturu çiz
    cv2.drawContours(img1, [approx], 0, (0), 5)

    # Konturun bir köşesini al
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # Şekil adını belirle ve görüntü üzerine yaz
    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), font1, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img1, "Rectangle", (x, y), font1, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y), font1, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img1, "Hexagon", (x, y), font1, 1, (0))
    else:
        cv2.putText(img1, "Ellipse", (x, y), font1, 1, (0))

# İkinci görüntü için aynı işlemleri yap
for cnt in contours2:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(img2, [approx], 0, (0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img2, "Triangle", (x, y), font2, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img2, "Rectangle", (x, y), font2, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img2, "Pentagon", (x, y), font2, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img2, "Hexagon", (x, y), font2, 1, (0))
    else:
        cv2.putText(img2, "Ellipse", (x, y), font2, 1, (0))

# İlk görüntüyü ekranda göster
cv2.imshow("IMG1", img1)

# İkinci görüntüyü ekranda göster
cv2.imshow("IMG2", img2)

# Kullanıcının herhangi bir tuşa basmasını bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
