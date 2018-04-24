import pandas as pd

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('D:/Workspace/PythonForDataAnalysis/data/ml-1m/users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('D:/Workspace/PythonForDataAnalysis/data/ml-1m/ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movies_id', 'title', 'genres']
movies = pd.read_table('D:/Workspace/PythonForDataAnalysis/data/ml-1m/movies.dat', sep='::', header=None, names=mnames, engine='python')
