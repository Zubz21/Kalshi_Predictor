# Nasdaq 100 Closing Price Range Prediction
---

## Problem Statement
Financial markets, though seemingly random, are influenced by a myriad of factors ranging from macroeconomic indicators to investor sentiment. A significant challenge in the world of trading and investment is predicting where a specific index or stock will close on any given day. This project focuses on the Nasdaq 100 index, aiming to predict the closing price range based on historical data. By accurately predicting the range in which the Nasdaq 100 will close, we can make more informed financial decisions, potentially leading to profitable trading strategies.

#### Objectives
**1. Predict the range within which the Nasdaq 100 will close on a particular day.**
**2. Understand the features that most influence these predictions.**

---

## Dataset
Our dataset comprises Nasdaq 100 data spanning the last 5 years, from 2019 to the present.

#### Features
1. **Date**: Represents the exact date of the trading data. Format: YYYY-MM-DD.
2. **DayOfWeek**: An integer representation of the weekday, where 1 corresponds to Monday and 7 corresponds to Sunday. Useful for identifying weekly trends or anomalies specific to certain days.
3. **Open**: The price at which the Nasdaq 100 started trading for the day.
4. **High**: The peak price at which the Nasdaq 100 traded for that particular day.
5. **Low**: The lowest price point the Nasdaq 100 dropped to during the day.
6. **Close**: The final trading price of the Nasdaq 100 when the market closed.
7. **Adj Close**: Adjusts the closing price to consider events like dividends, stock splits, or new stock offerings.
8. **Volume**: Represents the number of shares that changed hands during the trading day. Higher volume can indicate higher interest or significant events related to the Nasdaq 100.
9. **OC Difference**: Calculated as Open - Close, this metric provides insight into intraday movement and sentiment direction.
10. **HL Difference**: By calculating the difference High - Low, we capture the total intraday volatility, a measure of uncertainty or potential big news influencing the day's trading.
11. **OC %Change & HL %Change**: These percentage changes offer a normalized view of the intraday price movement and volatility, respectively.
12. **Close_Status**: A binary metric where a value of 1 indicates a rise in the closing price from the previous day and 0 indicates no rise. Useful for trend analysis.
13. **Close_Difference**: Shows the absolute change in the closing price from the previous day, indicating the magnitude of bullish or bearish sentiment.
14. **Same Bracket**: A computed binary feature where 1 indicates that the opening and closing prices were within the same 100-point bracket and 0 otherwise. This can be a direct target for some predictive models.
15. **Avg_OC_Spread_10_Day & Avg_Volume_10_Day**: Moving averages for 10 days offer smoother representations of the data, removing daily noise and emphasizing longer-term trends.
16. **Volatility_10_Day**: Represents the standard deviation of the 10-day OC differences. A higher value indicates higher price volatility, signaling potential uncertainty or major upcoming/recent events.
17. **Price_Change_Magnitude**: An absolute measure that showcases the intensity of price changes, disregarding the direction of the change.
18. **Price_Direction**: A binary classification of whether the stock closed higher (1) than it opened or not (0). This can be used to gauge intraday bullish/bearish sentiment.
19. **MA_Volume_Ratio**: By comparing the day's volume to the 10-day average volume, we can identify surges in trading interest. A ratio significantly above 1 might indicate a strong reaction to recent news or events.
20. **Close_Lag_x**: Represents the closing price of the stock x days ago. Useful to track short-term price movements and recognize patterns or trends.
21. **ShortEMA & LongEMA**: Exponential Moving Averages assign more weight to recent prices while still considering a history of prices.
    ShortEMA (typically 12 days): Gives more recent prices greater significance, reacts more quickly to price changes.
    LongEMA (typically 26 days): Considers a longer window, smoother than the short EMA.
    These EMAs are commonly used to identify bullish or bearish trends in the stock market.
22. **MACD (Moving Average Convergence Divergence)**: Calculated as the difference between the ShortEMA and the LongEMA. Helps identify changes in the strength, direction, momentum, and duration of a trend. A positive MACD indicates that the short-term average is above the long-term average, suggesting upward momentum. Conversely, a negative MACD indicates potential downward momentum.
23. **SignalLine**: A moving average (typically 9 days) of the MACD. Used as a trigger for buy or sell signals. When the MACD crosses above the SignalLine, it's a bullish sign, suggesting a potential buy opportunity. Conversely, when the MACD crosses below the SignalLine, it's a bearish sign.
24. **MACD_Histogram**: Represents the difference between MACD and its SignalLine. Helps visualize when the MACD is above or below the SignalLine. Positive values indicate bullish momentum, while negative values indicate bearish momentum.
25. **RSI (Relative Strength Index)**: Ranges from 0 to 100 and measures the speed and change of price movements. An RSI above 70 is typically considered overbought (indicating it might be overvalued and is a good candidate for selling), while an RSI below 30 is considered oversold (indicating potential undervaluation and might be a good buying opportunity). Helps traders identify potential reversals in price trends.

#### Target Variable
The range within which the Nasdaq 100 closes on a particular day. Ranges are defined in increments of 100 points (e.g., 14600-14700, 14700-14800).

---

## Models & Techniques
Given the nature of the problem (multiclass classification), a variety of machine learning models, including but not limited to Random Forests, Gradient Boosting Machines (like XGBoost), and Neural Networks, are employed. Time series considerations, feature engineering, and data transformations are utilized to optimize predictions.

---

## Evaluation
Models are evaluated based on metrics suitable for multiclass classification, such as accuracy, F1-score, precision, recall, and the confusion matrix. Special attention is given to minimizing false positives or false negatives to align with financial objectives.

---

## Contributions:
Contributions are welcome! Please fork the repository and open a pull request with your changes, or open an issue to discuss a potential change.

