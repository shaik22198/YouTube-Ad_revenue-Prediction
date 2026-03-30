# 🎥 YouTube Ad Revenue Predictor

A Machine Learning-powered web application built using **Streamlit** that predicts estimated YouTube ad revenue based on video performance metrics such as views, likes, comments, watch time, and more.

---

## 🚀 Project Overview

This project aims to predict **YouTube Ad Revenue (USD)** using various features related to video performance and audience engagement.

The application allows users to input video-related metrics and instantly get a revenue prediction using a trained ML model.

---

## 🧠 Machine Learning Workflow

The project follows a complete ML pipeline:

1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Building  
5. Model Evaluation  
6. Deployment using Streamlit  

---

## 📊 Features Used

### 🔢 Numerical Features
- Views  
- Likes  
- Comments  
- Watch Time (minutes)  
- Video Length (minutes)  
- Subscribers  

### 🏷️ Categorical Features
- Category (Entertainment, Gaming, Education, Music, Tech, Lifestyle)  
- Device (Mobile, Desktop, Tablet, TV)  
- Country (IN, US, UK, CA, DE, AU)  

---

## 🤖 Models Used

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- XGBoost Regressor  

✅ Final model (Linear Regression) is saved using **joblib** and deployed in the app.

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  
- Streamlit  

---

## 🌐 Streamlit App Features

- User-friendly UI for input  
- Real-time prediction  
- Handles missing values dynamically  
- Displays feature impact insights  

---

## 📈 Model Insights

### 🔹 Numerical Features Impact

| Feature | Impact on Ad Revenue |
|--------|--------------------|
| Likes | +0.017 USD |
| Comments | +0.017 USD |
| Views | +0.0066 USD |
| Watch Time | +0.0047 USD |
| Video Length | +0.0031 USD |
| Subscribers | +9.11e-08 USD |

---

### 🔹 Category Impact (Compared to Education)

| Category | Impact |
|---------|--------|
| Tech | +0.053 USD |
| Lifestyle | +0.018 USD |
| Entertainment | -0.023 USD |
| Music | -0.092 USD |
| Gaming | -0.101 USD |

---

### 🔹 Device Impact (Compared to Desktop)

| Device | Impact |
|--------|--------|
| Mobile | -0.063 USD |
| Tablet | -0.087 USD |
| TV | -0.235 USD |

---

### 🔹 Country Impact (Compared to Australia)

| Country | Impact |
|---------|--------|
| India | +0.038 USD |
| Canada | -0.031 USD |
| UK | -0.075 USD |
| US | -0.093 USD |
| Germany | -0.132 USD |

---

## ▶️ How to Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/shaik22198/youtube-ad-revenue-predictor.git
cd youtube-ad-revenue-predictor
