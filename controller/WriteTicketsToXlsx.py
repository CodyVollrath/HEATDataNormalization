from controller.WorkBookWriter import WorkBookWriter as WorkbookWriter
from model.Incident import Incident
import controller.fileHandler as fileHandler
from model.Service_Request import Service_Request
class WriteTicketsToXlsx:

    def __init__(self, workbookName, tickets):
        self.__workbookName = workbookName
        self.__tickets = tickets

        self.__incidentHeaders = ["Incident", "Customer", "Status", "Created On", "Resolved Date Time", "Closed", "Team",
                          "Service", "First Call Resolution"]
        self.__serviceRequestHeaders = ["Service Request", "Status", "Owner Team", "Owner", "Created On", "Resolved on"]

        self.__serviceRequestAnalytics = ["ServIT First Call Service Requests", "ServIT Closed SRs",
                                          "SW Closed SRs", "Telco Closed SRs", "PC Management SRs",
                                          "Infrastructure Security SRs", "Infrastructure Support & Connectivity SRs",
                                          "SAP/BI SRs", "SAP Security SRs", "Total SRs Closed"]
    def generateReports(self):
        try:
            if isinstance(self.__tickets[0], Incident):
                self.generateIncedentReport()
            else:
                self.generateServiceReports()
            return False
        except Exception as e:
            print(fileHandler.writeErrorToLog(e))
            return True

    def generateIncedentReport(self):
        self.__wbw = WorkbookWriter(self.__workbookName, "Incidents")
        self.__writeIncidentRecord()
        self.__wbw.close()

    def generateServiceReports(self):
        self.__wbw = WorkbookWriter(self.__workbookName, "ServiceReqs")
        self.__writeServiceReqsToExcel()
        self.__writeAnalyticsSR()
        self.__wbw.close()

    def __writeIncidentRecord(self):
        self.__wbw.writeToRow(0, self.__incidentHeaders)
        row = 1
        for ticket in self.__tickets:
            self.__wbw.writeToCell(row, 0, ticket.getIncidentNumber())
            self.__wbw.writeToCell(row, 1, ticket.getCreator())
            self.__wbw.writeToCell(row, 2, ticket.getStatus())
            self.__wbw.writeToCell(row, 3, self.__removeTime(ticket.getCreatedDateTime()))
            self.__wbw.writeToCell(row, 4, self.__removeTime(ticket.getResolveDateTime()))
            self.__wbw.writeToCell(row, 5, ticket.getOwner())
            self.__wbw.writeToCell(row, 6, ticket.getOwnerTeam())
            self.__wbw.writeToCell(row, 7, ticket.getService())
            self.__wbw.writeToCell(row, 8, ticket.getFirstCallResolve())
            row += 1

    def __writeServiceReqsToExcel(self):
        self.__wbw.writeToRow(0, self.__serviceRequestHeaders)
        row = 1

        for ticket in self.__tickets:
            resolveDate = ticket.getResolveDateTime()
            self.__wbw.writeToCell(row, 0, ticket.getServiceReqNumber())
            self.__wbw.writeToCell(row, 1, ticket.getStatus())
            self.__wbw.writeToCell(row, 2, ticket.getOwnerTeam())
            self.__wbw.writeToCell(row, 3, ticket.getOwner())
            self.__wbw.writeToCell(row, 4, self.__removeTime(resolveDate))
            self.__wbw.writeToCell(row, 5, self.__removeTime(resolveDate))
            row += 1

    def __writeAnalyticsSR(self):
        self.__wbw.addSheetName("SRAnalytics")
        self.__wbw.writeToRow(0, self.__serviceRequestAnalytics)
        self.__wbw.writeToCell(1, 1, self.__tickets.getNumberOfServReqClose())
        # self.__wbw.writeToCell(1, 9, self.__tickets.getNumberOfServReqClose())

    def __removeTime(self, dateTime):
        if " | " in dateTime:
            return dateTime.split(" | ")[0]
        else:
            return dateTime