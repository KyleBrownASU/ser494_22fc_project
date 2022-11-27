import matplotlib.pyplot as plt
import numpy as np
from wf_dataprocessing2 import *
from wf_ml_evaluation import func
from wf_ml_prediction import var_gdp, var_prop_crime, var_student_pop, var_unemployment, var_year


global_years_names_list = [2000, 2001 ,2002 ,2003 ,2004 ,2005 ,2006 ,2007 ,2008 ,2009 ,2010 ,2011 ,2012 ,2013 ,2014 ,2015 ,2016 ,2017 ,2018 ,2019]

def violent_vs_gdp(violent_crimes_list, gdp_list):
    crimes = np.array(violent_crimes_list)
    gdp = np.array(gdp_list)
   

    plt.plot(global_years_names_list, crimes, c ='black', label = 'Crime Rate')
    plt.plot(global_years_names_list, gdp, c = 'green', label = 'GDP change')
    plt.legend()
    plt.xlabel('Years')
    plt.ylabel('Rate of Change')
    plt.title('Vionlent Crime rate vs GDP change in percent')
    filename = 'visuals/violentCrime_vs_gdp.png'

    plt.savefig(filename)
    plt.close()

def violent_vs_umemployment(violent_crimes_list, unemployment_list):
    crimes = np.array(violent_crimes_list)
    employment = np.array(unemployment_list)

    plt.plot(global_years_names_list, crimes, c ='black', label = 'Crime Rate')
    plt.plot(global_years_names_list, employment, c = 'green', label = 'Percent unemployed')
    plt.legend()
    plt.title("unemployment rate vs crime rate")
    plt.xlabel('Years')
    filename = 'visuals/violentCrime_vs_unemployment.png'

    plt.savefig(filename)
    plt.close()


def property_vs_gdp(property_crime_list, gdp_list):
    property = np.array(property_crime_list)
    gdp = np.array(gdp_list)

    plt.plot(global_years_names_list, property, c = 'black', label = 'Property Crime Rate')
    plt.plot(global_years_names_list, gdp, c = 'green', label = 'GDP change')

    plt.legend()
    filename = 'visuals/property_vs_gdp.png'

    plt.savefig(filename)
    plt.close()

def property_vs_umemployment(property_crime_list, unemployment_list):
    property = np.array(property_crime_list)
    employment = np.array(unemployment_list)

    plt.plot(global_years_names_list, property, c = 'black', label = 'Property Crime Rate')
    plt.plot(global_years_names_list, employment, c = 'green', label = 'Percent unemployed')

    plt.legend()
    filename = 'visuals/property_vs_umemployment.png'

    plt.savefig(filename)
    plt.close()

def rape_vs_umemployment(rape_crime_list, unemployment_list):
    rape = np.array(rape_crime_list)
    employment = np.array(unemployment_list)

    plt.plot(global_years_names_list, rape, c = 'black', label = 'Rape per capita Rate')
    plt.plot(global_years_names_list, employment, c = 'green', label = 'Percent unemployed')
    plt.legend()

    filename = 'visuals/rape_vs_umemployment.png'
    plt.savefig(filename)
    plt.close()

def make_quantitative(gdp_data,crime_data,unemplyment_data,property_crime_data,rape_data):
    output_list = []

    min_data, max_data, median_data = do_quantitative(gdp_data)
    intput_str = ("gdp quantitative is min = ", str(min_data) , " max = ", str(max_data), ' and median = ', str(median_data))
    output_list.append(intput_str)

  

    min_data, max_data, median_data = do_quantitative(unemplyment_data)
    input_str = str("unemplyment_data quantitative is min = ", str(min_data) , " max = ", str(max_data), ' and median = ', str(median_data))
    output_list.append(input_str)



    output_file = open("data_processed\summary.txt", 'w+')

    for i in output_list:
        print(i)
        output_file.write(i)

    output_file.close()

def make_var_year(x, y):
    x = np.array(x)
    y = np.array(y)

    plt.scatter(x, y )
    plt.title("Year vs Estimated violent crime")
    plt.xlabel("Year")
    plt.ylabel("Estimated violent crime ")
    filename = 'visuals/Year_vs_Estimated_violent_crime.png'
    plt.savefig(filename)
    plt.close()

def make_var_gdp(x, y):
    x = np.array(x)
    y = np.array(y)

    plt.scatter(x, y )
    plt.title("GDP vs Estimated violent crime")
    plt.xlabel("Gdp")
    plt.ylabel("Estimated violent crime ")
    filename = 'visuals/GDP_vs_Estimated_violent_crime.png'
    plt.savefig(filename)
    plt.close()

def make_student_pop(x, y):
    x = np.array(x)
    y = np.array(y)

    plt.scatter(x, y )
    plt.title("student population vs Estimated violent crime")
    plt.xlabel("student population")
    plt.ylabel("Estimated violent crime ")
    filename = 'visuals/student_pop_vs_Estimated_violent_crime.png'
    plt.savefig(filename)
    plt.close()



if __name__ == '__main__':
    gdp_data = get_gdp_data()
    crime_data = get_crime_data()
    unemplyment_data = get_unemplyment_data()
    property_crime_data = get_crime_data('property')
    rape_data = get_crime_data('rape')

    #rape_vs_umemployment(rape_data, unemplyment_data)
    #violent_vs_umemployment(crime_data, unemplyment_data)
    #violent_vs_gdp(crime_data, gdp_data)
    #property_vs_gdp(property_crime_data, gdp_data)
    #property_vs_umemployment(property_crime_data, unemplyment_data)
    
    func()

    x, y = var_year()
    make_var_year(x, y)

    x, y = var_gdp()
    make_var_gdp(x, y)
    x, y = var_student_pop()
    make_student_pop(x ,y)


