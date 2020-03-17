from model.heat_requests import heat_requests
import controller.FormaterData as date
import controller.fileHandler as fileHandler
from controller.WriteTicketsToXlsx import WriteTicketsToXlsx as ticketWriter
class Main:
    def __init__(self):
        print("Logging in")
        self.heat = heat_requests()
        self.sessionKeyFile = fileHandler.getSessionId()
    def __getLoginTenantInfo(self):
        tenant = []
        try:
            file = open("../files/tenantLogin.csv", "r")
            tenant = file.readline().rsplit('|')
        except:
            print("File not found")
        return tenant

    def __generateIncidents(self, dateToStop):
        isValid = False
        print("Loading tickets from HEAT")
        isValid = self.heat.getBusinessObjectsByURLFilter("https://southwire.saasit.com/api/odata/businessobject/incidents?$orderby=CreatedDateTime desc", dateToStop)
        self.heat.getTickets().generateReports("../files/Incidents_" + date.getCurrentDate() + ".xlsx") #<----- Generate Report
        return isValid

    def __generateServiceReq(self, dateToStop):
        isValid = False
        print("Loading tickets from HEAT")
        isValid = self.heat.getBusinessObjectsByURLFilter("https://southwire.saasit.com/api/odata/businessobject/ServiceReqs?$orderby=CreatedDateTime desc", dateToStop)
        self.heat.getTickets().generateReports("../files/serviceRequests_" + date.getCurrentDate() + ".xlsx") #<---- Generate Report
        return

    def __createReport(self):
        ticketLibrary = self.heat.getTickets()
        report = ticketWriter(ticketLibrary)
    def createSession(self):
        headers = self.__getLoginTenantInfo()
        if len(headers) == 5:
            try:
                self.heat = heat_requests(headers[0], headers[1], headers[2], headers[3], headers[4])
                self.sessionKeyFile.write(self.heat.getSessionID())
            except Exception as e:
                print(fileHandler.writeErrorToLog(e))
                exit()
        else:
            raise ValueError("Bad tenant file")

    def getSession(self):
        return self.sessionKeyFile

    def getIncidents(self, dateToStop):
        if not self.__generateIncidents(dateToStop):
            self.createSession()
            self.__generateIncidents(dateToStop)

    def getServiceRequests(self, dateToStop):
        if not self.__generateServiceReq(dateToStop):
            self.createSession()
            self.__generateServiceReq(dateToStop)

if __name__ == "__main__":
    test = Main()
    test.getServiceRequests("03/16/2020 | 03:10:10PM")
    print("Finished")