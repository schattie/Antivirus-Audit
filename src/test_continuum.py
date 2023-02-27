import unittest
from continuum import Continuum

class ContinuumTest(unittest.TestCase):
    continuum = Continuum()
    def test_file_path_set(self): #test if file name is being passed properly
        self.continuum.set_file_path("Antivirus-Audit\continuum-workstations\2023.xlsx")
        self.assertIn("Antivirus-Audit\continuum-workstations\2023.xlsx", self.continuum.get_file_string())
    
    def test_excel_workbook_loading(self): #test if workbook loads succesfully
        self.continuum.set_file_path("Z:/Antivirus-Audit/continuum-workstations/2023.xlsx")
        self.continuum.load_workstation_workbook_and_sheet()
        self.assertIn("REQ00000000000001192888", self.continuum.sheet.title)

    def test_excel_workbook_column_deletion(self): #creates a excel file in root directory. Examine this for test results. Should only have one column. 
        self.continuum.set_file_path("Z:/Antivirus-Audit/continuum-workstations/2023.xlsx")
        self.continuum.load_workstation_workbook_and_sheet()
        self.continuum.remove_cells_from_workbook()
        self.continuum.workstation_workbook.save(filename="test.xlsx") 