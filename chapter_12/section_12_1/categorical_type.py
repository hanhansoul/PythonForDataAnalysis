import pandas as pd
import numpy as np

"""
Categorical基于整数或编码保存数据
"""

fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
df = pd.DataFrame({
    'fruit': fruits,
    'basket_id': np.arange(N),
    'count': np.random.randint(3, 15, size=N),
    'weight': np.random.uniform(0, 4, size=N)},
    columns=['basket_id', 'fruit', 'count', 'weight'])
fruit_cat = df['fruit'].astype('category')
c = fruit_cat.values
print(c.categories)
print(c.codes)

df['fruit'] = df['fruit'].astype('category')
my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])

# pd.Categorical.from_codes
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
ordered_cat = pd.Categorical.from_codes(codes, categories, ordered=True)
my_cats_2.as_ordered()
