import re
import datetime
from model.DateTimeObj import DateTimeObj as dto
def formatDateTime(dateTime):
    if dateTime == None:
        return "Not Yet Resolved"

    if not re.match("\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z",dateTime):
        raise ValueError("dateTime format does not match format specification YYYY-MM-DDTHH:MM:SSZ")
    date = dateTime[:dateTime.index("T")]
    time = dateTime[dateTime.index("T")+1:dateTime.index("Z")]
    arrangedDate = __dateArrange(date)
    standardTime = __timeConvert(time)
    return arrangedDate + " | " + standardTime

def __timeConvert(time):
    hours, minutes,seconds = time.split(":")
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    if hours == 0:
        hours = 12
    return ("%02d:%02d:%02d" + setting) % (hours, minutes, seconds)

def __dateArrange(date):
    dateItems = date.split("-")
    year = dateItems[0]
    month = dateItems[1]
    day = dateItems[2]
    return ("%s/%s/%s") % (month,day,year)

def formatNonticketDateFormat(dateTime):
    if not re.match("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+", dateTime):
        raise ValueError("dateTime format does not match format specification YYYY-MM-DD HH:MM:SS.MS+")
    date = __dateArrange(dateTime[:dateTime.index(" ")])
    time = __timeConvert(dateTime[dateTime.index(" ")+1:dateTime.index(".")])
    return date + " | " + time
def testFindDateRange(minDate, maxDate, currentDate):
    """
    test to build function for determing if date is within date range
    must be in mm/dd/yyyy | HH:MM:SS(PM|AM)
    """
    minDate = dto(minDate)
    maxDate = dto(maxDate)
    currentDate = dto(currentDate)
    min = int(str(minDate.getYear() + minDate.getMonth() + minDate.getDay()))
    max = int(str(maxDate.getYear() + maxDate.getMonth() + maxDate.getDay()))
    curr = int(str(currentDate.getYear() + currentDate.getMonth() + currentDate.getDay() ))
    if (min - curr) <= 0 and (max - curr) >= 0 :
        print("Date is within range")
    else:
        print("Date is NOT within Range")


testFindDateRange("02/05/2021 | 10:50:80PM","09/07/2021 | 10:50:80PM","08/10/2021 | 10:50:80PM") #<- Do more testing on this and make sure it works for sure