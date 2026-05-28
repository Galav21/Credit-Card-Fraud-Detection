# Credit Card Fraud Detection System

## 📌 Project Overview
This project detects fraudulent credit card transactions using machine learning.
It handles highly imbalanced data and predicts whether a transaction is fraudulent or genuine.

## 🛠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib, Seaborn
- Joblib
- SQL (for analysis – optional extension)

## 📂 Dataset
- Source: Kaggle Credit Card Fraud Dataset
- Total Transactions: 284,807
- Fraudulent Transactions: 492

## 🔍 Approach
1. Data Loading & Cleaning
2. Exploratory Data Analysis
3. Train-Test Split
4. Handling Imbalanced Data using SMOTE
5. Model Training:
   - Logistic Regression
   - Random Forest
   - Isolation Forest
6. Model Evaluation using:
   - Confusion Matrix
   - Precision, Recall, F1-score
7. Model Saving using Joblib

## 📊 Results
- High accuracy achieved
- Improved recall for fraud detection using SMOTE
- Random Forest performed best overall

## 💾 How to Run
```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn joblib


