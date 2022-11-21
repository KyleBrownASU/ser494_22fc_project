import os
import pandas as pd
import glob
from dataclasses import dataclass, field

#form1 = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2017', '2018', '2019',] # 0,1,2,3,4,9
#form2 = ['2013','2014','2015'] # 0,1,2,3,4,10

state_names = ["Alaska", "Alabama", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
    "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
    "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

@dataclass
class state_data():
    name: str
    student_pop_list : list= field(init=False)
    violent_crime_list : list= field(init=False)
    prop_crime_list : list = field(init=False)

def start():
    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    #print(csv_files)
    #print(path)

    for file in csv_files:
        
        # read the csv file
        if '2013' in file or '2014' in file or '2015' in file:

            df = pd.read_excel(file, header = 3, usecols=[0,1,2,3,4,10 ])
        else:
            df = pd.read_excel(file, header = 3, usecols=[0,1,2,3,4,9])
        dict = df.to_dict()

        rows, cols = df.shape

        for index, row in df.iterrows():
            value = df.loc[index].iat[0]
            if pd.notnull(value):
                #print(len(value), value)
                if len(value) > 20:
                    df.drop(index, inplace=True)


        state_index_list = []
        for index, row in df.iterrows():
            value = df.loc[index].iat[0]
            if pd.notnull(value):
                state_index_list.append(index)

        print(state_index_list)

       
    
    #print(len(state_names))

    


if __name__ == '__main__':
    start()