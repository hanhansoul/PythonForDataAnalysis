import ibm_db

conn_string = "DATABASE=Ifr;HOSTNAME=172.18.8.117;PORT=50000;UID=AMASISFULL;PWD=AMASISFULL;"

conn = None

try:
    ibm_db.connect(conn_string, "", "")
except Exception as ex:
    print(ex)

if conn:
    print('success')
else:
    print('failure')
