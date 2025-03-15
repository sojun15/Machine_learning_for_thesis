import pandas as pd

ds = pd.read_csv('heart_disease.csv')
ds.info()
print(ds.to_string())


