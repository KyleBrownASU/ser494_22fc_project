from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from wf_dataprocessing import *


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




if __name__ == '__main__':
    gdp_data = get_gdp_data()
    crime_data = get_crime_data()
    unemplyment_data = get_unemplyment_data()
    property_crime_data = get_crime_data('property')
    rape_data = get_crime_data('rape')

    rape_vs_umemployment(rape_data, unemplyment_data)
    violent_vs_umemployment(crime_data, unemplyment_data)
    violent_vs_gdp(crime_data, gdp_data)
    property_vs_gdp(property_crime_data, gdp_data)
    property_vs_umemployment(property_crime_data, unemplyment_data)
    

