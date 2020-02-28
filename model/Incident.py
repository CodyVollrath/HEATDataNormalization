from model.Ticket import Ticket
class Incident(Ticket):
    def __init__(self, subject, creator, owner, ownerEmail, ownerTeam, service, createdDateTime, resolveDate, incidentNumber,
                 status, typeData):
        Ticket.__init__(self, subject, creator,owner,ownerEmail,ownerTeam, service, createdDateTime, resolveDate, status, typeData)
        self.__incidentNumber = incidentNumber
    def getIncidentNumber(self):
        return self.__incidentNumber

    def toString(self):
        delimiter = " | "
        return Ticket.toString() + delimiter + self.__incidentNumber