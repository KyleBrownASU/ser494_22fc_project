import pandas as pd

us_gdp_growth_exl = "data_original\\us-gdp-growth.xlsx"

us_gdp_growth = pd.read_excel(us_gdp_growth_exl, index_col= 0, header= 0)

print(us_gdp_growth)