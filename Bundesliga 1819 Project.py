import pandas as pd

German_data= pd.read_csv("season-1819_csv.csv", index_col = 0)

print(German_data.head())

print(German_data.isnull().sum())

print(German_data.info())

print(German_data.columns)

print(German_data.iloc[:, 3:5])
print()

print(German_data[["FTHG", "FTAG"]].sum())
print(548 + 425)




