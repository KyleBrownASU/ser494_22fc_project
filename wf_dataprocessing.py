import os
import pandas as pd
import glob


#form1 = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2017', '2018', '2019',] # 0,1,2,3,4,9
#form2 = ['2013','2014','2015'] # 0,1,2,3,4,10

state_names = ["Alaska", "Alabama", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
    "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
    "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

alabamba = []
    

def start():
    

    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    #print(csv_files)
    #print(path)
    state_data_list = []

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

        #print(state_index_list)

        #print(df)


        for int in range(len(state_index_list)-2):
            start_val = state_index_list[int]
            state_name_start = df.loc[start_val].iat[0]
            state_name = ''.join([i for i in state_name_start if not i.isdigit()])
            state_name = state_name.lower()
            state_name = state_name.replace(' ', '')

            student_pop_sum = 0
            violent_crime_sum = 0
            prop_crime_sum = 0

            schools_in_state = state_index_list[int] - state_index_list[int - 1]

            for i in range(schools_in_state):
                if start_val + i < rows - 20:
                    student_pop =  df.loc[start_val + i].iat[3]
                    violent_crime =  df.loc[start_val + i].iat[4]
                    prop_crime=  df.loc[start_val + i].iat[5]

                    if pd.notnull(student_pop) : student_pop_sum += student_pop
                    if pd.notnull(violent_crime) : violent_crime_sum += violent_crime
                    if pd.notnull(prop_crime) : prop_crime_sum += prop_crime

            year = (file[-8:-4])
            #print(state_name, student_pop_sum, violent_crime_sum, prop_crime_sum, year)
            print(state_name)
        print("")

            


       
    
    #print(len(state_names))

    


if __name__ == '__main__':
    start()