Brain Tumor Detection Using Machine Learning
Overview

This project is a machine learning-based web application that detects the presence of brain tumors from MRI scan images. The system analyzes medical images and predicts whether a tumor is present using a trained classification model.

Features
MRI image upload
Image preprocessing
Brain tumor prediction
Web-based user interface
Fast and automated diagnosis support
Tech Stack
Frontend
HTML
CSS
JavaScript
Backend
Python
Flask
Machine Learning
Scikit-learn
NumPy
OpenCV
Dataset

The model was trained using a brain tumor MRI image dataset containing tumor and non-tumor brain scans. Images were preprocessed and converted into feature vectors before model training.

Model
Algorithm: Random Forest Classifier
Model File: brain_tumor_rf_model.pkl
Training Library: Scikit-learn
Project Structure
Tumor-detection-using-ML/
├── tumor dataset/
├── www/
├── brain_tumor_rf_model.pkl
├── server.py
└── README.md
Installation

Clone the repository:

git clone https://github.com/Mansiprabhu/Tumor-detection-using-ML.git
cd Tumor-detection-using-ML

Install dependencies:

pip install -r requirements.txt

Run the application:

python server.py
Usage
Launch the application.
Upload an MRI scan image.
The image is processed by the trained model.
The prediction result is displayed.
Screenshots

Add screenshots of the application interface and prediction results here.

Future Improvements
Deep learning-based classification using CNNs
Multi-class tumor classification
Improved prediction accuracy
Cloud deployment
Author

Mansi Prabhu
