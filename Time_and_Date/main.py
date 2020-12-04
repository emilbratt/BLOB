#!/usr/bin/env python3
import calendar
from datetime import datetime







def getDate():
    return datetime.now().strftime("%Y-%m-%d")
def getWeekNumber():
    return datetime.now().strftime("%V")
def getMonth():
    nameMonths = [
    'January','February','Mach',
    'Arpil','May','June',
    'July','August','September',
    'October','November','December'
    ]
    m = datetime.now().strftime("%m")
    return nameMonths[int(m)-1]



def getWeekDay():
    date = datetime.now().strftime("%Y%m%d")
    nameDays=[
    'Monday','Tuesday','Wednesday','Thursday',
    'Friday','Saturday','Sunday'
    ]
    try: # if from datetime import datetime
        dayNumber = calendar.weekday(
            int(date[0:4]),
            int(date[4:6]),
            int(date[6:8]))
    except TypeError: # if import datetime
        dayNumber = date.weekday()
    return nameDays[dayNumber]


print('date: '+getDate())
print('weeknumber: '+getWeekNumber())
print('month name: '+getMonth())
print('weekday: '+getWeekDay())
exit()
