import pymssql
import re

conn = pymssql.connect(host='172.18.8.241', port=1433, user='sa', password='Scaljw@2016', database='AMIS-CSC')
cursor = conn.cursor()

i = input()
acTuple = tuple(re.split("\s+|、", input()))
sql = 'update reg set lopaId = ' + str(i) + ' where ac in %s'
print(sql % "{}".format(acTuple))
res = cursor.execute(sql % "{}".format(acTuple))
conn.commit()
conn.close()
