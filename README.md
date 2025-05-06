# Intrusion Detection System (IDS) using Machine Learning

This project implements a machine learning-based IDS to detect malicious activity in network traffic using the NSL-KDD dataset.

## 🚀 Features
- Supervised learning model (Random Forest)
- Trained on NSL-KDD dataset
- Predicts normal vs attack traffic
- Saves trained model for future use

## 📁 Project Structure
```
ids-ml/
├── data/                 # Contains NSL-KDD dataset
├── model/                # Trained model stored here
├── train_model.py        # For training the IDS model
├── ids.py                # Predict new samples
├── requirements.txt
└── README.md
```

## 📦 Requirements
```bash
pip install pandas numpy scikit-learn joblib
```

## 🧠 Train the Model
```bash
python train_model.py
```

## 🔍 Predict
```bash
python ids.py
```

## 📚 Dataset
[NSL-KDD Dataset](https://www.kaggle.com/datasets/hassan06/nslkdd)

## 📌 Author
Krupal Savaliya
