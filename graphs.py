import matplotlib.pyplot as plt

def plot_stock_prices(data, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(data["Date"], data["Close"], label="Actual Price")
    plt.plot(data["Date"], data["Predicted"], label="Predicted Price", linestyle='--')
    plt.title(f"{symbol} Stock Price Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.savefig("price_prediction.png", bbox_inches='tight')