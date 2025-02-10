# import datetime
# print(dir(datetime))
from datetime import datetime
now = datetime.now()
now.strftime("%d/%m/%Y, %H:%M:%S")
newvar = datetime.now(datetime.timetz)
day = now.day
month = now.month
year = now.year
hour = now.hour
min = now.minute
sc = now.second
# print(day,month,year,hour,min,sc)
print(f'{day}/{month}/{year}/{hour}/{min}/{sc}')