import pandas as pd
import time
import csdnfptree as fp

## 我们需要对文件进一步处理：需要处理成列表格式以便于后续的算法输入
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

# with open('dealtTransaction.txt','w') as f:
#     f.write(str(Lister))
# print(Lister)
start =  time.perf_counter()
fptree = fp.FP_Tree(minsup=0.04)
fptree.get_frequent_k_itemsets((Lister))

fp.print_all_frequent_k_itemsets(fptree.frequent_k_itemsets, fptree.frequent_k_itemsets_sup)
print("打印最大项......")
fp.print_max_frequent_k_itemsets(fptree.frequent_k_itemsets, fptree.frequent_k_itemsets_sup)
end =time.perf_counter()
print("程序运行时间为：",end,"s")