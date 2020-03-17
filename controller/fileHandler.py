import controller.FormaterData as Date
def writeErrorToLog(error):
    error =  Date.getCurrentDate(time=True) + ": " + str(error) + "\n"
    errorLog = open("../files/errors.log", 'a+')
    errorLog.write(error)
    return error

def getSessionId():
    file = open("../files/sessionId.key", 'r')
    return file.readline()

