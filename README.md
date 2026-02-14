# 🚓 Crime Analysis and Prediction using Machine Learning

A data-driven machine learning project that analyzes crime patterns across Indian cities and predicts whether a crime is **violent or non-violent** using historical crime data.

This system helps identify crime hotspots, understand temporal trends, and support data-driven decision making for law enforcement and policy planning.

---

## 📌 Project Overview

Crime analysis plays a critical role in public safety and strategic policing. This project leverages **data analytics and machine learning** to:

- Analyze crime patterns across cities and time.
- Detect crime hotspots.
- Study demographic and temporal trends.
- Predict crime category (violent vs non-violent).
- Provide insights for better resource allocation and preventive action.

The project combines **Exploratory Data Analysis (EDA)** and **Random Forest based prediction** to generate actionable insights.

---

## 🎯 Objectives

- Identify crime hotspots across cities.
- Analyze crime distribution across time.
- Study victim demographics and crime characteristics.
- Build a predictive ML model for crime classification.
- Provide data-driven policy recommendations.

---

## 🛠️ Tech Stack

### Programming Language
- Python 3

### Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

### Machine Learning
- Random Forest Classifier
- Label Encoding
- Train-Test Split
- Model Evaluation Metrics

---

## 📊 Dataset Description

Dataset: `crime_dataset_india.csv`

Main features used:

| Column | Description |
|---------|-------------|
| Date of Occurrence | Crime date |
| Time of Occurrence | Crime time |
| Crime Domain | Crime category |
| Crime Description | Specific crime type |
| Victim Age | Age of victim |
| Victim Gender | Gender of victim |
| Weapon Used | Weapon involved |
| Police Deployed | Police units assigned |
| Case Closed | Case status |
| City | Crime location |

---

## ⚙️ System Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Exploratory Data Analysis
5. Model Training
6. Model Testing
7. Prediction & Visualization
8. Policy Recommendations

---

## 🔍 Key Analyses Performed

✔ City-wise crime hotspots  
✔ Monthly and hourly crime trends  
✔ Victim demographic patterns  
✔ Crime domain distribution  
✔ Feature correlation analysis  
✔ Violent vs Non-violent classification  

---

## 🤖 Machine Learning Model

We used **Random Forest Classifier** due to:

- High accuracy
- Robustness
- Feature importance extraction
- Reduced overfitting risk

### Important Features for Prediction
- City
- Crime Description
- Hour of occurrence
- Police deployed
- Weapon used

---

## 📈 Results

- Reliable classification of violent vs non-violent crimes.
- Identification of crime peak hours.
- Detection of major crime hotspots.
- Feature importance insights for policy planning.

---

## 🖥️ Application Features

- Crime distribution dashboards
- Interactive hotspot visualization
- Crime prediction interface
- Risk assessment visualization
- Resource allocation insights

---

## 🚀 Future Improvements

- Real-time crime data integration
- Deep learning models
- Multi-class crime prediction
- Mobile/web application deployment
- Integration with surveillance systems
- Advanced spatio-temporal forecasting

---

## Project Folder Structure

```Crime-Analysis-And-Prediction/
│
├─ backend/
│ └─ app.py
│
├─ frontend/
│ ├─ components/
│ │ ├─ init.py
│ │ ├─ alerts_panel.py
│ │ ├─ charts_section.py
│ │ ├─ dashboard.py
│ │ ├─ data_upload_page.py
│ │ ├─ footer.py
│ │ ├─ header.py
│ │ └─ metric_card.py
│ └─ assets/
│ └─ theme.js
│
└─ maincode.ipynb```

