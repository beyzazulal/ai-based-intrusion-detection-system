# AI-Based Intrusion Detection System (IDS)

<img width="1920" height="1080" alt="Ekran Görüntüsü (5588)" src="https://github.com/user-attachments/assets/a72ef64f-b5db-440b-a9a0-962aec6f3c87" />


## 📌 Overview

This project is an AI-powered Intrusion Detection System that detects network attacks using machine learning models trained on CICIDS2017 dataset.

## 🚀 Features

* Real-time attack detection
* Flask REST API
* XGBoost machine learning model
* MongoDB feedback storage
* Model retraining support

## 🧠 Technologies

* Python
* Flask
* XGBoost
* MongoDB
* Scikit-learn
* Pandas

## 🔌 API Endpoints

* `/predict` → Predict if traffic is attack or benign
* `/feedback` → Store user feedback
* `/health` → Check API status

## ⚙️ Run Locally

```bash
python app.py
```

## 📊 Model

Trained using CICIDS2017 dataset with feature engineering and class balancing (SMOTE).

## 📁 Structure

* app.py → API server
* test_api.py → Prediction test
* test_feedback.py → Feedback test
* Mongo scripts → Data handling

## 📌 Note

Model file (.pkl) is not included due to size limitations.

<img width="1912" height="967" alt="Ekran görüntüsü 2026-04-22 162537" src="https://github.com/user-attachments/assets/646fff5e-be4f-40a1-8445-1b136abed428" />

<img width="1920" height="917" alt="Ekran görüntüsü 2026-04-22 162724" src="https://github.com/user-attachments/assets/ab7aa3a8-97be-46ee-a084-b3715e542f5d" />



