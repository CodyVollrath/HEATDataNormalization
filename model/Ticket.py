class Ticket:
    def __init__(self, subject, createdDateTime, incidentNumber, status, typeData):
        self.__subject = subject
        self.__createdDateTime = createdDateTime
        self.__incidentNumber = incidentNumber
        self.__status = status
        self.__typeData = typeData

    def getSubject(self):
        return self.__subject

    def getCreatedDateTime(self):
        return self.__createdDateTime
    def getIncidentNumber(self):
        return self.__incidentNumber

    def getStatus(self):
        return self.__status
    
    def getTypeData(self):
        return self.__status