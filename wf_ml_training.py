from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train(x_train, x_test, y_train, y_test):
    lr = LinearRegression()
    lr.fit(x_train.values, y_train.values)
    y_train_pred = lr.predict(x_train)
    y_test_pred = lr.predict(x_test)
    
    return y_train_pred, y_test_pred, lr