import unittest
from continuum import Continuum

class ContinuumTest(unittest.TestCase):
    continuum = Continuum()
    def test_file_path_set(self):
        self.continuum.set_file_path("Antivirus-Audit\continuum-workstations\2023.xlsx")
        self.assertIn("Antivirus-Audit\continuum-workstations\2023.xlsx", self.continuum.get_file_string())
    
    def test_excel_workbook_loading(self):
        self.continuum.set_file_path("Z:/Antivirus-Audit/continuum-workstations/2023.xlsx")
        self.continuum.load_workstation_workbook_and_sheet()
        self.assertIn("REQ00000000000001192888", self.continuum.sheet.title)