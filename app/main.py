import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model
model = joblib.load('model.joblib')

# Define Flask app
app = Flask(__name__)

# Define endpoint for predicting survival
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    input_data = request.get_json()

    # Convert input data to a pandas DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Make predictions using the loaded model
    predictions = model.predict(input_df)

    # Return predictions as JSON
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
