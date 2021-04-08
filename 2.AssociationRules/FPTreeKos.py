import time
import numpy as np
import pandas as pd

import csdnfptree as fp
import os
os.chdir(r'F:\Data-Mining-Access\2.AssociationRules')
print("Starting......")
def createDataset(fileName):
    with open(fileName, 'r') as fr:
        read_line = fr.readlines()
        support =[]
        for line in read_line:
            line = line.strip()
            splitLine = str(line).split(' ')
            m =len(splitLine)
            data_Mat = np.zeros((1,m))
            data_Mat[:]=splitLine[:]
            support.append(data_Mat[0,: ])
    fr.close()
    return support

start =  time.perf_counter()
dataSet = createDataset('data/kosarak.dat')
print(dataSet)

fptree = fp.FP_Tree(minsup=0.04)
fptree.get_frequent_k_itemsets((dataSet))

fp.print_all_frequent_k_itemsets(fptree.frequent_k_itemsets, fptree.frequent_k_itemsets_sup)
print("打印最大项......")
fp.print_max_frequent_k_itemsets(fptree.frequent_k_itemsets, fptree.frequent_k_itemsets_sup)


# L, suppData = Apr.apriori(dataSet, minSupport=0.04)
#
# print(L)
# try:
#     da = open('aprioriKos.txt',"a")
# except:
#     print("Error")
#
# da.write(str(L))
#
# rules = Apr.generateRules(L, suppData, minConf=0.7)
# print(rules)
end =time.perf_counter()
print("程序运行时间为：",end,"s")
