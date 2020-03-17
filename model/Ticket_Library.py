
class Ticket_Library:
    def __init__(self):
        self.__tickets = []

        self.__numberOfIncidents = 0
        self.__numberOfServiceReq = 0

        self.__numberOfIncidentsClosed = 0
        self.__numberOfIncidentsOpened = 0

        self.__numberOfServiceReqClosed = 0
        self.__numberOfServiceReqOpen = 0

    def add(self, ticket):
        if ticket == None:
            raise ValueError("ticket can not be none")
        prevLength = len(self.__tickets)
        self.__addToIncidentOrServiceReq(ticket)
        self.__tickets.append(ticket)
        return len(self.__tickets) > prevLength

    def __addToIncidentOrServiceReq(self, ticket):
        if ticket.getTypeData() == "Incident":
            self.__numberOfIncidents += 1
            if ticket.getStatus() == "Closed":
                self.__numberOfIncidentsClosed += 1
            else:
                self.__numberOfIncidentsOpened += 1
        else:
            self.__numberOfServiceReq += 1
            if ticket.getStatus() == "Closed":
                self.__numberOfServiceReqClosed += 1
            else:
                self.__numberOfServiceReqOpen += 1

    def length(self):
        return len(self.__tickets)

    def getTickets(self):
        return self.__tickets

    def generateReports(self, filename):
        report = ticketWriter(filename, self.__tickets)
        try:
            report.generateReports()
        except:
            self.writeTicketToFile("../files/" + self.__tickets[0].getTypeData() + ".txt")

    def writeTicketToFile(self, filename):
        file = open(filename, 'w+')
        output = ""
        for each in self.__tickets:
            try:
                output += str(each.toString()) + "\n"
            except:
                output += ""
        file.write(output)
        file.close()
    '''
    Analytic Tools for keeping track of the numbers
    '''
    def getNumberOfIncidentsClosed(self):
        return self.__numberOfIncidentsClosed

    def getNumberOfIncidentsOpen(self):
        return self.__numberOfIncidentsOpened

    def getNumberOfServReqClose(self):
        return self.__numberOfServiceReqClosed

    def getNumberOfServReqOpen(self):
        return self.__numberOfServiceReqOpen

    def getTotalIncidents(self):
        return self.__numberOfIncidents

    def getTotalServReq(self):
        return self.__numberOfServiceReq