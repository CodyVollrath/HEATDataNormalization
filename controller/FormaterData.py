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
def getCurrentDate(time=False):
    currentDate = datetime.datetime.now()
    if time:
        formatedTime = "{year}{month}{day}_{hour}{minute}{second}".format(year=currentDate.year, month=currentDate.month, day=currentDate.day,
                                                                          hour=currentDate.hour ,minute=currentDate.minute, second=currentDate.second)
    else:
        formatedTime = "{year}{month}{day}".format(year=currentDate.year, month=currentDate.month,
                                                                          day=currentDate.day)
    return formatedTime
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
    min = int(str(minDate.getYear() + minDate.getMonth() + minDate.getDay() +  minDate.getHour() + minDate.getMinute() + minDate.getSecond()))
    max = int(str(maxDate.getYear() + maxDate.getMonth() + maxDate.getDay() + maxDate.getHour() + maxDate.getMinute() + maxDate.getSecond()))
    if min > max:
        raise ValueError("minDate must not be greater than maxDate")

    curr = int(str(currentDate.getYear() + currentDate.getMonth() + currentDate.getDay() + currentDate.getHour() + currentDate.getMinute() + currentDate.getSecond()))
    if (min - curr) <= 0 and (max - curr) >= 0 :
        return True
    else:
        return False

def isDateLessThanOrEqualTo(date1, date2):
    date1 = dto(date1)
    date2 = dto(date2)
    firstDate = int(str(date1.getYear() + date1.getMonth() + date1.getDay() + date1.getHour() + date1.getMinute() + date1.getSecond()))
    secondDate = int(str(date2.getYear() + date2.getMonth() + date2.getDay() + date2.getHour() + date2.getMinute() + date2.getSecond()))
    return firstDate <= secondDate