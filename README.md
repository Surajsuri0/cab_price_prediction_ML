# Cab Price Prediction

**Short description:**  
A Flask web application that predicts taxi / ride-hailing prices (Uber, Lyft) using a trained machine learning model. The UI allows users to enter ride details (distance, cab type, source/destination, timestamp, surge multiplier) and see a predicted fare instantly.

## Project Overview
This project demonstrates a full ML workflow: data exploration and preprocessing, feature engineering, model training and evaluation, and deployment via a Flask app. The goal is to provide accurate fare estimates and an easy-to-use demo interface for stakeholders.

**Key features**
- Predicts ride price given distance, cab type, source/destination, timestamp and surge.
- Simple, responsive HTML frontend (Flask `templates/index.html`).
- Model saved as `cab_price_model.pkl` (downloadable from the release / Drive link).
- Example notebook with EDA and model training (`Machine Learning Project.ipynb`).
- Lightweight backend ready for local hosting or simple deployment (ngrok / cloud).

**Why this is useful**
- Helps drivers and riders estimate fares and plan trips.
- Useful for product demos, academic projects, and learning ML deployment.
- The pipeline (from EDA to deployment) is a repeatable template for similar regression problems.

**Quick stats**  
- Model: RandomForest / XGBoost (trained on historic rides)  
- Example performance: RMSE = `1.63`, R² = `0.969`  

---
## Dataset

The dataset used for training and evaluation contains historical ride information (Uber & Lyft) with features such as:

- Distance (km)
- Cab type (Uber/Lyft and product line)
- Source and destination
- Timestamps
- Surge multipliers
- Price

**Download Links:**
- 📂 [Raw Data (CSV)](https://drive.google.com/file/d/1QqiydMw3WgQwM4TW102yV6DIzsj8nWNL/view?usp=sharing)  
- 📂 [Predicted Price (CSV)](https://drive.google.com/file/d/1wY2eSUa3pdJPbFn6RETxnWPiYI_4weqj/view?usp=sharing)

---
## Model

- 📂 [Trained Model (`cab_price_model.pkl`)](https://drive.google.com/file/d/1abw48Qjhx4enzQjalfk5IoOuW6Lkxa7l/view?usp=sharing)
---


