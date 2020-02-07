import re
def formatDateTime(dateTime):
    if not re.match("\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z",dateTime):
        raise ValueError("dateTime format does not match format specification YYYY-MM-DDTHH:MM:SSZ")
    date = dateTime[:dateTime.index("T")] 
    time = dateTime[dateTime.index("T")+1:dateTime.index("Z")]
    arrangedDate = __dateArrange(date)
    standardTime = __timeConvert(time)
    return arrangedDate + " _ " + standardTime

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