from flask import Flask, request, jsonify  
from joblib import load 

app = Flask(__name__)

#Load trained model
model = load('linear_regression_model.joblib')  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    