### GİRİŞ BÖLÜMÜ
**Slayt 1: Kapak** "Herkese merhaba. Bugün sizlerle bilgisayarlı görünün en temel yapı taşı olan OpenCV kütüphanesini ve Python ile görüntü işlemenin kritik adımlarını inceleyeceğiz. Hazırsanız başlayalım."
<br>

**Slayt 2: Bilgisayarlı Görü İş Akışı** "Bir görüntü işleme projesine başladığınızda aslında 4 temel aşamadan geçersiniz.
1. **Veri Girişi**: Önce görüntüyü veya videoyu sisteme alırız.
2. **Ön İşleme**: Gürültüleri temizleyip veriyi analize hazırlarız.
3. **Özellik Çıkarımı**: Kenar, köşe gibi anlamlı yapıları matematiksel olarak buluruz.
4. **Analiz ve Karar**: Son olarak da 'bu bir insandır' veya 'bu bir araçtır' gibi kararı veririz."
<br>

**Slayt 3: Kritik Fonksiyonlar Tablosu** "Burada OpenCV'nin en sık kullanılan fonksiyonlarını ve neden kullandığımızı bir tabloyla özetledim. Örneğin; `cv.cvtColor` fonksiyonunu ön işlemede veri boyutunu düşürmek için kullanırken , `cv.Canny` fonksiyonunu nesne sınırlarını en hassas şekilde bulmak, yani özellik çıkarımı için kullanıyoruz. Bu tablo, sunum boyunca göreceğimiz fonksiyonların bir özeti niteliğinde."

**Slayt 4: OpenCV Mimari Akış Şeması** "Az önce bahsettiğimiz adımları bir boru hattı (``pipeline``) olarak düşünün. Soldan 'Giriş' ile başlıyoruz (``imread``), ardından 'Ön İşleme'de griye çevirme veya bulanıklaştırma yapıyoruz. Daha sonra 'Segmentasyon' ile nesneyi arka plandan ayırıp, 'Özellik Çıkarımı' ile sınırlarını çiziyoruz. Sonuçta sistem bir karar veriyor. Her aşamanın çıktısı, bir sonrakinin girdisi oluyor."
<br>

**Slayt 5: Endüstriyel Uygulama (Otonom Araçlar)** "Peki bu teori gerçek hayatta nerede? En iyi örnek: Otonom Araçlar.
1. Araç kameradan saniyede 60 kare görüntüyü alır.
2. Yağmurlu havaysa gürültüyü temizler (Ön İşleme).
3. Yol çizgilerini ve kaldırımları birbirinden ayırır (Segmentasyon).
4. Son olarak, şerit eğimine bakıp direksiyonu ne kadar çevireceğine karar verir."

---
### TEMEL İŞLEMLER VE MATEMATİK

**Slayt 6: GUI Özellikleri** "Kodlamaya giriş yapalım. Ekranda gördüğünüz 3 fonksiyon bizim elimiz ayağımızdır.

``cv.imread`` görüntüyü diskten alıp bir sayı matrisine dönüştürür. ``cv.imshow`` bunu ekranda pencere olarak açar. ``cv.putText`` ise görselin üzerine, burada gördüğünüz koordinat mantığıyla yazı yazmamızı sağlar."
<br>

**Slayt 7: Temel İşlemler (Core Operations)** "Görüntülerin matris olduğunu söylemiştim, yani onları matematiksel olarak toplayabiliriz. Buradaki ``cv.addWeighted`` fonksiyonu, iki resmi belirli oranlarda (örneğin %70'e %30) şeffaflık vererek üst üste bindirmemizi, yani harmanlamamızı sağlar."
<br>

**Slayt 8: Maskeleme ve Bitwise İşlemleri** "Görüntü işlemenin en kritik mantığına geldik: Mantıksal Kapılar. Bir resmin sadece belirli bir bölgesini almak istiyorsak '``Bitwise AND``' kullanırız; bu işlem maskenin beyaz olduğu yerleri korur, siyah yerleri siler. Tam tersini yapmak için, yani maskeyi çevirmek içinse '``Bitwise NOT``' kullanıyoruz."
<br>

