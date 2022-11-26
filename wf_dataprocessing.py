import os
import pandas as pd
import glob
import csv


def start():
    alabama = [],
    alaska = [],
    arizona = [],
    arkansas = [],
    california = [],
    colorado = [],
    connecticut = [],
    delaware = [],
    florida = [],
    georgia = [],
    illinois = [],
    indiana = [],
    iowa = [],
    kansas = [],
    kentucky = [],
    louisiana = [],
    maine = [],
    maryland = [],
    massachusetts = [],
    michigan = [],
    minnesota = [],
    mississippi = [],
    missouri = [],
    montana = [],
    nebraska = [],
    nevada = [],
    newhampshire = [],
    newjersey = [],
    newmexico = [],
    newyork = [],
    northcarolina = [],
    northdakota = [],
    ohio = [],
    oklahoma = [],
    pennsylvania = [],
    rhodeisland = [], 
    southcarolina = [], 
    southdakota = [],  
    tennessee = [],  
    texas = [], 
    utah = [],
    vermont = [], 
    virginia = [],   
    washington = [],  
    westvirginia = [],
    wisconsin = [],
    oregon = [],


    state_dict = {"alabama": alabama, "alaska" :alaska, "arizona" :arizona , "arkansas" :arkansas, "california" :california , "colorado" : colorado, "connecticut" :connecticut ,"delaware" : delaware,
    "florida" : florida, "georgia" : georgia, "illinois" :illinois , "indiana" :indiana , "iowa" :iowa , "kansas" :kansas , "kentucky" :kentucky , 'louisiana' : louisiana, "maine" :maine ,
    "maryland" :maryland , "massachusetts" :massachusetts , "michigan" :michigan ,  "minnesota" :minnesota , "mississippi" : mississippi, "missouri" : missouri , "montana" : montana, 
    "nebraska" : nebraska, "nevada" :nevada , "newhampshire" :newhampshire , "newjersey" : newjersey, "newmexico" :newmexico , "newyork" :newyork , "northcarolina" :northcarolina , "northdakota" :northdakota ,
    "ohio" :ohio , "oklahoma" :oklahoma , "pennsylvania" :pennsylvania , "rhodeisland" :rhodeisland , "southcarolina" : southcarolina, "southdakota" :southdakota , "tennessee" :tennessee , 
    "texas" : texas, "utah" : utah, "vermont" : vermont,"virginia" :virginia ,"washington" :washington , "westvirginia" :westvirginia,"wisconsin" :wisconsin, "oregon" :oregon, "massachusettes" :massachusetts   } 


    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    #print(csv_files)
    #print(path)

    my_file = open('data_processed\output.csv', 'w', newline = '')
    writer = csv.writer(my_file)
    writer.writerow(['year', 'student_pop_sum', 'prop_crime_sum', 'violent_crime_sum'])
    

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
            
            state = state_dict.get(state_name)
            #print(state_name, year)
            state = state[0]
            #print((state))
            data = [year, student_pop_sum, prop_crime_sum, violent_crime_sum]
            writer.writerow(data)
            #print(data)
            state.append(data)
            #print(state)

    result_list = list(state_dict.values())
    '''
    my_file = open('data_processed\output.csv', 'w')
    writer = csv.writer(my_file)
    writer.writerow(['year', 'student_pop_sum', 'prop_crime_sum', 'violent_crime_sum'])

    for i in result_list:
        i = i[0]
        for y in i:
            data0, data1, data2, data3 = y
            input_list = [data0,data1,data2,data3]
            writer.writerow(input_list)
    '''
    my_file.close()
    return( result_list)
    


if __name__ == '__main__':
    start()