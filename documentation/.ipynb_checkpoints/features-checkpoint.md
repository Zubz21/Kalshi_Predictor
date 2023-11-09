# Detailed Documentation:
---

1. **Date**: Represents the exact date of the trading data. Format: YYYY-MM-DD.

2. **DayOfWeek**: An integer representation of the weekday, where 1 corresponds to Monday and 7 corresponds to Sunday. Useful for identifying weekly trends or anomalies specific to certain days.

3. **Open, High, Low, Close, Adj Close**:
-- Open: The price at which the Nasdaq 100 started trading for the day.
-- High: The peak price at which the Nasdaq 100 traded for that particular day.
-- Low: The lowest price point the Nasdaq 100 dropped to during the day.
-- Close: The final trading price of the Nasdaq 100 when the market closed.
-- Adj Close: Adjusts the closing price to consider events like dividends, stock splits, or new stock offerings.
-- Volume: Represents the number of shares that changed hands during the trading day. Higher volume can indicate higher interest or significant events related to the Nasdaq 100.

4. **OC Difference**: Calculated as Open - Close, this metric provides insight into intraday movement and sentiment direction.

5. **HL Difference**: By calculating the difference High - Low, we capture the total intraday volatility, a measure of uncertainty or potential big news influencing the day's trading.

6. **OC %Change & HL %Change**: These percentage changes offer a normalized view of the intraday price movement and volatility, respectively.

7. **Close_Status**: A binary metric where a value of 1 indicates a rise in the closing price from the previous day and 0 indicates no rise. Useful for trend analysis.

8. **Close_Difference**: Shows the absolute change in the closing price from the previous day, indicating the magnitude of bullish or bearish sentiment.

9. **Same Bracket**: A computed binary feature where 1 indicates that the opening and closing prices were within the same 100-point bracket and 0 otherwise. This can be a direct target for some predictive models.

10. **Avg_OC_Spread_10_Day & Avg_Volume_10_Day**: Moving averages for 10 days offer smoother representations of the data, removing daily noise and emphasizing longer-term trends.

11. **Volatility_10_Day**: Represents the standard deviation of the 10-day OC differences. A higher value indicates higher price volatility, signaling potential uncertainty or major upcoming/recent events.

12. **Price_Change_Magnitude**: An absolute measure that showcases the intensity of price changes, disregarding the direction of the change.

13. **Price_Direction**: A binary classification of whether the stock closed higher (1) than it opened or not (0). This can be used to gauge intraday bullish/bearish sentiment.

14. **MA_Volume_Ratio**: By comparing the day's volume to the 10-day average volume, we can identify surges in trading interest. A ratio significantly above 1 might indicate a strong reaction to recent news or events.