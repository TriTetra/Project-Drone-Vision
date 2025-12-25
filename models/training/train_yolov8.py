import os 
import argparse
import gdown
import torch
import zipfile
import glob
from ultralytics import YOLO
from dotenv import load_dotenv

load_dotenv()

DEFAULT_EPOCHS = 300
DEFAULT_PATIENCE = 50
DEFAULT_IMG_SIZE = 640
DEFAULT_BATCH = 16

PROJECT_NAME = os.getenv("PROJECT_NAME")


def check_gpu():
    if torch.cuda.is_available():
        print(f"GPU Aktif: {torch.cuda.get_device_name(0)}")
    else:
        raise SystemError("GPU bulunamadı. Lütfen CUDA destekli bir GPU ile çalıştığınızdan emin olun.")
    

def download_and_extract_data(output_dir="data/dataset_local"):
    file_id= os.getenv("DRIVE_FILE_ID")

    if not file_id:
        raise ValueError("DRIVE_FILE_ID ortam değişkeni ayarlanmamış.")
    
    if os.path.exists(output_dir):
        existing_yaml=glob.glob(f"{output_dir}/*.yaml", recursive=True)
        if existing_yaml:
            print(f"Veri seti zaten mevcut: {output_dir}")
            return
        
    os.makedirs(output_dir, exist_ok=True)

    url = f"https://drive.google.com/uc?id={file_id}"
    zip_path = os.path.join(output_dir, "dataset.zip")

    try:
        gdown.download(url, zip_path, quiet=False, fuzzy=True)
    except Exception as e:
        if os.path.exists(zip_path):
            os.remove(zip_path)
            raise RuntimeError(f"Dosya indirme başarısız oldu ve kısmi dosya silindi: {e}")
        
    print(f"Veri seti indirildi: {zip_path}")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
    except zipfile.BadZipFile:
        print("HATA: Dosya zip değil veya bozuk indi.")
        os.remove(zip_path)
        raise

    os.remove(zip_path)
    print(f"Veri seti çıkarıldı: {output_dir}")
    return output_dir


def find_data_yaml(search_path):
    yaml_files = glob.glob(f"{search_path}/**/data.yaml", recursive=True)
    if not yaml_files:
        raise FileNotFoundError("data.yaml bulunamadı! Klasör yapısını kontrol et.")
    return yaml_files[0]


def train_yolo(yaml_path, model_type, epochs, batch, device):
    model_name = f"yolov8{model_type}.pt"
    print(f"\n Model: {model_name} | Epochs: {epochs}")
    
    model = YOLO(model_name)
    
    model.train(
        data=yaml_path,
        epochs=epochs,
        patience=DEFAULT_PATIENCE,
        imgsz=DEFAULT_IMG_SIZE,
        batch=batch,
        device=device,
        project=f"runs/{PROJECT_NAME}",
        name=f"train_drive_{model_type}",
        exist_ok=True,
        plots=True,
        verbose=True
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Drive + DotEnv Eğitim Aracı")
    # Artık ID'yi argüman olarak zorunlu tutmuyoruz, env'den çekecek
    parser.add_argument("--model", type=str, default="n", choices=['n', 'm', 's'], help="Model Tipi")
    parser.add_argument("--batch", type=int, default=DEFAULT_BATCH, help="Batch Size")
    
    args = parser.parse_args()
    device_id = check_gpu()
    
    try:
        # Parametre vermiyoruz, içeride env'den okuyacak
        dataset_folder = download_and_extract_data()
        yaml_file = find_data_yaml(dataset_folder)
        train_yolo(yaml_file, args.model, DEFAULT_EPOCHS, args.batch, device_id)
        
    except Exception as e:
        print(f"KRİTİK HATA: {e}")