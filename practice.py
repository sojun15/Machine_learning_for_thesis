import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('heart_disease.csv')
ds['age'].plot(kind='hist')
plt.show()
