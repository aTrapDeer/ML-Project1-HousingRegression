import streamlit as st
import requests

# Streamlit webpage layout
st.title('Housing Price Prediction')

# URL of the Flask app's predict endpoint running inside Docker
url = 'http://localhost:5000/predict'

# Create input fields for each feature
features = []
#Label for each input field
# Descriptive labels as markdown or text
st.markdown('**CRIM**: Per capita crime rate by town.')
features.append(st.number_input('CRIM', value=0.00632))

st.markdown('**ZN**: Proportion of residential land zoned for lots over 25,000 sq.ft.')
features.append(st.number_input('ZN', value=18.0))

st.markdown('**INDUS**: Proportion of non-retail business acres per town.')
features.append(st.number_input('INDUS', value=2.31))

st.markdown('**CHAS**: Charles River dummy variable (1 if tract bounds river; 0 otherwise).')
features.append(st.number_input('CHAS', value=0))

st.markdown('**NOX**: Nitric oxides concentration (parts per 10 million).')
features.append(st.number_input('NOX', value=0.538))

st.markdown('**RM**: Average number of rooms per dwelling.')
features.append(st.number_input('RM', value=6.575))

st.markdown('**AGE**: Proportion of owner-occupied units built prior to 1940.')
features.append(st.number_input('AGE', value=65.2))

st.markdown('**DIS**: Weighted distances to five Boston employment centers.')
features.append(st.number_input('DIS', value=4.0900))

st.markdown('**RAD**: Index of accessibility to radial highways.')
features.append(st.number_input('RAD', value=1))

st.markdown('**TAX**: Full-value property-tax rate per $10,000.')
features.append(st.number_input('TAX', value=296.0))

st.markdown('**PTRATIO**: Pupil-teacher ratio by town.')
features.append(st.number_input('PTRATIO', value=15.3))

st.markdown('**B**: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.')
features.append(st.number_input('B', value=396.90))

st.markdown('**LSTAT**: Percentage of lower status of the population.')
features.append(st.number_input('LSTAT', value=4.98))

# Button to make prediction
if st.button('Predict'):
    # Construct the request payload
    input_features = {"features": features}
    
    # Make a POST request to the Flask app
    response = requests.post(url, json=input_features)
    
    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()
        prediction_price = prediction['prediction'][0]*1000
        st.write(f"Predicted Price: ${prediction_price:,.2f}")
    else:
        st.write("Failed to get prediction.")
        st.write(f"Status code: {response.status_code}")
        st.write(f"Response: {response.text}")
