# Yolo End-to-end practice

Bu proje, uçtan uca **Veri Mühendisliği (Data Engineering)** ve **YOLOv8** model eğitimi süreçlerini kapsar. Veri toplama, sentetik üretim, temizleme ve özel eğitim boru hatları (pipelines) aşağıda adım adım açıklanmıştır.

---

## Pipeline

### 1. Veri Kaynağı ve Sentetik Üretim
* **Kaynak:** Roboflow ve açık kaynaklardan ham drone görüntüleri toplandı.
> https://universe.roboflow.com/tarik-nskbt/red-2k-blue-2k-anotation-catisiz-eks9g
* **Problem:** Veri çeşitliliği ve zemin farkları (asfalt, çim, toprak) yetersizdi.
* **Çözüm (Sentetik Veri):** Google Colab üzerinde **Stable Diffusion XL** kullanılarak 100+ adet fotorealistik sentetik veri üretildi.
> https://github.com/CompVis/stable-diffusio
> https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
  * **İlgili Script:** `data/synthetic/generate_syn_data.py`
  * **Senaryolar:** `data/synthetic/prompts.json` içerisindeki promptlar kullanıldı.
```bash
python data/synthetic/generate_syn_data.py \
  --prompts_file "data/synthetic/prompts.json" \
  --output "data/dataset_synthetic" \
  --count 10
```

### 2. Veri Temizliği (Data Sanitization)
İndirilen verilerdeki hatalı etiketler ve karışık dosya isimleri temizlendi.
* **İşlem 1 (Etiket Silme):** Hatalı olan tüm `.txt` etiket dosyaları silindi.
```bash
python data/scripts/clean_labels.py 
    --dir "data/raw"
```
* **İşlem 2 (İsimlendirme):** Tüm dosyalar `drone_v1_0001.jpg` formatına çevrildi.
```bash
python data/scripts/standardize_names.py 
    --dir "data/raw" 
    --prefix "drone"
```

### 3. Etiketleme ve Zenginleştirme (Roboflow)
> https://app.roboflow.com/tritetra/red-blue-squares/1
Temizlenen **Orijinal** ve **Sentetik** veriler Roboflow'a yüklenerek toplam **1245 Görüntü** elde edildi.
* **Preprocessing (Ön İşleme):**
  * **Auto-Orient:** Uygulandı.
  * **Resize:** Tüm görüntüler **512x512** piksele (Stretch) boyutlandırıldı.
* **Augmentation (Veri Çoğaltma):** Modelin farklı açılara dayanıklı olması için her görüntüden **3 varyasyon** üretildi:
  * **Flip:** Horizontal (Yatay Çevirme).
  * **Rotation:** 90° Clockwise, Counter-Clockwise, Upside Down (Farklı açılardan drone bakışı simülasyonu).
  * **Crop:** %0 ile %20 arası rastgele yakınlaştırma (Zoom).

### 4. Lokal Veri Dağıtımı (Custom Split)
Roboflow'un otomatik dağıtımı yerine, bilimsel tutarlılık için veriler indirilip **lokalde** işlendi.
* **Algoritma:** Tüm veri birleştirildi, **Seed 42** ile karıştırıldı (Shuffle).
* **Split:** %70 Train, %20 Val, %10 Test olarak ayrıldı.
* **Konfigürasyon:** YOLO eğitimi için `data.yaml` otomatik oluşturuldu.
```bash
python data/scripts/prepare_dataset.py 
    --source "data/raw_download" 
    --dest "data/ready_dataset
```

### 5. Model Eğitimi (Training)
> https://docs.ultralytics.com/models/yolov8/#performance-metrics
> https://huggingface.co/Ultralytics/YOLOv8
> https://docs.ultralytics.com/usage/python/#export
> https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models
Hazırlanan veri seti `.zip` olarak Google Drive'a yüklendi.
* **Yöntem:** `train_from_drive.py` scripti veriyi Drive'dan çeker, `data.yaml` dosyasını bulur ve eğitimi başlatır.
* **Model:** YOLOv8 Nano ve Medium.
* **Strateji:** Overfitting'i önlemek için **300 Epoch** ve **Patience 50** (Erken Durdurma) kullanıldı.
```bash
    python models/training/train_from_drive.py 
        --model m
```

---

### Kurulum ve Çalıştırma

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```