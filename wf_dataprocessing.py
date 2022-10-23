import pandas as pd

us_gdp_growth_exl = "data_original\\us-gdp-growth.xlsx"

us_gdp_growth = pd.read_excel(us_gdp_growth_exl)

list = us_gdp_growth.values

years_list = list[0]
years_list = years_list.tolist()
years_list.remove('United States')

values_list = list[1]
values_list = values_list.tolist()
del values_list[0]

print(years_list)
print(values_list)
