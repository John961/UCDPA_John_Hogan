import pandas as pd
import matplotlib.pyplot as plt

LaLiga_data= pd.read_csv("../FinalProject/laliga_player_stats_english.csv", index_col = 0)

print(LaLiga_data.head())

print(LaLiga_data.isnull().sum())

print(LaLiga_data.info())

print(LaLiga_data.columns)

print(LaLiga_data.iloc[:, 15:17])

print(LaLiga_data[["Goals scored", "Penalties scored"]].sum())
print(943 +104)








