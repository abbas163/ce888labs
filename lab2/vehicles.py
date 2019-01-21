import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
sns.set(style="whitegrid")

df  = pd.read_csv('./vehicles.csv')

sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
plt.show()

from matplotlib import pyplot as plt
sns_plot  = pd.read_csv('./vehicles.csv')

sb.distplot(sns_plot['Current fleet'],bins=20 ,kde = False)

plt.show()
sb.distplot(sns_plot['New Fleet'],bins=20 ,kde = False)

plt.show()