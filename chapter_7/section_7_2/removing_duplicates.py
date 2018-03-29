import pandas as pd
import numpy as np

# 去重

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
data.duplicated()  # 只检查相邻两行是否重复
data.drop_duplicates()  # 只去除相邻两行的重复行

data['v1'] = range(7)
data.drop_duplicates(['k1'])  # 指定需要去重的列

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])

