import os
import pandas as pd
import glob



def start():
    path = os.getcwd()
    path = path + '\data_original'
    csv_files = glob.glob(os.path.join(path, "*.xls"))
    print(csv_files)
    print(path)

    for f in csv_files:
        
        # read the csv file
        df = pd.read_excel(f)

        dict = df.to_dict()
        print(dict)
        
        # print the location and filename
        #print('Location:', f)
        #print('File Name:', f.split("\\")[-1])
        
        # print the content
        #print('Content:')
        #print(df)
        #print()

    
   
    






if __name__ == '__main__':
    start()