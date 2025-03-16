import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('heart_disease.csv')
# if i want to see histogram for a particular column then write that column into ds[]
ds['age'].plot(kind='hist')
plt.show()
