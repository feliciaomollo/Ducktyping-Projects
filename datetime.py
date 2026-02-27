#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)

#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))




from datetime import date


print(date.today())


