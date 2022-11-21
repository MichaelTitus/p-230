import pandas as pd
dataset = pd.read_csv('country_vaccinations.csv')
print("shape of dataset",dataset.shape)
print("number of parameters",len(dataset.columns))
print("parameter names",dataset.columns)
print("Display empty row data:",dataset.loc[:,dataset.isna().any()])