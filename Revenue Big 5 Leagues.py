import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("statistic_id261218_revenue-of-the-big-five-european-soccer-leagues-1996-2021_csv.csv", index_col=0)
print(data.head())

Top_3 = data.drop(['Italy', 'France'], axis='columns')
print(Top_3)


fig, ax = plt.subplots()
ax.bar(data.index, data["England"])
ax.set_xticklabels(data.index, rotation=90)
ax.set_ylabel("GMV")
plt.show()