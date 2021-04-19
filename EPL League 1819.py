import pandas as pd

EPL_data= pd.read_csv("epl_1819_csv.csv", index_col = 0)

print(EPL_data.head())

print(EPL_data.isnull().sum())

print(EPL_data.info())

print(EPL_data.columns)

unique_teams = EPL_data.drop_duplicates()
print(unique_teams)

print(unique_teams.sort_values("attack_scored", ascending=False))

print(unique_teams["attack_scored"].sum())








