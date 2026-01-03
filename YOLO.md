# End-to-End YOLO Practice

This project covers the end-to-end processes of **Data Engineering** and **YOLOv8** model training. The data collection, synthetic generation, cleaning, and custom training pipelines are explained step-by-step below.

---

## Pipeline

### 1. Data Source and Synthetic Generation
*   **Source:** Raw drone images were collected from Roboflow and open-source repositories.
    > https://universe.roboflow.com/tarik-nskbt/red-2k-blue-2k-anotation-catisiz-eks9g
*   **Problem:** There was a lack of data diversity and variations in ground surfaces (asphalt, grass, dirt).
*   **Solution (Synthetic Data):** Over 100 photorealistic synthetic data points were generated using **Stable Diffusion XL** on Google Colab.
    > https://github.com/CompVis/stable-diffusion
    > https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
    *   **Relevant Script:** `data/synthetic/generate_syn_data.py`
    *   **Scenarios:** Prompts from `data/synthetic/prompts.json` were used.
    ```bash
    python data/synthetic/generate_syn_data.py \
      --prompts_file "data/synthetic/prompts.json" \
      --output "data/dataset_synthetic" \
      --count 10
    ```

### 2. Data Sanitization
Erroneous labels and inconsistent file names in the downloaded data were cleaned.
*   **Step 1 (Delete Labels):** All incorrect `.txt` label files were deleted.
    ```bash
    python data/scripts/clean_labels.py \
        --dir "data/raw"
    ```
*   **Step 2 (Standardize Naming):** All files were renamed to the `drone_v1_0001.jpg` format.
    ```bash
    python data/scripts/standardize_names.py \
        --dir "data/raw" \
        --prefix "drone"
    ```

### 3. Labeling and Enrichment (Roboflow)
> https://app.roboflow.com/tritetra/red-blue-squares/1
The cleaned **Original** and **Synthetic** data were uploaded to Roboflow, resulting in a total of **1245 Images**.
*   **Preprocessing:**
    *   **Auto-Orient:** Applied.
    *   **Resize:** All images were stretched to **512x512** pixels.
*   **Augmentation:** To make the model robust to different angles, **3 variations** were generated from each image:
    *   **Flip:** Horizontal.
    *   **Rotation:** 90° Clockwise, Counter-Clockwise, Upside Down (to simulate different drone perspectives).
    *   **Crop:** Random zoom between 0% and 20%.

### 4. Local Data Split (Custom Split)
Instead of using Roboflow's automatic distribution, the data was downloaded and processed **locally** for scientific consistency.
*   **Algorithm:** All data was merged and shuffled with **Seed 42**.
*   **Split:** The data was split into 70% Train, 20% Validation, and 10% Test sets.
*   **Configuration:** A `data.yaml` file was automatically generated for YOLO training.
    ```bash
    python data/scripts/prepare_dataset.py \
        --source "data/raw_download" \
        --dest "data/ready_dataset"
    ```

### 5. Model Training
> https://docs.ultralytics.com/models/yolov8/#performance-metrics
> https://huggingface.co/Ultralytics/YOLOv8
> https://docs.ultralytics.com/usage/python/#export
> https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models
The prepared dataset was uploaded to Google Drive as a `.zip` file.
*   **Method:** The `train_from_drive.py` script pulls the data from Drive, locates the `data.yaml` file, and starts the training.
*   **Model:** YOLOv8 Nano and Medium.
*   **Strategy:** To prevent overfitting, **300 Epochs** and **Patience 50** (Early Stopping) were used.
    ```bash
    python models/training/train_from_drive.py \
        --model m
    ```

---

### Setup and Execution

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```