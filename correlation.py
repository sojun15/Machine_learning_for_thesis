import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('heart_disease.csv')
# print summary of correlation that truncating some column
print(ds.corr())

# if i want to display all columns correlation
correlation_matrix = ds.corr()
pd.set_option('display.max_columns', None)
print(correlation_matrix)
