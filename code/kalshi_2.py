import streamlit as st
import numpy as np
import pickle

# Load your trained model
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the app layout
st.title('Stock Close Price Prediction for Next 5 Days')

# Create inputs for each feature
open_p = st.number_input('Open Price', format='%.10f')
avg_oc_spread_10_day = st.number_input('Average Open-Close Spread Over 10 Days', format='%.10f')
avg_volume_10_day = st.number_input('Average Volume Over 10 Days', format='%.10f')
volatility_10_day = st.number_input('Volatility Over 10 Days', format='%.10f')
price_change_magnitude = st.number_input('Price Change Magnitude', format='%.10f')
price_direction = st.number_input('Price Direction (Enter 1 for Up, 0 for Down)', format='%.10f')
ma_volume_ratio = st.number_input('Moving Average Volume Ratio', format='%.10f')
close_lag_5 = st.number_input('Close Lag 5', format='%.10f')
close_lag_4 = st.number_input('Close Lag 4', format='%.10f')
close_lag_3 = st.number_input('Close Lag 3', format='%.10f')
close_lag_2 = st.number_input('Close Lag 2', format='%.10f')
close_lag_1 = st.number_input('Close Lag 1', format='%.10f')
shortema = st.number_input('Short-term EMA', format='%.10f')
longema = st.number_input('Long-term EMA', format='%.10f')
macd = st.number_input('MACD', format='%.10f')

# Predict button
if st.button('Predict'):
    # Initialize an empty list to store predictions
    predictions = []

    # Initial features for the first prediction
    features = [open_p, avg_oc_spread_10_day, avg_volume_10_day, volatility_10_day,
                price_change_magnitude, price_direction, ma_volume_ratio,
                close_lag_5, close_lag_4, close_lag_3, close_lag_2,
                close_lag_1, shortema, longema, macd]

    for i in range(5):
        # Make prediction for the next day
        prediction = model.predict(np.array([features]))[0]
        predictions.append(prediction)

        # Update features for the next prediction
        # Note: This step needs to be customized based on how your features should be updated
        features = update_features(features, prediction)

    # Display predictions
    for i, pred in enumerate(predictions):
        st.write(f'Day {i+1} Predicted Close Price: {pred}')
