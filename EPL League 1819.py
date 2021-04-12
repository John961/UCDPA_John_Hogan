import pandas as pd

data= pd.read_csv("epl_1819_csv.csv")

print(data.head())

unique_teams = data.drop_duplicates(subset=["Team"])
print(unique_teams)

print(data.iloc[:, 26:30])

