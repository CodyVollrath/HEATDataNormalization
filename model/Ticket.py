class Ticket:
    def __init__(self, subject, creator, owner, ownerEmail, ownerTeam, service, createdDateTime, resolveDate, status, typeData):
        self.__subject = subject
        self.__creator = creator
        self.__owner = owner
        self.__ownerEmail = ownerEmail
        self.__ownerTeam = ownerTeam
        self.__service = service
        self.__createdDateTime = createdDateTime
        self.__resolvedDate = resolveDate
        self.__status = status
        self.__typeData = typeData
    def getSubject(self):
        return self.__subject

    def getCreator(self):
        self.__creator

    def getOwner(self):
        return self.__owner

    def getOwnerEmail(self):
        return self.__ownerEmail

    def getOwnerTeam(self):
        return self.__ownerTeam
    def getService(self):
        return self.__service
    def getCreatedDateTime(self):
        return self.__createdDateTime

    def getResolveDateTime(self):
        return self.__resolvedDate

    def getStatus(self):
        return self.__status

    def getTypeData(self):
        return self.__status