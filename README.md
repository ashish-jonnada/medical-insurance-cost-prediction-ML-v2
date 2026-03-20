# 🧠 Medical Insurance Cost Prediction (Improvement - v2)

![Python](https://img.shields.io/badge/Python-Data%20Science-blue)
![Project](https://img.shields.io/badge/Project-Machine%20Learning-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Intermediate-purple)
![Focus](https://img.shields.io/badge/Focus-Regression%20Model-yellow)

------------------------------------------------------------------------

## 👨‍💻 Author

**Ashish Jonnada**  
🎓 B.Tech CSE (AI & Data Science) — Marwadi University  

🔗 LinkedIn: [Ashish Jonnada](https://www.linkedin.com/in/jonnada-ashish)

------------------------------------------------------------------------

## 📌 Project Overview

This project is an improved version of a previously built **Medical Insurance Cost Prediction model**.

The main focus of this version is not just building a model, but **improving model performance and understanding the impact of different techniques**.

A **Multiple Linear Regression model** is used to predict insurance charges based on features such as age, BMI, smoking status, children, and region.

------------------------------------------------------------------------

## ⚠️ Problem Statement

In the previous version of this project, a Linear Regression model was developed to predict insurance charges.

Although the model performed well, there was a need to improve its accuracy and analyze which techniques actually help in improving performance.

This project focuses on refining the existing model and identifying meaningful improvements.

------------------------------------------------------------------------

## 🎯 Project Objectives

- Improve the performance of the existing model  
- Analyze the effect of different feature engineering techniques  
- Understand which changes improve performance and which do not  
- Evaluate the model using standard regression metrics  
- Identify the limitations of Linear Regression  

------------------------------------------------------------------------

## 🧠 Methodology

### 🔍 Data Understanding

- Explored dataset structure and feature types  
- Identified numerical and categorical features  
- Observed distribution of insurance charges  

### 🧹 Data Cleaning

- Removed duplicate records (~51% of dataset)  

👉 This significantly improved data quality  

### 🔄 Feature Encoding

- Converted categorical variables:
  - sex → binary  
  - smoker → binary  
  - region → one-hot encoding  

### 🛠 Feature Engineering

- Tried BMI category feature  
- Created interaction feature:
  - bmi × smoker  

## 🧩 Code Modularization (New Improvement)

In this version of the project, the workflow was improved by separating reusable logic into Python (.py) files.

- Model training logic was moved to ml_util.py
- Functions were created for better reusability and cleaner structure
- Notebook is used mainly for experimentation and visualization
- Improves code readability and maintainability  
- Makes the project scalable  
- Reflects real-world machine learning practices

------------------------------------------------------------------------

## 📈 Model Performance

| Metric | Value |
|------|------|
| R² Score | ~0.885 |
| MAE | ~2800 |
| RMSE | ~4500 |
 

------------------------------------------------------------------------

## 🧪 Key Experiments & Findings

### 1. BMI Category Feature
- Converting BMI into categories reduced performance  

👉 Continuous BMI gives better results  

---

### 2. Interaction Feature (bmi × smoker)
- Improved model performance  

👉 Smoking increases the impact of BMI on insurance cost  

---

------------------------------------------------------------------------

## 📊 Key Insights

- Smoking status has the highest impact on insurance charges  
- BMI plays a significant role, especially for smokers  
- Feature engineering should be meaningful, not random  
- Model performs well for normal cases but struggles with high charges  

------------------------------------------------------------------------

## 🏁 Conclusion

The Linear Regression model achieved an improved **R² score of ~0.885**, showing strong performance for this dataset.

The project highlights that:
- Proper feature engineering can improve performance  
- Not all transformations are useful  
- Model performance reaches a saturation point  

👉 This indicates the limitation of Linear Regression for complex patterns  

------------------------------------------------------------------------

## 🛠 Tools & Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Jupyter Notebook  
