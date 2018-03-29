import pandas as pd
import numpy as np


def output(d):
    for k, v in d:
        print(k)
        print(v)


people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

g1 = people.groupby(['a'])
output(g1)

g2 = people.groupby(len)
output(g2)
