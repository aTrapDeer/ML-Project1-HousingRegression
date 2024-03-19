import requests
import json

# URL of the Flask app's predict endpoint running inside Docker
url = 'http://localhost:5000/predict'

# Example input features for the model
# Make sure this matches the expected input structure in your Flask app
input_features = {
    "features": [0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900, 1, 296.0, 15.3, 396.90, 4.98]
}

# Make a POST request to the Flask app
response = requests.post(url, json=input_features)

# Check if the request was successful
if response.status_code == 200:
    # Get the prediction from the response
    prediction = response.json()
    print("Prediction:", prediction)
else:
    print("Failed to get prediction. Status code:", response.status_code)
    print("Response:", response.text)
