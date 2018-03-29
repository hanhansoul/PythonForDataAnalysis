from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day)

# Datetime和String格式转换

stamp = datetime(2011, 1, 3)
str(stamp)
stamp.strftime('%Y-%m-%d')

value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')
