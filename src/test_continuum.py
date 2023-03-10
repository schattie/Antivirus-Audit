import unittest
import src.continuum

class ContinuumTest(unittest.TestCase):
    continuum = src.continuum.Continuum()
    def test_file_path_set(self): #test if file name is being passed properly
        self.continuum.set_file_path("Antivirus-Audit\continuum-workstations\2023.xlsx")
        self.assertIn("Antivirus-Audit\continuum-workstations\2023.xlsx", self.continuum.get_file_string())
    
    def test_excel_workbook_loading(self): #test if workbook loads succesfully
        self.continuum.set_file_path("Z:/Antivirus-Audit/continuum-workstations/2023.xlsx")
        self.continuum.load_workstation_workbook_and_sheet()
        self.assertIn("REQ00000000000001192888", self.continuum.sheet.title)

    def test_excel_workbook_column_deletion(self): #Test if columns are deleted.  
        self.continuum.set_file_path("Z:/Antivirus-Audit/continuum-workstations/2023.xlsx")
        self.continuum.load_workstation_workbook_and_sheet()
        self.continuum.remove_cells_from_workbook()
        self.assertEqual(2, self.continuum.sheet.max_column)
        self.assertEqual(1359, self.continuum.sheet.max_row)
