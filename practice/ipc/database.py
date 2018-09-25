# encoding=utf8
import pymssql

conn = pymssql.connect('172.18.80.182', 'sa', 'sa', 'amis-csc')
cursor = conn.cursor()

sql = "select * from "
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print("Error")

conn.close()
