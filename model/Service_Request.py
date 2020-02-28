from model.Ticket import Ticket
class Service_Request(Ticket):
    def __init__(self, subject, creator, owner,ownerEmail, ownerTeam, service, createdDateTime, resolveDate, serviceRequestNumber, status, typeData):
        Ticket.__init__(self, subject, creator, owner, ownerEmail, ownerTeam, service, createdDateTime, resolveDate, status, typeData)
        self.__serviceReqNumber = serviceRequestNumber

    def getServiceReqNumber(self):
        return self.__serviceReqNumber
    
    def toString(self):
        delimiter = " | "
        return Ticket.toString() + delimiter + self.__serviceReqNumber