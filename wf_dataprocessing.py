import os
import pandas as pd
import glob
import csv
from wf_dataprocessing2 import *


def start():
    my_file = open('data_processed\output.csv', 'w', newline = '')
    writer = csv.writer(my_file)
    writer.writerow(['year', 'student_pop_sum', 'prop_crime_sum', 'gdp', 'unemployment' , 'violent_crime_sum'])

    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    
    for file in csv_files:
        
        # read the csv file
        if '2013' in file or '2014' in file or '2015' in file:

            df = pd.read_excel(file, header = 3, usecols=[0,1,2,3,4,10 ])
        else:
            df = pd.read_excel(file, header = 3, usecols=[0,1,2,3,4,9])
 

        for index, row in df.iterrows():
            value = df.loc[index].iat[0]
            if pd.notnull(value):
                #print(len(value), value)
                if len(value) > 20:
                    df.drop(index, inplace=True)
        
        year = (file[-8:-4])
        gdp, unemployment = get_year_data(year)

        for index, row in df.iterrows():        
            student_pop = df.loc[index].iat[3]
            violent_crime = df.loc[index].iat[4]
            prop_crime = df.loc[index].iat[5]

            

            

            if pd.notnull(student_pop) and pd.notnull(violent_crime) and pd.notnull(prop_crime):

                data = [year, student_pop, prop_crime, gdp, unemployment, violent_crime]
                writer.writerow(data)

    my_file.close()
    

if __name__ == '__main__':
    start()