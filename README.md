
# Brain Tumor Detection Using Machine Learning

## Overview

This project is a machine learning-based web application that detects the presence of brain tumors from MRI scan images. The system analyzes medical images and predicts whether a tumor is present using a trained classification model.

## Features

* MRI image upload
* Image preprocessing
* Brain tumor prediction
* Web-based user interface
* Fast and automated diagnosis support

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* NumPy
* OpenCV

## Dataset

The model was trained using a brain tumor MRI image dataset containing tumor and non-tumor brain scans. Images were preprocessed and converted into feature vectors before model training.

## Model

* Algorithm: Random Forest Classifier
* Model File: `brain_tumor_rf_model.pkl`
* Training Library: Scikit-learn

## Project Structure

```text
Tumor-detection-using-ML/
├── tumor dataset/
├── www/
├── brain_tumor_rf_model.pkl
├── server.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Mansiprabhu/Tumor-detection-using-ML.git
cd Tumor-detection-using-ML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python server.py
```

## Usage

1. Launch the application.
2. Upload an MRI scan image.
3. The image is processed by the trained model.
4. The prediction result is displayed.

## Screenshots

<img width="940" height="425" alt="image" src="https://github.com/user-attachments/assets/176a9fe2-fe54-4e9f-88fa-267132ec4bf1" />
<img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/61cec34b-fb5d-44e2-990a-7054a7ef522e" />
<img width="940" height="503" alt="image" src="https://github.com/user-attachments/assets/e4c9cb92-517a-4e23-b512-6d427f01dce5" />



## Future Improvements

* Deep learning-based classification using CNNs
* Multi-class tumor classification
* Improved prediction accuracy
* Cloud deployment

## Author

Mansi Prabhu
