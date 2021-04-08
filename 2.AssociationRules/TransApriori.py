import time
import pandas as pd
import numpy as np
# 先读取对应的Excel文件，把2进制的数据处理成数据清单列表
import Apriori_Algorithm_for_Generating_Frequent_Itemsets as Apr


f = pd.read_excel('data/Transactions.xls')
a = f
Lister = []
# print(a.columns)
for i in a.index:
    lister = []
    b = a.loc[i].values
    for j in range(len(b)):
        if b[j] == 1:
            lister.append(a.columns[j])
    Lister.append(lister)
dataSet = Lister

start =  time.perf_counter()
L, suppData = Apr.apriori(dataSet, minSupport=0.04)
print(L)
try:
    da = open('aprioriTrans.txt',"a")
except:
    print("Error")
da.write(str(L))
rules = Apr.generateRules(L, suppData, minConf=0.7)
print(rules)
end =time.perf_counter()
print("程序运行时间为：",end,"s")