🛡️ AI Fraud Shield – Credit Card Fraud Detection System

A Machine Learning powered web application that detects fraudulent credit card transactions in real-time using advanced classification models and imbalance handling techniques.

⸻

🌐 Live Demo

Deployed Website:
https://credit-card-fraud-detection-jwoj.onrender.com/

⸻

📌 Project Overview

This project detects fraudulent credit card transactions using Machine Learning techniques. Since fraud datasets are highly imbalanced (very few fraud cases compared to genuine transactions), special preprocessing techniques such as SMOTE (Synthetic Minority Oversampling Technique) are used to improve fraud detection performance.

The system predicts whether a transaction is:

✅ Legitimate Transaction
🚨 Fraudulent Transaction

The project also includes a professional Flask web interface for real-time predictions.

⸻

✨ Features

* 🔍 Real-time fraud prediction
* 🤖 Machine Learning-based classification
* ⚖️ Handles highly imbalanced data using SMOTE
* 🌐 Professional Flask web interface
* 📊 Model performance evaluation
* 💾 Saved trained model using Joblib
* 🚀 Deployable on Render

⸻

🛠️ Technologies Used

Programming Language

* Python

Libraries & Frameworks

* Flask
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Joblib

Data Visualization

* Matplotlib
* Seaborn

Deployment

* Render
* GitHub

⸻

📂 Dataset

Source: Kaggle Credit Card Fraud Dataset

Dataset Information

* Total Transactions: 284,807
* Fraudulent Transactions: 492
* Normal Transactions: 284,315
* Nature: Highly Imbalanced Dataset

The dataset contains anonymized transaction features named:

V1 – V28, Time, and Amount

⸻

🔍 Project Workflow

1️⃣ Data Collection & Loading

* Imported dataset
* Performed preprocessing and cleaning

2️⃣ Exploratory Data Analysis (EDA)

* Fraud vs Legitimate transaction analysis
* Correlation analysis
* Class imbalance visualization

3️⃣ Data Preprocessing

* Feature selection
* Train-Test Split
* Feature scaling (if applicable)

4️⃣ Handling Imbalanced Data

Used:

SMOTE (Synthetic Minority Oversampling Technique)

This helped improve model performance for minority fraud cases.

5️⃣ Model Training

Multiple machine learning models were trained:

Logistic Regression

* Simple baseline model
* Fast and interpretable

Random Forest Classifier

* Ensemble learning technique
* High accuracy and better fraud detection

Isolation Forest

* Anomaly detection approach
* Useful for outlier detection

6️⃣ Model Evaluation

Performance evaluated using:

* Accuracy Score
* Confusion Matrix
* Precision Score
* Recall Score
* F1 Score

7️⃣ Model Saving

Best performing model saved using: 
joblib.dump(model, "model.pkl")

8️⃣ Web Application Development

Built a Flask web app for real-time transaction fraud detection.

⸻

📊 Results

Model Performance Summary

✅ High prediction accuracy achieved

✅ Improved fraud detection using SMOTE

✅ Better recall for minority fraudulent transactions

🏆 Random Forest Classifier performed best overall

📁 Project Structure

Credit-Card-Fraud-Detection/
│── app.py
│── requirements.txt
│── Procfile
│── README.md
│
├── models/
│   └── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── Css/
│       └── style.css
│
├── Data/
│   └── creditcard.csv.zip
│
└── notebooks/

💾 How to Run Locally

1. Clone Repository
git clone https://github.com/Galav21/Credit-Card-Fraud-Detection.git

2. Move into Project Folder
cd Credit-Card-Fraud-Detection

3. Install Dependencies
pip install -r requirements.txt

4. Run Flask App
python app.py

5. Open in Browser
http://127.0.0.1:5000/

🚀 Deployment

This project is deployed using Render.

⸻

🎯 Future Improvements

* Deep Learning based fraud detection
* Real-time transaction API integration
* User authentication system
* Fraud analytics dashboard
* Cloud database integration

⸻

👨‍💻 Developer

Galav Bhatt

B.Tech – Artificial Intelligence & Data Science
