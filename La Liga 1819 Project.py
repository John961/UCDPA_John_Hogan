import pandas as pd

data= pd.read_csv("../FinalProject/laliga_player_stats_english.csv")

print(data.head())

Goals_Scored = data.sort_values("Goals scored", ascending=False)
print(Goals_Scored)

print(data.iloc[:, 16:18])
print()

Sum_Goals = ["Goals scored"] + ["Penalties scored"]
print(Sum_Goals)




