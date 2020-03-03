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
        self.sheet = self.out_wb.add_worksheet(sheetName)

    """
    Writes data to a column or row dpending on what is entered for the and allows for the checking of
    a condition prior the writing of that value. By default it is set to True
    
    :param col the column
    :param data the data that is to be added
    :param condition a boolean that should be checked before the addition of a cell is added to that row. Use in case of
        spefic usecase. Default it is set to true
    :precondition nothing entered can be None
    :postcondition a worksheet will be created with the specified name and data entered into provided the condition
    entered in it allows for it.
    """
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
