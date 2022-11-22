from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from wf_dataprocessing import *
from wf_ml_training import *
import pickle

def func():
    start()
    data = pd.read_csv('data_processed\output.csv')
    y= data['violent_crime_sum']
    x = data.drop('violent_crime_sum', axis= 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state= 100)

    y_train_pred, y_test_pred, model = train(x_train, x_test, y_train, y_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    r2_train = r2_score(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    r2_test = r2_score(y_test, y_test_pred)

    str1 = "MSE Train = " + repr(train_mse) + "\n"
    str2 = "r2 train = " + repr(r2_train) + "\n"
    str3 = "MSE test = " + repr(test_mse) + "\n"
    str4 = "r2 test = " + repr(r2_test) + "\n"

    with open('evaluation\summary.txt', 'w') as f:
        f.writelines(str1)
        f.writelines(str2)
        f.writelines(str3)
        f.writelines(str4)

    with open('models/model_pickle', 'wb') as f:
        pickle.dump(model,f)



if __name__ == '__main__':
    func()
    