from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# Load the trained model
with open("cab_price_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from frontend
        data = request.json

        # Extract values
        distance = float(data.get("distance", 0))
        cab_type = data.get("cab_type", "")
        source = data.get("source", "")
        destination = data.get("destination", "")
        time_stamp = int(data.get("time_stamp", 0))
        surge_multiplier = float(data.get("surge_multiplier", 1.0))

        # Convert timestamp to datetime
        dt = datetime.fromtimestamp(time_stamp / 1000)
        hour = dt.hour
        day_of_week = dt.weekday()
        month = dt.month

        # Feature engineering
        distance_surge = distance * surge_multiplier
        peak_hour = 1 if 7 <= hour <= 10 or 17 <= hour <= 20 else 0
        is_weekend = 1 if day_of_week >= 5 else 0

        # Create a dataframe with same columns as training
        X_new = pd.DataFrame(columns=model.feature_names_in_)
        X_new.loc[0] = 0  # start with zeros

        # Fill numeric columns
        numeric_features = {
            "distance": distance,
            "surge_multiplier": surge_multiplier,
            "hour": hour,
            "day_of_week": day_of_week,
            "month": month,
            "distance_surge": distance_surge,
            "peak_hour": peak_hour,
            "is_weekend": is_weekend
        }

        for col, val in numeric_features.items():
            if col in X_new.columns:
                if np.issubdtype(X_new[col].dtype, np.integer):
                    X_new.at[0, col] = int(val)
                else:
                    X_new.at[0, col] = float(val)

        # Fill one-hot categorical features
        for cat, val in {
            f"cab_type_{cab_type}": 1,
            f"source_{source}": 1,
            f"destination_{destination}": 1,
            f"name_{cab_type}": 1
        }.items():
            if cat in X_new.columns:
                X_new.at[0, cat] = val

        # Make prediction
        predicted_price = model.predict(X_new)[0]

        return jsonify({"predicted_price": round(float(predicted_price), 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
