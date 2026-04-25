import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()

def train():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([15, 30, 45, 60, 75])
    model.fit(X, y)

def predict(value):
    return float(model.predict([[value]])[0])