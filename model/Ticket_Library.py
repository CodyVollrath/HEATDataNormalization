from Ticket import Ticket
import write
class Ticket_Library:
    def __init__(self):
        self.__tickets = []
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
    def writeTicketToFile(self, filename):
        output = ""
        for each in self.__tickets:
            output += each.toString() + "\n"
        return write.writeToFile(filename, output)