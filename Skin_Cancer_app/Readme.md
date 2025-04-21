#                                              Skin Cancer Prediction System 

## Introduction:

Skin cancer is one of the most common forms of cancer globally. Early detection is crucial for effective
treatment and improving patient survival rates. In this project, we developed a Skin Cancer Prediction System
using Machine Learning (ML) for prediction and Flask for a user-friendly web interface.

---

## Objectives:

- Detect the presence of skin cancer from dermoscopic images.
- Classify images into different types (e.g., melanoma, nevus, etc.).
- Develop a web-based interface for users to upload skin lesion images and get predictions.
- Assist dermatologists and patients with early screening.

---

## Dataset Description:

We used the HAM10000 ("Human Against Machine with 10000 training images") dataset available on
Kaggle.
Diagnosis Categories:
- mel: Melanoma
- nv: Melanocytic nevus
- bkl: Benign keratosis
- bcc: Basal cell carcinoma
- akiec: Actinic keratoses
- vasc: Vascular lesions
- df: Dermatofibroma

---

## Data Preprocessing

Steps:
- Loaded image files and metadata CSV.
- Merged metadata with image data using image_id.

Skin Cancer Prediction System - Project Report
- Handled missing values.
- Performed label encoding on categorical variables (dx, sex, localization).
- Resized all images to 64x64 pixels.
- Normalized image pixel values.
- Split dataset into training (80%) and testing (20%) sets.
Model Building

Algorithms Tried:
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- CNN (for image data, using Keras/TensorFlow)
  
CNN Architecture:
Conv2D -> MaxPooling2D -> Conv2D -> MaxPooling2D -> Flatten -> Dense -> Dropout -> Dense (softmax)
Compiled with Adam optimizer and categorical_crossentropy loss.
Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix
  
Example Results:
- Logistic Regression: 71% Accuracy
- SVM: 75% Accuracy
- CNN: 88% Accuracy

---

## Flask Web Application

Features:
- Upload image functionality
- Backend calls the ML model and returns predictions
- Displays prediction and probability
  
Folder Structure:
- static/uploads/
- templates/index.html
- model/skin_model.h5
- app.py
- requirements.txt
  
Frontend (User Interface)
Features:
- Upload Button
- Display Prediction Result

---

## Conclusion:

This project demonstrates how machine learning and deep learning can help in the early diagnosis of skin
cancer. The model achieved an accuracy of around 88% with a CNN architecture and was deployed via a
Flask web app for real-time prediction.

---

## Future Enhancements:

Skin Cancer Prediction System - Project Report
- Deploy using cloud services
- Add patient history analysis
- Enhance UI/UX
- Improve classification using ensemble models
- Include mobile app integration

---

## References
- HAM10000 Dataset - Kaggle
- TensorFlow/Keras Documentation
- Flask Documentation
- Scikit-learn

