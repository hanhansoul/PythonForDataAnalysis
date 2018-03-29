import numpy as np
import pandas as pd

# cut()

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)         # 返回ages列表中每个元素所属区间Categories对象的列表
print(cats.codes)   # 返回ages列表中每个元素所属区间排序位置的列表
print(cats.categories)  # 返回排序后的区间Categories对象的列表
print(pd.value_counts(cats))    # 返回各区间中元素的个数

# 指定区间名
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)

data = np.random.rand(20)
res = pd.cut(data, 4, precision=2)
print(pd.value_counts(res))

# qcut()
data = np.random.randn(1000)
# qcut()采用采样方式划分区间，基本做到平均分布
cats = pd.qcut(data, 4)
