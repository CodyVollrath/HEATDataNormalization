
import controller.write as write
from controller.WriteTicketsToXlsx import WriteTicketsToXlsx as ticketWriter
class Ticket_Library:
    def __init__(self):
        self.__tickets = []
        self.numberOfIncidents = 0
        self.numberOfIncidentsClosed = 0
        self.numberOfIncidentsOpened = 0
    def add(self, ticket):
        if ticket == None:
            raise ValueError("ticket can not be none")
        prevLength = len(self.__tickets)
        self.__tickets.append(ticket)
        return len(self.__tickets) > prevLength
    def length(self):
        return len(self.__tickets)
    def getTicekts(self):
        return self.__tickets
    def generateReports(self, filename, sheetname = "Sheet1"):
        report = ticketWriter(filename,self.__tickets, sheetname = sheetname)
        report.generateIncedentReport()
    def writeTicketToFile(self, filename):
        output = ""
        for each in self.__tickets:
            try:
                output += str(each.toString()) + "\n"
            except:
                output += ""
        return write.writeToFile(filename, output)
    def findTicketsDateRange(self, minDate, maxDate, type):
        """
        Finds the tickets within the date range specfied by min and max date params and gets the number of what ever
        type was entered (inclusive)
        :param minDate: the start date to search for the number of tickets. Format('MM/DD/YYYY | HH:MM(PM/AM)') <-
        not including ' ()' for HH:MM (PM/AM)
        :param maxDate: the end date to search for tickets
        :param type: the type of ticket to search for (IE. Incidents, serviceReqs, etc)
        :return: The number of tickets by type of the search parameters
        """
        count = 0
        for each in self.__tickets:
            if each.getTypeData() == "Incident":
                count += 1
    def getNumberIncidentsSinceyesterday(self):
        pass
    def getNumberIncidentsSinceOneWeekAgo(self):

        pass
    def getNumberIncidentsSinceOneMonthAgo(self):
        pass
    def getNumberOfIncidentsResolved(self):
        pass