import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
sns.set(style="whitegrid")

df  = pd.read_csv('./vehicles.csv')

sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
plt.show()

sb.distplot(sns_plot['Current fleet'],bins=30 ,kde = False)
sns_plot.savefig("Histogram-Currentfleet.pdf",bbox_inches='tight')
plt.show()



sb.distplot(sns_plot['New Fleet'],bins=30 ,kde = False)
sns_plot.savefig("Histogram-Newfleet.pdf",bbox_inches='tight')
plt.show()