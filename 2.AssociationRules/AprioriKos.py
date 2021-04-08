import time
import numpy as np
import pandas as pd
import csdnfptree as fp
import Apriori_Algorithm_for_Generating_Frequent_Itemsets as Apr
import os
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
# Apr.apriori(createDataset('data/test.dat'), 0.02)
#print "数据集D:\n", D
#print "所有候选1项集C1:\n", C1
#L1, supportData0 = scanD(D, C1, 0.0025)
#print '符合最小支持度的频繁1项集L1:\n', L1
#L, suppData = apriori(dataSet)
#print "所有符合最小支持度0.029的项集L：\n", L
#print "频繁2项集：\n", aprioriGen(L[0], 2)
#L, suppData = apriori(dataSet, minSupport=0.7)
#print "所有符合最小支持度为0.7的项集L：\n", L

L, suppData = Apr.apriori(dataSet, minSupport=0.04)

print(L)
try:
    da = open('aprioriKos.txt',"a")
except:
    print("Error")

da.write(str(L))

rules = Apr.generateRules(L, suppData, minConf=0.7)
print(rules)
end =time.perf_counter()
print("程序运行时间为：",end,"s")