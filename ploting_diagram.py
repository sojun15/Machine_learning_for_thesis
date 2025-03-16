import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('heart_disease.csv')
# if i want to plot diagram only two column with x and y axix
ds.plot(kind='scatter',y='target',x='cp')
# if i want to plot diagram for whole dataset then use it
ds.plot()
plt.show()
