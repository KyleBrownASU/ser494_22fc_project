from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from wf_dataprocessing import *
from wf_ml_training import *
import pickle


def make_pred():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)
    
    data = [2019,30414,149]
    data = pd.DataFrame(data)
    data = data.values.reshape(1,-1)
    pred = model.predict(data)


    print(pred)


if __name__ == '__main__':
    make_pred()
