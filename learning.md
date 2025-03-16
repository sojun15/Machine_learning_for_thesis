## At first import pandas before using pandas
import pandas as pd

## Read a csv file then store a variable
ds = pd.read_csv('heart_disease.csv')

## see summary of dataset
ds.head()
print(ds)

## see full dataset values
print(ds.to_string())

## if we see have there any duplicate row in our dataset
ds.duplicated()

## if we see row,collum,not null, datatypes
ds.info()

## A Pandas Series is like a column in a table which holding data of any type.
a = { 'name': ["sojun","sourov"],
'id':[15,17]}
myvar = pd.Series(a)
print(myvar)

## Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

## Return row from 0 to 1 values:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[1])
print(df.loc[[0, 1]])

## if we want to remove empty cell rows then use dropna
new_df = df.dropna() // dropna will return a new dataset removing null,empty values
df.dropna(inplace = True) // it will modify the original dataset removing null,empty values
print(new_df.to_string())

## difference dropna() and drop()
dropna is used to remove rows of null or empty cell 
drop is used to remove row of specific index value

## Replace NULL values with the number 130:
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)

## plot diagram
- if we want to plat diagram for all column then use
ds = pd.read_csv('heart_disease.csv')
ds.plot()
plt.show()

- if we want to plat diagram only two column with x and y axix then use this
ds = pd.read_csv('heart_disease.csv')
ds.plot(kind='scatter',y='target',x='cp')
plt.show()

## correlation between different column
- if i see summary of correlation then use (truncate some column)
print(ds.corr())
- if i see all column correlation then use 
correlation_matrix = ds.corr()
pd.set_option('display.max_columns', None)  // Set option to display all columns
print(correlation_matrix)