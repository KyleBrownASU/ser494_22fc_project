from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def func():
    data = pd.read_csv('data_processed\output.csv')
    y= data['violent_crime_sum']
    x = data.drop('violent_crime_sum', axis= 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state= 100)

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_train_pred = lr.predict(x_train)
    y_test_pred = lr.predict(x_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    r2_train = r2_score(y_train, y_train_pred)

    test_mse = mean_squared_error(y_test, y_test_pred)
    r2_test = r2_score(y_test, y_test_pred)

    print("MSE Train = ", train_mse)
    print("r2 train = ", r2_train)
    print("MSE test = ", test_mse)
    print("r2 test = ", r2_test)    









if __name__ == '__main__':
    func()
    