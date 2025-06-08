from sklearn.linear_model import LinearRegression
import numpy as np

def predict_prices(data):
    data = data.copy()
    data['Days'] = np.arange(len(data))
    X = data[['Days']]
    y = data['Close']

    model = LinearRegression()
    model.fit(X, y)
    data['Predicted'] = model.predict(X)
    return data