**Slayt 9: Threshold'dan Maskeye (Segmentasyon)** "Peki bu maskeyi nasıl oluşturuyoruz? İşte reçetemiz:
1. Önce ``threshold`` ile resmi siyah-beyaz yapıp nesne sınırlarını belirliyoruz.
2. Bu siyah-beyaz görüntü artık bizim maskemiz oluyor.
3. Son olarak az önce öğrendiğimiz ``bitwise_and`` ile bu maskeyi orijinal resme uygulayıp nesneyi arka plandan tamamen koparıyoruz.
<br>


**Slayt 10: Renk Uzayları ve Eşikleme** "Renk uzaylarını değiştirmek bize hız kazandırır. Renkli (BGR) bir resmi Gri (GRAY) tona çevirmek işlem yükünü 3 kat azaltır. Eğer renk takibi yapacaksak, ışık değişimlerinden etkilenmemek için HSV formatına geçeriz. Eşikleme yaparken de eğer ışık her yerde aynı değilse, sabit bir eşik yerine ``Adaptive Threshold`` kullanmak daha sağlıklı sonuç verir.
<br>

**Slayt 11: Kernel ve Konvolüsyon** "Bu işin matematiksel kalbi burası: Kernel. Kernel dediğimiz şey, resim üzerinde kaydırdığımız küçük bir penceredir (matristir). Bu pencereyi her kaydırdığımızda, alttaki piksellerle çarpıp toplayarak yeni bir değer üretiriz. Buna 'Konvolüsyon' denir. Bulanıklaştırma veya kenar bulma işlemleri tamamen bu matematiksel işlemle yapılır."
<br>

**Slayt 12: Yumuşatma Metotları (Tablo)** "Gürültü gidermek için farklı yöntemlerimiz var ve hangisini seçeceğimiz amaca bağlı. Eğer çok hızlı sonuç istiyorsak 'Averaging' veya 'Gaussian' kullanırız. Ama resimde tuz-biber gibi noktacıklar varsa 'Median' en iyisidir. Hem gürültü gitsin hem kenarlar keskin kalsın diyorsak 'Bilateral' filtre kullanırız, ancak bu biraz daha yavaştır."

---

### ÖZELLİK ÇIKARIMI

**Slayt 13: Sobel Operatörü** "Nesneleri tanımak için kenarları bulmamız gerekir. Kenar aslında piksel değerinin aniden değiştiği yerdir. Sobel operatörü bu değişimi, yani türevi hesaplar. X yönündeki Sobel dikey çizgileri, Y yönündeki Sobel yatay çizgileri bulmamızı sağlar."
<br>

**Slayt 14: Canny Kenar Algılama** "Sobel temeldir, ama ``cv.Canny`` bu işin profesyonelidir. Çünkü Canny algoritması gürültüyü temizler, gradyanı hesaplar ve kopuk çizgileri birleştirir. Parametre olarak verdiğimiz alt ve üst eşik değerleri (threshold1, threshold2) ile kenar hassasiyetini ayarlarız."
<br>

**Slayt 15: Morfolojik İşlemler** "Kenarları bulduk ama bazen gürültü kalabilir veya çizgiler kopuk olabilir. 'Erozyon' ile nesne sınırlarını aşındırıp gürültüyü yok ederiz. 'Genişletme' (Dilation) ile de nesneyi kalınlaştırıp kopuk parçaları birleştiririz."
<br>

**Slayt 16: Kontur Analizi** "Kenarlar birleşip kapalı bir şekil oluşturduğunda buna 'Kontur' diyoruz.
``cv.findContours`` fonksiyonu bize resimdeki tüm bağımsız nesnelerin sınırlarını verir. Bu sayede nesneleri sayabilir veya ``contourArea`` ile alanlarını hesaplayabiliriz."
<br>

