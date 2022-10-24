import pandas as pd

global_years_names_list = [2000, 2001 ,2002 ,2003 ,2004 ,2005 ,2006 ,2007 ,2008 ,2009 ,2010 ,2011 ,2012 ,2013 ,2014 ,2015 ,2016 ,2017 ,2018 ,2019]

def get_gdp_data():

    us_gdp_growth_exl = "data_original\\us-gdp-growth.xlsx"

    us_gdp_growth = pd.read_excel(us_gdp_growth_exl)

    list = us_gdp_growth.values

    years_list = list[0]
    years_list = years_list.tolist()
    years_list.remove('United States')

    values_list = list[1]
    values_list = values_list.tolist()
    del values_list[0]

    return global_years_names_list, values_list



def unemplyment_data():
    us_unemplyment_exl = 'data_original\\SeriesReport-uneployment.xlsx'
    us_unemplyment = pd.read_excel(us_unemplyment_exl,header=11 )

    vals_list = us_unemplyment.values.tolist()

    y2000 = vals_list[0]
    y2001 = vals_list[1]
    y2002 = vals_list[2]
    y2003 = vals_list[3]
    y2004 = vals_list[4]
    y2005 = vals_list[5]
    y2006 = vals_list[6]
    y2007 = vals_list[7]
    y2008 = vals_list[8]
    y2009 = vals_list[9]
    y2010 = vals_list[10]
    y2011 = vals_list[11]
    y2012 = vals_list[12]
    y2013 = vals_list[13]
    y2014 = vals_list[14]
    y2015 = vals_list[15]
    y2016 = vals_list[16]
    y2017 = vals_list[17]
    y2018 = vals_list[18]
    y2019 = vals_list[19]
    
    years_list = [y2000,y2001,y2002,y2003,y2004,y2005,y2006,y2007,y2008,y2009,y2010,y2011,y2012,y2013,y2014,y2015,y2016,y2017,y2018,y2019]
    result_list = []

    for year in years_list:
        del year[0]
        del year[12]

        year.append( sum(year) / 12)
        result_list.append(year[12])

   

    return global_years_names_list, result_list

    

def crime_data(input_srt = 'violent' ):

    input_srt = input_srt.lower()
    crime_exl = 'data_original\\table-1.xls'
    crime = pd.read_excel(crime_exl, header=3)

    #print(crime.columns.values)

    Population = crime[['Population1']].head(20).values.tolist()
    Violent_crime = crime[['Violent\ncrime2']].head(20).values.tolist()
    rape_rate = crime[['Rape\n(legacy \ndefinition) \nrate4']].head(20).values.tolist()
    robbery_rate = crime[['Robbery \nrate ']].head(20).values.tolist()
    agg_assult_rate = crime[['Aggravated \nassault rate ']].head(20).values.tolist()
    prop_crime_rate = crime[['Property \ncrime \nrate ']].head(20).values.tolist()


    if 'violent' in input_srt:
        return global_years_names_list, Violent_crime
    elif 'rape' in input_srt:
        return global_years_names_list, rape_rate
    elif 'robbery' in input_srt:
        return global_years_names_list, robbery_rate
    elif 'assult' in input_srt:
        return global_years_names_list, agg_assult_rate
    elif 'property' in input_srt:
        return global_years_names_list, prop_crime_rate





if __name__ == '__main__':

    pass