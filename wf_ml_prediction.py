import pandas as pd
import pickle


def make_pred():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)
    
    data = [2019,30414,149]
    data = pd.DataFrame(data)
    data = data.values.reshape(1,-1)
    pred = model.predict(data)

    print(pred) # expected was 14 [19.48717727]

    data = [2006,187477,2687]
    data = pd.DataFrame(data)
    data = data.values.reshape(1,-1)
    pred = model.predict(data)
    print(pred) #expected was 110 [78.58852103]


if __name__ == '__main__':
    make_pred()
