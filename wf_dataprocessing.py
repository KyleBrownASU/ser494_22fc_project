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

def start():
    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    #print(csv_files)
    #print(path)

    for f in csv_files:
        
        # read the csv file
        if '2013' in f or '2014' in f or '2015' in f:

            df = pd.read_excel(f, header = 3, usecols=[0,1,2,3,4,10 ])
        else:
            df = pd.read_excel(f, header = 3, usecols=[0,1,2,3,4,9])
        dict = df.to_dict()

        print(df.shape)

        #print(f, dict.keys())
        
        # print the location and filename
        #print('Location:', f)
        #print('File Name:', f.split("\\")[-1])
        

        # print the content
        #print('Content:')
        #print(df)
        #print()
    
    #print(len(state_names))

    
   
    






if __name__ == '__main__':
    start()