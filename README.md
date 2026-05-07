#  Multi-State Sales Forecasting System

End-to-End Time Series Forecasting Platform using XGBoost, Prophet, SARIMA and LSTM with Automatic Model Selection, REST API and Interactive Dashboard.

---

#  Project Overview

Businesses often struggle to accurately forecast future sales across different regions due to:
- changing seasonal patterns
- trend variations
- missing historical records
- different state-level behaviors

This project builds a production-style forecasting system capable of:

✅ Forecasting next 8 weeks of sales for each state  
✅ Training multiple forecasting algorithms  
✅ Automatically selecting the best-performing model per state  
✅ Serving forecasts through REST APIs  
✅ Visualizing predictions using an interactive dashboard  

The system was designed as a scalable ML backend service with deployment-ready architecture.

---

#  Dataset

The dataset contains weekly sales data across 43 states from 2019 to 2023.

Dataset characteristics:
- Multi-state sales history
- Weekly granularity
- Missing periods in historical timeline
- State-level seasonality and trend behavior

---

#  Problem Statement

Forecast the next 8 weeks of sales for each state using historical sales data.

The system must:
- Handle missing dates and missing values
- Capture seasonality and trend
- Compare multiple forecasting algorithms
- Automatically select the best-performing model
- Serve predictions using API
- Provide dashboard visualization

---

#  Project Pipeline

- Data Understanding and Cleaning
- Missing Timeline Reconstruction
- Missing Value Imputation
- Feature Engineering
- Time-Series Train/Validation Split
- Multi-Model Forecasting
- Automatic Model Selection
- Future Forecast Generation
- API Development
- Interactive Dashboard Deployment

---

#  Feature Engineering

The following forecasting features were created:

## Lag Features
- lag_1
- lag_7
- lag_30

## Rolling Statistics
- rolling_mean_4
- rolling_std_4

## Calendar Features
- day_of_week
- month
- quarter
- week_of_year
- year

## Holiday Features
US holiday flags generated using the `holidays` library.

## Cyclical Encoding
- month_sin
- month_cos

---

#  Forecasting Models

The system trains and compares four forecasting models.

## 1️⃣ XGBoost
Gradient boosting regression using engineered lag features.

## 2️⃣ Prophet
Captures trend and seasonality decomposition.

## 3️⃣ SARIMA
Statistical time-series forecasting model.

## 4️⃣ LSTM
Deep learning recurrent neural network for sequential forecasting.

---

#  Automatic Model Selection

Instead of assuming one model works best globally, the system:

- trains all forecasting models independently for each state
- evaluates each model using RMSE and MAE
- automatically selects the best-performing model per state

This creates a dynamic production-style forecasting engine.

---

#  Evaluation Metrics

Models were evaluated using:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

Lower values indicate better forecasting performance.

---

#  Interactive Dashboard

The dashboard allows users to:
- Select states dynamically
- View 8-week forecasts
- Compare forecasting models
- Visualize forecast trends
- Inspect RMSE comparison charts

---

#  Live Dashboard

Render Deployment:

https://multi-state-sales-forecasting-system.onrender.com/

---

#  Demo Video

A locally recorded walkthrough demonstrating:
- dashboard functionality
- state-wise forecasting
- dynamic model selection
- interactive visualizations

will be added shortly.

---

# ⚡ FastAPI Endpoints

## Available States

```bash
GET /states
```

## Forecast Endpoint

```bash
GET /forecast/{state}
```

## Best Model Endpoint

```bash
GET /best-model/{state}
```

## Metrics Endpoint

```bash
GET /metrics/{state}
```

---

#  System Architecture

```text
User → Streamlit Dashboard → Forecast Registry → Prediction Response
```

---

#  Deployment

The project was containerized using Docker and deployed using Render.

## Deployment Stack

- Docker
- Streamlit
- FastAPI
- Render

---

#  Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Prophet
- Statsmodels
- TensorFlow / Keras
- Streamlit
- FastAPI
- Plotly
- Joblib
- Docker
- Render

---

#  Project Structure

```text
forecasting-system/
│
├── app.py
├── dashboard.py
│
├── forecast_registry.pkl
├── best_model_registry.pkl
├── metrics_registry.pkl
│
├── Dockerfile
├── requirements.txt
├── README.md
└── notebooks/
```

---

#  Key Learnings

- Building end-to-end forecasting pipelines
- Handling time-series leakage
- Forecast feature engineering
- Multi-model evaluation systems
- Recursive forecasting
- API deployment for ML systems
- Dashboard deployment and visualization
- Docker containerization

---

#  Future Improvements

- Add retraining endpoint
- Implement MLflow experiment tracking
- Add distributed forecasting pipeline
- Integrate cloud object storage
- Add ensemble forecasting
- Improve deployment optimization

---

# Author

Swati Yadav  
Machine Learning and Data Science Enthusiast

GitHub:  
https://github.com/swati666
