import pandas as pd

data= pd.read_csv("season-1819_csv.csv")

print(data.head())

print(data.iloc[:, 4:6])
print()

df = pd.dataframe(data,columns=['FTHG'])
sum_column = df.sum('FTHG')
print(sum_column)