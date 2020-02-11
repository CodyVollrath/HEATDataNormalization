from controller.WorkBookWriter import WorkBookWriter as WorkbookWriter
class WriteTicketsToXlsx:

    def __init__(self, workbookName, tickets,sheetname = "sheet1"):
        self.__workbookName = workbookName
        self.__sheetname = sheetname
        self.__tickets = tickets
        self.__wbw = WorkbookWriter(self.__workbookName, self.__sheetname)
        self.__headers = ["Incident", "Customer", "Status", "Created On", "Resolved Date Time", "Closed", "Team",
                          "Service", "First Call Resolution"]

    def generateIncedentReport(self):
        self.__writeHeadersForIncedents()
        self.__writeIncidentsToExcel()
    def __writeIncidentsToExcel(self):
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

    def __writeHeadersForIncedents(self):
        col = 0
        for header in self.__headers:
            self.__wbw.writeToColumn(col,header)
            col += 1