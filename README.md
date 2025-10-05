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
- This model has `97%` Accuracy  

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
## How to Run the Project

**Step-by-step instructions:**

**1. Download Project Files :**
- Download the backend, frontend, notebook, and other files from this repository.
- Download the trained model (cab_price_model.pkl)
- Download the raw dataset

**2. Ensure Python 3.8+ is installed on your system.**

**3. Install Required Libraries :**
- Open a terminal in the project folder and run : pip install -r requirements.txt

**4. Run the Backend (Flask API) :**
- Start the Flask server : python app.py
- The app will run locally at : http://127.0.0.1:5000/

**5. Open the Frontend :**
- Open templates/index.html in a browser.
- Fill in ride details and click Predict Price to see the predicted fare.
- Ensure the backend is running for predictions to work.
  
<a href="https://github.com/Surajsuri0/cab_price_prediction_ML/blob/main/Screenshots/Cab%20Price%20Prediction.mp4">Demo Video</a>

---
## Screenshots
<img width="634" height="795" alt="Input Cab Price Prediction" src="https://github.com/user-attachments/assets/fc7f6869-485e-4226-83ef-04fe5e1cb3fa" />
<img width="1038" height="614" alt="Predicted Cab Price" src="https://github.com/user-attachments/assets/5045c4d4-5e0c-4402-996f-550bbf608591" />

---
## Questions (KPIs)
- How accurate are the predicted fares compared to actual fares?
- What is the model’s error distribution for different cab types?
- Does the model maintain accuracy during peak hours versus non-peak hours?
- How does surge pricing affect prediction accuracy?
- What percentage of predictions fall within an acceptable error margin (e.g., ±$1)?
- How fast does the web application return a prediction?
- Are users entering all necessary inputs correctly, or are there frequent input errors?
- How many users interact with the prediction tool per day/week?
- Do users revisit the app after their first prediction?
- Are users satisfied with the predicted prices and the clarity of the interface?

---
## Final Conclusion
This project demonstrates a complete end-to-end workflow for predicting cab prices using machine learning. From data preprocessing and feature engineering to model training, evaluation, and deployment through a Flask web application, it showcases how predictive models can be integrated into an interactive and user-friendly interface. The app allows users to quickly estimate ride fares based on distance, cab type, source/destination, timestamp, and surge multiplier. This repository serves as both a practical tool for fare estimation and a learning resource for building, deploying, and sharing machine learning projects. With organized code, clear documentation, and accessible model files, it provides a professional template for similar regression-based prediction projects.
