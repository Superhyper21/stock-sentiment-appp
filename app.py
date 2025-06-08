import streamlit as st
from fetch_data import get_stock_data
from sentiment_analysis import analyze_sentiment
from prediction_model import predict_prices
from graphs import plot_stock_prices

st.title("📊 Stock Price Prediction with Sentiment Analysis")

symbol = st.text_input("Enter stock symbol (e.g., AAPL, TSLA)", value="AAPL")

if st.button("Predict"):
    st.write(f"Fetching data for: {symbol}")
    df = get_stock_data(symbol)

    headlines = [
        "Company is doing well this quarter.",
        "Investors are optimistic about the new product.",
        "Analysts give a strong buy rating."
    ]
    sentiments = analyze_sentiment(headlines)
    avg_sentiment = sum(sentiments) / len(sentiments)

    st.write(f"📈 Average Sentiment Score: {avg_sentiment:.2f}")

    df_pred = predict_prices(df)
    plot_stock_prices(df_pred, symbol)

    st.image("price_prediction.png", caption="Stock Price Prediction Graph")