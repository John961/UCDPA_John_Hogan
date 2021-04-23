import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

combined_countries = [
                         {"Country": "England", "GMV": 4900, "Goals_Scored": 1072},
                         {"Country": "Spain", "GMV": 3100, "Goals_Scored": 1047},
                         {"Country": "Germany", "GMV": 3300, "Goals_Scored": 973}
                         ]
print(combined_countries)

top3merged = pd.DataFrame(combined_countries)
print(top3merged)

sns.catplot(x="GMV",data=top3merged, kind="count")
plt.show()

sns.scatterplot(x="GMV", y="Goals_Scored",data=top3merged, hue="Country")
plt.xlim([2500, 5500])
plt.ylim([800, 1200])
sns.set_style("darkgrid")
plt.show()
fig.savefig("Top_3_Revenue.svg")

def Johns_Function
    print(sns.scatterplot(x="GMV", y="Goals_Scored",data=top3merged, hue="Country")
plt.xlim([2500, 5500])
plt.ylim([800, 1200])
plt.show())





