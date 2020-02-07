class Ticket:
    def __init__(self, subject,owner,ownerEmail,ownerTeam, createdDateTime,incidentNumber,status, typeData):
        self.__subject = subject
        self.__owner = owner
        self.__ownerEmail = ownerEmail
        self.__ownerTeam = ownerTeam
        self.__createdDateTime = createdDateTime
        self.__incidentNumber = incidentNumber
        self.__status = status
        self.__typeData = typeData

    def getSubject(self):
        return self.__subject

    def getOwner(self):
        return self.__owner

    def getOwnerEmail(self):
        return self.__ownerEmail
        
    def getOwnerTeam(self):
        return self.__ownerTeam

    def getCreatedDateTime(self):
        return self.__createdDateTime

    def getIncidentNumber(self):
        return self.__incidentNumber

    def getStatus(self):
        return self.__status
    
    def getTypeData(self):
        return self.__status

    def toString(self):
        delimiter = " | "
        return self.getSubject() + delimiter + self.getOwner() + delimiter + self.getOwnerEmail() + delimiter + self.getOwnerTeam() + delimiter + self.getCreatedDateTime() + delimiter + self.getIncidentNumber() + delimiter + self.getStatus() + delimiter + self.getTypeData()