**Slayt 17: Kenar Algılama Karşılaştırması** "Özetle, hangi yöntemi ne zaman kullanmalıyız? Basitçe yön bulmak istiyorsak Sobel. Hızlıca keskin kenar bulmak istiyorsak Laplacian. Ama en temiz, en güvenilir nesne sınırı istiyorsak mutlaka Canny kullanmalıyız çünkü içinde gürültü temizleme özelliği de var."
<br>

**Slayt 18: Konturlar Örneği** "Burada kontur bulmanın görsel bir örneğini görüyorsunuz. Madeni paraların veya hapların sınırları ``findContours`` ile tespit edilmiş ve ``drawContours`` ile yeşil renkte çizilmiş. Ayrıca hiyerarşi özelliği sayesinde iç içe geçmiş şekilleri de ayırt edebiliriz."`

---

### VİDEO VE NESNE ANALİZİ

**Slayt 19: Arka Plan Çıkarma** "Şimdi videolara geçelim. Hareketli bir nesneyi (örneğin yürüyen bir insanı) tespit etmenin en kolay yolu arka planı çıkarmaktır.

``MOG2`` algoritması, gölgeleri de algılayabildiği için ışık değişimlerinde çok başarılıdır. Sabit arka planı çıkarır, geriye sadece hareketli maske kalır."
<br>

**Slayt 20: Optik Akış (Optical Flow)** "Hareketin sadece varlığını değil, yönünü de merak ediyorsak Optik Akış kullanırız. Lucas-Kanade yöntemi (Sparse) sadece belirgin noktaları takip eder. Farneback yöntemi (Dense) ise ekrandaki her pikselin nereye gittiğini hesaplar, bu yüzden daha detaylıdır ama işlemciyi daha çok yorar."
<br>

**Slayt 21: Özellik Algılama (Feature Detection)** "Bir nesneyi (mesela bir logoyu) farklı açılardan da tanımak istiyorsak 'Keypoint' (Anahtar Nokta) algoritmaları gerekir. **SIFT** çok başarılıdır ama yavaştır. Bizim favorimiz **ORB** algoritmasıdır; çünkü hem çok hızlıdır, hem ücretsizdir hem de mobil cihazlarda bile rahatlıkla çalışır."
<br>

**Slayt 22: Nesne Algılama (Yüz Tespiti)** "Ve geldik en popüler konuya: Yüz Tespiti. Burada kullandığımız yöntem Haar Cascade. Makine öğrenmesi tabanlıdır; önceden eğitilmiş binlerce pozitif ve negatif görüntüden öğrenilen bir XML dosyasını kullanır. ``detectMultiScale`` fonksiyonu ile resimdeki yüzleri farklı boyutlarda olsa bile yakalarız."
<br>

**Slayt 23: Video Analizi Derinlemesine Bakış** "Son olarak video analiz yöntemlerini kıyaslayalım. Hız istiyorsak Lucas-Kanade veya MOG2 tercih ederiz. Daha detaylı analiz ve tüm sahnenin hareket haritasını çıkarmak istiyorsak Farneback kullanırız. Gerçek zamanlı sistemlerde gölge yönetimi olduğu için MOG2 genellikle standart tercihimizdir."

---

### KAPANIŞ

**Slayt 24: Sonuç** "Toparlamak gerekirse; OpenCV, endüstri standardı bir kütüphanedir. Python entegrasyonu sayesinde çok karmaşık algoritmaları burada gördüğünüz gibi birkaç satırla hayata geçirebiliriz. Bugün attığımız bu temel, otonom araçlardan güvenlik sistemlerine kadar uzanan bir yolun başlangıcıdır."
<br>

**Slayt 25: Kaynakça** "Daha detaylı bilgi ve dökümantasyon için buradaki linkleri inceleyebilirsiniz. Dinlediğiniz için teşekkür ederim."
