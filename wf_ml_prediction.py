import pandas as pd
#import numpy as np
import pickle


def make_pred():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)
    
    data = [2014,16646.0,181.0,2.287775933,6.158333333333334]
    data = pd.DataFrame(data)
    data = data.values.reshape(1,-1)
    pred = model.predict(data)

    print(pred) # expected was 14 [19.48717727]

    data = [2010,38550.0,870.0,2.708856694,9.608333333333333]
    data = pd.DataFrame(data)
    data = data.values.reshape(1,-1)
    pred = model.predict(data)
    print(pred) #expected was 110 [78.58852103]

def var_year():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)

    y = []
    x = []
    year = 2005
    local_data = [year, 13271, 129, 1.934765, 6.208646]
    
    while local_data[0] < 2020:
        x.append(local_data[0])
        data = pd.DataFrame(local_data)
        data = data.values.reshape(1,-1)
        pred = model.predict(data)
        
        y.append(pred[0])
        
        local_data[0] +=1


    return x, y

def var_student_pop():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)

    local_data = [2011, 12, 129, 1.934765, 6.208646]
    y = []
    x = []

    while local_data[1] < 127583:
        x.append(local_data[1])
        data = pd.DataFrame(local_data)
        data = data.values.reshape(1,-1)
        pred = model.predict(data)
        
        y.append(pred[0])


        local_data[1] +=10

    return x, y

def var_prop_crime():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)

    local_data = [2011, 13271, 0, 1.934765, 6.208646]
    y = []
    x = []

    while local_data[2] < 1358:
        x.append(local_data[2])
        data = pd.DataFrame(local_data)
        data = data.values.reshape(1,-1)
        pred = model.predict(data)
        
        y.append(pred[0])


        local_data[2] += 1

    return x, y

def var_gdp():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)

    local_data = [2011, 13271, 129, -2.599888, 6.208646]
    y = []
    x = []

    while local_data[3] < 3.483220:
        x.append(local_data[3])
        data = pd.DataFrame(local_data)
        data = data.values.reshape(1,-1)
        pred = model.predict(data)
        
        y.append(pred[0])


        local_data[3] += 0.001

    return x, y

def var_unemployment():
    with open('models/model_pickle', 'rb') as f:
        model = pickle.load(f)

    local_data = [2011, 13271, 129, 1.934765, 3.675000]
    y = []
    x = []

    while local_data[4] < 9.608333:
        x.append(local_data[4])
        data = pd.DataFrame(local_data)
        data = data.values.reshape(1,-1)
        pred = model.predict(data)
        
        y.append(pred[0])


        local_data[4] += 0.001

    return x, y



if __name__ == '__main__':
    x, y = var_unemployment()
    #print(x)
    #print(y)
    print(len(y))
    av_data = [2011, 13271, 129, 1.934765, 6.208646]
    


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