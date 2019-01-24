import matplotlib

matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
    # <---INSERT YOUR CODE HERE--->
    array = np.empty([iterations, sample_size])
    mean = np.empty([iterations, 1])

    for i in range(iterations):
        array[i] = np.random.choice(sample, size=sample_size)
        mean[i] = np.mean(array[i])

    data_mean = np.mean(mean)
    lower = np.percentile(mean, 2.5)
    upper = np.percentile(mean, 97.5)
    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    i = 10000
    data_current = df.values.T[0]
    boot = boostrap(data_current, data_current.shape[0], i)
    print("Current Fleet:")
    print(boot)


    data_new = df.values.T[1]
    data_new = data_new[~np.isnan(data_new)]
    boot = boostrap(data_new, data_new.shape[0], i)
    print("New Fleet")
    print(boot)

#print(("Mean: %f")%(np.mean(df))
#print(("Var: %f")%(np.var(df))
