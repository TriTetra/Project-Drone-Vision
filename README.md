# Drone Vision Project

Welcome to the Drone Vision Project! This repository contains a collection of resources, experiments, and a complete end-to-end pipeline for training object detection models with YOLOv8.

## Project Structure

This repository is organized into several key modules, each serving a specific purpose in the drone vision pipeline and learning journey.

```
.
├── data/                    # Data handling: scripts for synthetic data generation, cleaning, and dataset preparation
├── experiments/             # OpenCV learning hub: tutorials, code examples, and interactive scripts
│   ├── _assets/             # Images/videos used in experiments
│   └── ...
├── models/                  # Model development: YOLOv8 training scripts, model weights, and related notebooks
│   ├── notebooks/           # Notebooks for model-related experiments
│   ├── training/            # Scripts for model training
│   └── weights/             # Directory for trained model weights
├── Slides/                  # Project presentations and related materials
├── .gitignore               # Files/directories to be ignored by Git
├── Opencv.md                # Detailed documentation for OpenCV experiments
├── README.md                # Project overview and navigation (this file)
├── requirements.txt         # Python dependencies
└── YOLO.md                  # Detailed documentation for the YOLOv8 pipeline
```

-   **`data/`**: Contains scripts and configurations related to data engineering. This includes generating synthetic data, cleaning raw datasets, and preparing data for model training.
-   **`experiments/`**: A comprehensive collection of OpenCV tutorials and examples, organized by topic. This module serves as a learning hub for various computer vision techniques.
-   **`models/`**: Houses everything related to the YOLOv8 object detection model, from training scripts to pre-trained weights and evaluation notebooks.
-   **`Slides/`**: This directory is designated for project presentations, reports, and any other related static materials. You can upload your presentations here.
-   **`Opencv.md`**: Detailed documentation and guides for working with the OpenCV experiments.
-   **`YOLO.md`**: In-depth documentation covering the end-to-end YOLOv8 model training pipeline.

## Modules

This project is divided into two main parts:

1.  **OpenCV Experiments**: A comprehensive set of tutorials and code examples for learning and experimenting with OpenCV. This is a great place to start if you are new to computer vision or want to explore specific techniques.
    *   [**Go to OpenCV Documentation**](./Opencv.md)

2.  **YOLOv8 End-to-End Pipeline**: A complete, step-by-step guide and implementation for training a YOLOv8 model on a custom dataset. This includes data collection, synthetic data generation, data cleaning, labeling, and model training.
    *   [**Go to YOLOv8 Documentation**](./YOLO.md)

## External Resources

This section is for linking to external project-related materials, such as online notebooks or hosted presentations.

### Presentations

Project presentations and reports can be found in the [`Slides/`](./Slides) directory.

### Google NotebookLM

* [Vefa Project: YOLOv8 Data Preparation Pipeline](https://notebooklm.google.com/notebook/81caf2bc-23a2-46db-bc51-2dcdaef4b95a)
* [Python Computer Vision with OpenCV: Fundamentals and Implementation](https://notebooklm.google.com/notebook/0d00a043-a614-41a4-88ad-0784edcd0132)
* [YOLO Ultralytics: End-to-end](https://notebooklm.google.com/notebook/574f8d45-f209-4779-bde0-aefcb76c8a6c)

## Getting Started

To get started with the project, you can explore the directories and documentation linked above.

### Installation

If you want to run the code, you'll need to set up a Python virtual environment and install the required packages.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
