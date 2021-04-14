import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
f = pd.read_csv('world-happiness-report-2021.csv')
CityName = f['Country name'].values

retData = f.iloc[:,1:]

def km(n):
    '''

    :param n:
    :return:
    '''
    lab = []
    km = KMeans(n_clusters=n)
    label = km.fit_predict(retData)
    expenses = np.sum(km.cluster_centers_,axis=1)
    for i in range(n):
        eptlists = []
        lab.append(eptlists)
    for i in range(len(CityName)):
        lab[label[i]].append(CityName[i])
    for i in range(len(lab)):
        print("Expenses:%.2f" % expenses[i])
        print(lab[i])

km(3)
