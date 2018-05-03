import pandas as pd

"""
MovieLens 1M Dataset
"""
basedir = "E:/development/PythonForDataAnalysis/chapter_14/section_14_2/"

basedir = ""

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(basedir + 'data/users.dat', sep='::', header=None, names=unames,
                      engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(basedir + 'data/ratings.dat', sep='::', header=None,
                        names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(basedir + 'data/movies.dat', sep='::', header=None, names=mnames,
                       engine='python')

data = pd.merge(pd.merge(ratings, users), movies)

print(data.iloc[0])

data.groupby(['movie_id', 'gender'])['rating'].mean()

# 对于每一部电影，对于不同性别群体的评分的平均值
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean', margins=True)

# 对于每一部电影，参与评分的总人数
data.groupby('title')['gender'].size()

# 对于每一部电影，参与评分的不同性别群体的人数
data.pivot_table('rating', index='title', columns='gender', aggfunc='count', margins=True)
# 或
data.groupby(['title', 'gender']).size().unstack()

# 参与每部电影评分的总人数
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]
# 评分人数超过250人的电影
ratings_by_title[ratings_by_title >= 250]
active_titles = ratings_by_title.index[ratings_by_title >= 250]  # 仅保留index内容
# 仅保留评分人数超过250人的电影的评分平均值
mean_ratings = mean_ratings.loc[active_titles]
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

# Measuring Rating Disagreement
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])
# 男女评分差距最大，且在男性中最受欢迎的电影
print(sorted_by_diff[::-1][:10])

# 评分的标准差最大的电影
ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.loc[active_titles]
ratings_std_by_title.sort_values(ascending=False)[:10]
