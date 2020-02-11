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
        return str(self.getSubject()) + delimiter + str(self.getCreator()) + str(delimiter + self.getOwner()) + \
               delimiter + str(self.getOwnerEmail()) + delimiter + str(self.getOwnerTeam()) + delimiter + \
               str(self.getService()) + delimiter + str(self.getCreatedDateTime()) + \
               delimiter + str(self.getIncidentNumber()) + delimiter + str(self.getResolveDateTime()) + delimiter + \
               str(self.getStatus()) + delimiter + str(self.getTypeData())