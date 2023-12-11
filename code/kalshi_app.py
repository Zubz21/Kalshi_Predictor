import streamlit as st
import numpy as np
import pickle

# Load your trained model
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the app layout
st.title('Stock Close Price Prediction')

# Create inputs for each feature
open_p = st.number_input('Open Price', format='%.10f')
avg_oc_spread_10_day = st.number_input('Average Open-Close Spread Over 10 Days', format='%.10f')
avg_volume_10_day = st.number_input('Average Volume Over 10 Days', format='%.10f')
volatility_10_day = st.number_input('Volatility Over 10 Days', format='%.10f')
price_change_magnitude = st.number_input('Price Change Magnitude', format='%.10f')
price_direction = st.number_input('Price Direction (Enter 1 for Up, 0 for Down)', format='%.10f')
ma_volume_ratio = st.number_input('Moving Average Volume Ratio')
close_lag_5 = st.number_input('Close Lag 5', format='%.10f')
close_lag_4 = st.number_input('Close Lag 4', format='%.10f')
close_lag_3 = st.number_input('Close Lag 3', format='%.10f')
close_lag_2 = st.number_input('Close Lag 2', format='%.10f')
close_lag_1 = st.number_input('Close Lag 1', format='%.10f')
shortema = st.number_input('Short-term EMA', format='%.10f')
longema = st.number_input('Long-term EMA', format='%.10f')
macd = st.number_input('MACD', format='%.10f')

# When the 'Predict' button is clicked, make a prediction and display it
if st.button('Predict'):
    features = np.array([[open_p,avg_oc_spread_10_day, avg_volume_10_day, volatility_10_day,
                          price_change_magnitude, price_direction, ma_volume_ratio,
                          close_lag_5, close_lag_4, close_lag_3, close_lag_2,
                          close_lag_1, shortema, longema, macd]])
    
    prediction = model.predict(features)
    st.write(f'Predicted Close Price: {prediction[0]}')

# The standard deviation of residuals could be used to give a range of predicted prices
# This would typically be calculated during model training and hardcoded here, or dynamically adjusted
# standard_deviation_of_residuals = <your_calculated_value>
# prediction_interval = 1.96 * standard_deviation_of_residuals
# st.write(f'95% prediction interval: {prediction[0] - prediction_interval} to {prediction[0] + prediction_interval}')
std_dev_residuals = 10.839669987848684 # replace with your actual standard deviation value

# Calculate a 95% prediction interval assuming normally distributed residuals
interval_range = 1.96 * std_dev_residuals

# When the 'Predict' button is clicked, make a prediction and display it
if st.button('Predict Range'):
    features = np.array([[open_p, avg_oc_spread_10_day, avg_volume_10_day, volatility_10_day,
                          price_change_magnitude, price_direction, ma_volume_ratio,
                          close_lag_5, close_lag_4, close_lag_3, close_lag_2,
                          close_lag_1, shortema, longema, macd]])
    
    # Use the model to make a prediction
    prediction = model.predict(features)
    
    # Calculate the lower and upper bounds of the 95% prediction interval
    lower_bound = prediction[0] - interval_range
    upper_bound = prediction[0] + interval_range
    
    # Display the predicted close price and the prediction interval
    st.write(f'Predicted Close Price: {prediction[0]}')
    st.write(f'95% prediction interval: {lower_bound} to {upper_bound}')

