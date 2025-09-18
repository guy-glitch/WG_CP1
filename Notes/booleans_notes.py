#WG_1st_Booleans_Notes
#base
import time
#time is a python library
current_time = time.time()
readable_time = time.ctime(current_time)
print(f"{current_time} seconds since January 1, 1970(epoch)")
print(f"Today is {readable_time}")
import datetime as date
#datetime is easeir to use for specific information
newcurrent_time = date.datetime.now()
newreadable_time = time.ctime(current_time)
print(newcurrent_time)
hour = newcurrent_time.strftime("%H")
print(f"The hour is {hour}")
#minutes = %M
#weekday = %A
#day = %d
#month = %B
#month num = %m
#year = %Y
#seconds = %S
print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an string: {isinstance(hour, str)}")






