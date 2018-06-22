import pymssql

conn = pymssql.connect(host='172.18.8.241', port=1433, user='sa', password='Scaljw@2016', database='AMIS-CSC')

sql = "select ac, act from reg where ac not in ('BXXXXX', 'B-XXXX')"

cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()

cursor.executemany("insert into FlightRestrictionInfoList (ac, act) values (%s, %s)", res)
conn.commit()

# row = cursor.fetchone()
# while row:
#     print(row[0], row[1])
#     row = cursor.fetchone()

conn.close()
