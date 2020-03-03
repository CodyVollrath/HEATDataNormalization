from controller.WorkBookWriter import WorkBookWriter as WorkbookWriter
from model.Incident import Incident
from model.Service_Request import Service_Request
class WriteTicketsToXlsx:

    def __init__(self, workbookName, tickets, sheetname = "IncidentTotal"):
        self.__workbookName = workbookName
        self.__sheetname = sheetname
        self.__tickets = tickets
        self.__wbw = WorkbookWriter(self.__workbookName, self.__sheetname)
        self.__incidentHeaders = ["Incident", "Customer", "Status", "Created On", "Resolved Date Time", "Closed", "Team",
                          "Service", "First Call Resolution"]
        self.__serviceRequestHeaders = ["Service Request", "Status", "Owner Team", "Owner", "Created On", "Resolved on"]

    def generateReports(self):
        try:
            if isinstance(self.__tickets[0], Incident):
                self.generateIncedentReport()
            else:
                self.generateServiceReports()
            return False
        except:
                return True


    def generateIncedentReport(self):
        self.__writeHeadersForIncedents()
        self.__writeIncidentsToExcel()

    def generateServiceReports(self):
        self.__writeHeadersForServiceReqs()
        self.__writeServiceReqsToExcel()

    def __writeIncidentsToExcel(self):
        self.__writeIncidentRecord()
        self.__writeServiceReqsToExcel()
        self.__wbw.close()

    def __writeIncidentRecord(self):
        row = 1
        for ticket in self.__tickets:
            self.__wbw.writeToCell(row, 0, ticket.getIncidentNumber())
            self.__wbw.writeToCell(row, 1, ticket.getCreator())
            self.__wbw.writeToCell(row, 2, ticket.getStatus())
            self.__wbw.writeToCell(row, 3, ticket.getCreatedDateTime())
            self.__wbw.writeToCell(row, 4, ticket.getResolveDateTime())
            self.__wbw.writeToCell(row, 5, ticket.getOwner())
            self.__wbw.writeToCell(row, 6, ticket.getOwner())
            self.__wbw.writeToCell(row, 7, ticket.getOwnerTeam())
            self.__wbw.writeToCell(row, 8, ticket.getService())
            row += 1
        self.__wbw.close()

    def __writeServiceReqsToExcel(self):
        row = 1
        for ticket in self.__tickets:
            self.__wbw.writeToCell(row, 0, ticket.getServiceReqNumber())
            self.__wbw.writeToCell(row, 1, ticket.getStatus())
            self.__wbw.writeToCell(row, 2, ticket.getOwnerTeam())
            self.__wbw.writeToCell(row, 3, ticket.getOwner())
            self.__wbw.writeToCell(row, 4, ticket.getCreatedDateTime())
            self.__wbw.writeToCell(row, 5, ticket.getResolveDateTime())
            row += 1
        self.__wbw.close()

    def __writeHeadersForIncedents(self):
        self.__wbw.writeToRow(0, self.__incidentHeaders)

    def __writeHeadersForServiceReqs(self):
        self.__wbw.addSheetName("ServiceReqTotal")
        self.__wbw.writeToRow(0, self.__serviceRequestHeaders)