import re
import datetime
class DateTimeObj:
    def __init__(self, dateTimeString):
        self.__fulldate = dateTimeString[:dateTimeString.index(" ")]
        self.__fulltime = self.__convertTimeToMilitary(dateTimeString[dateTimeString.rindex(" ")+1:])
        self.__year = self.__fulldate[self.__fulldate.rindex("/")+1:]
        self.__month = self.__fulldate[:self.__fulldate.index("/")]
        self.__day = self.__fulldate[self.__fulldate.index("/")+1:self.__fulldate.rindex("/")]

        self.__hour = self.__fulltime[:2]
        self.__minute = self.__fulltime[3:5]
        self.__second = self.__fulltime[-2:]
    def getDate(self):
        return self.__fulldate

    def getTime(self):
        return self.__fulltime

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def getDay(self):
        return self.__day

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def __convertTimeToMilitary(self, timeString):
        if timeString[-2:] == "AM" and timeString[:2] == "12":
            return "00" + timeString[2:-2]
        elif timeString[-2:] == "AM":
            return timeString[:-2]
        elif timeString[-2:] == "PM" and timeString[:2] == "12":
            return timeString[:-2]
        else:
            return str(int(timeString[:2]) + 12) + timeString[2:8]
