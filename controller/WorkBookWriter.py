import xlsxwriter

class WorkBookWriter:

    def  __init__(self, outputFile,sheetName):
        if outputFile is None:
            raise ValueError("outputFile must not be 'None'")
        if ".xlsx" not in outputFile:
            raise ValueError("outputFile must be a valid excel file")
        if sheetName is None:
            raise ValueError("sheetName must not be 'None'")
        self.out_wb = xlsxwriter.Workbook(outputFile)
        self.sheet = {}
        self.sheet = self.out_wb.add_worksheet(sheetName)
        self.__sheetName = self.sheet.get_name()

    def writeToColumn(self, col, data):
        if col < 0:
            raise ValueError("col must not be less than zero")
        if data is None:
            data = ""
        row = 0
        for item in data:
            self.sheet.write(row, col, item)
            row += 1

    def writeToRow(self,row, data):
        if row < 0:
            raise ValueError("row must not be less than zero")

        if data is None:
            data = ""
        col = 0
        for item in data:
            self.sheet.write(row, col, item)
            col += 1

    def writeToCell(self, row , col, item):
        if row < 0:
            raise ValueError("col must not be less than zero")
        if col < 0:
            raise ValueError("col must not be less than zero")
        if item is None:
            item = ""
        self.sheet.write(row, col, item)

    def addSheetName(self, sheetName):
        self.sheet = self.out_wb.add_worksheet(sheetName)

    def close(self):
        self.out_wb.close()
