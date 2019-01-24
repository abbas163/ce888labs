import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
sns.set(style="whitegrid")


df  = pd.read_csv('./vehicles.csv')
sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
#sns_plot.set_title("Scaterplot for Current  and New Fleet")
sns_plot.savefig("Scaterplot.pdf",bbox_inches='tight')
plt.show()

cf=df.values.T[0]
plt.clf()
sns_plot2 = sns.distplot(cf, bins=20, kde=False, rug=False, label="Current Fleet")
sns_plot2.set_title("Histogram for Current Fleet")
sns_plot2.set_ylim(0, 50)
sns_plot2.set(xlabel='Current Fleet', ylabel='Frequency')
sns_plot2.get_figure().savefig("Current_Fleet_Histogram.png", bbox_inches='tight')
sns_plot2.get_figure().savefig("Current_Fleet_Histogram.pdf", bbox_inches='tight')

nf=df.values.T[1]
plt.clf()
sns_plot3 = sns.distplot(cf, bins=20, kde=False, rug=True, label="New Fleet")
sns_plot3.set_title("Histogram for New Fleet")
sns_plot3.set_ylim(0, 50)
sns_plot3.set(xlabel='New Fleet', ylabel='Frequency')
sns_plot3.get_figure().savefig("New_Fleet_Histogram.png", bbox_inches='tight')
sns_plot3.get_figure().savefig("New_Fleet_Histogram.pdf", bbox_inches='tight')










