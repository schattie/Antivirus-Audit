from pathlib import Path
from openpyxl import load_workbook

class Sophos:
    file_string = None  #file path where excel sheet is stroed
    file_path = None #This is the converted string value to path 
    workstation_workbook = None #point this to path where file is stored
    sheet = None #Should only be one sheet per excel, program auto selects first sheet. Used to manipulate sheet values. Mainly used to delete columns

    def set_file_path(self, file_string): 
        self.file_string = file_string
        self.file_path = Path(self.file_string)

    def get_file_path(self): 
        return self.file_path

    def get_file_string(self):
        return self.file_string
        
    def load_workstation_workbook_and_sheet(self): #loads the workbook up and sets the first sheet to its working sheet
        self.workstation_workbook = load_workbook(filename=self.file_path)
        self.sheet = self.workstation_workbook.active

    def remove_cells_from_workbook(self): #used to remove all columns other than pc name / site
        self.sheet.delete_cols(1, 1)
        self.sheet.delete_cols(3, 24)

        self.sheet.delete_rows(1, 7)

    def save_workbook(self):
        self.workstation_workbook.save("Sophos.xlsx")