# OpenCV Deneyleri Projesi - Hızlı Bakış ve Sunum Rehberi

Bu döküman, projede ele alınan OpenCV konularının seviyelere göre gruplandırılmış bir özetini ve toplantı sırasında canlı demo için kullanılabilecek en uygun betiklerin (script) listesini içerir.

---

## 1. Temel Seviye Konular

Bu bölüm, OpenCV'nin en temel fonksiyonlarını içerir. Görüntü ve videolarla ilk tanışma için idealdir.

- **Görüntü Okuma, Yazma, Gösterme ve Temel Özellikler**
  - Bir görüntünün dosya sisteminden nasıl okunduğunu, ekranda bir pencerede nasıl gösterildiğini ve temel özelliklerinin (boyut, veri tipi vb.) nasıl alındığını gösterir.
  - **Canlı Demo Önerisi:** `experiments/1_image_basics/07_image_properties.py`

- **Şekil ve Metin Çizimi**
  - Boş bir tuval veya bir resim üzerine programatik olarak çizgi, dikdörtgen, daire ve metin ekleme işlemlerini kapsar.
  - **Canlı Demo Önerisi:** `experiments/2_drawing_and_interaction/03_drawing_functions.py`

- **Video ve Webcam Kullanımı**
  - Bir video dosyasını veya canlı webcam akışını kare kare okuma ve ekranda gösterme.
  - **Canlı Demo Önerisi:** `experiments/3_video_and_webcam/03_capture_from_webcam.py`

---

## 2. Orta Seviye Konular

Bu bölüm, görüntülerin içeriğini ve yapısını değiştirmeye yönelik temel görüntü işleme tekniklerini kapsar.

- **Renk Uzayı Dönüşümleri (BGR, HSV, Gri Tonlama)**
  - Görüntüleri farklı renk formatları arasında dönüştürme ve her bir formatın kullanım amacını (örneğin renk tespiti için HSV) gösterir.
  - **Canlı Demo Önerisi:** `experiments/4_image_processing/04_color_spaces.py`

- **Görüntü Aritmetiği ve Bulanıklaştırma (Smoothing)**
  - İki resmi üst üste ekleme, harmanlama (blending) ve görüntüdeki gürültüyü azaltmak için kullanılan `blur`, `medianBlur` gibi filtreleme teknikleri.
  - **Canlı Demo Önerisi:** `experiments/4_image_processing/06_image_smoothing.py`

- **Eşikleme (Thresholding) ve Morfolojik Operasyonlar**
  - Bir görüntüyü siyah-beyaz formata dönüştürme ve `Erosion`, `Dilation` gibi operasyonlarla şekilleri temizleme veya belirginleştirme.
  - **Canlı Demo Önerisi:** `experiments/4_image_processing/09_morphological_ops.py`

---

## 3. İleri Seviye ve Uygulamalar

Bu bölüm, nesne tespiti, özellik çıkarma ve interaktif uygulamalar gibi daha karmaşık ve pratik konuları içerir.

- **Kontur Analizi (Alan, Ağırlık Merkezi, Dışbükey Örtü)**
  - Bir nesnenin dış hatlarını (konturlarını) bulma ve bu hatlar üzerinden alan, merkez noktası ve dışbükey örtü (convex hull) gibi geometrik özellikleri hesaplama.
  - **Canlı Demo Önerisi:** `experiments/5_feature_detection/09_contour_moments_and_centroid.py` (Merkez bulma)
  - **Canlı Demo Önerisi:** `experiments/5_feature_detection/11_convex_hull.py` (Dışbükey örtü)

- **Hough Dönüşümü ile Çizgi ve Daire Tespiti**
  - Görüntülerdeki parametrik şekilleri (çizgiler, daireler) matematiksel olarak tespit etme.
  - **Canlı Demo Önerisi:** `experiments/5_feature_detection/15_hough_circle_transform.py` (Daire bulma)

- **İnteraktif Arayüzler: Trackbar ile Renk Ayarlama**
  - Kullanıcının arayüzdeki ayar çubukları (trackbar) ile anlık olarak giriş yapmasını sağlama ve bu girdiye göre görüntüyü dinamik olarak değiştirme. Renk tespiti için kalibrasyon aracı olarak kullanılır.
  - **Canlı Demo Önerisi:** `experiments/2_drawing_and_interaction/05_trackbar_interaction.py`

- **Pratik Uygulama: Renk Tabanlı Nesne Tespiti (Video)**
  - Bir videodaki belirli bir renge sahip nesneleri, tüm adımları (HSV dönüşümü, maskeleme, `bitwise_and`) birleştirerek gerçek zamanlı olarak izole etme.
  - **Canlı Demo Önerisi:** `experiments/5_feature_detection/08_object_isolation_by_color.py`
