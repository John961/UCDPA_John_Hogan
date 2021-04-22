import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("statistic_id261218_revenue-of-the-big-five-european-soccer-leagues-1996-2021_csv.csv", index_col=0)
print(data.head())

print(data.isnull().sum())

print(data.columns)

Top_3 = data.drop(['Italy', 'France'], axis='columns')
print(Top_3)

Revenue = Top_3.loc[["19/20**"]]
print(Revenue)

Country = ('England', 'Spain', 'Germany',)
y_pos = np.arange(len(Country))
GMV = [4900, 3100, 3300]

plt.bar(y_pos, GMV, align='center', alpha=0.5, color='r')
plt.xticks(y_pos, Country)
plt.ylabel('GMV in million Euros')
plt.xlabel('Country')
plt.title('Season 2019/2020 TV Revenue')
plt.show()
fig.savefig("Top_3_Revenue.png")



