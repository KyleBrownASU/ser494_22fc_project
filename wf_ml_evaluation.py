from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from wf_dataprocessing import *
from wf_ml_training import *
import pickle
import numpy as np

def func():
    start()
    data = pd.read_csv('data_processed\output.csv')
    print(data.iloc[:, 0:6].apply(np.average))

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
    

'''
mean
year                  2011.969277
student_pop_sum      13271.088578
prop_crime_sum         129.383300
gdp                      1.934765
unemployment             6.208646
violent_crime_sum        4.914148

min 
year                 2005.000000
student_pop_sum        12.000000
prop_crime_sum          0.000000
gdp                    -2.599888
unemployment            3.675000
violent_crime_sum       0.000000

max
year                   2019.000000
student_pop_sum      127582.000000
prop_crime_sum         1358.000000
gdp                       3.483220
unemployment              9.608333
violent_crime_sum       114.000000

'''