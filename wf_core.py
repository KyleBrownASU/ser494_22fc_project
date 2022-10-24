from wf_dataprocessing import *
from wf_visualization import *


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