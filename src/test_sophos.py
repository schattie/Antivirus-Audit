import unittest
import src.sophos

class SophosTest(unittest.TestCase):
    sophos = src.sophos.Sophos()
    def test_file_path_set(self): #test if file name is being passed properly
        self.sophos.set_file_path("Z:\Antivirus-Audit\sophos-workstations\Sophos_10032023_10-45-28.xlsx")
        self.assertIn("Z:\Antivirus-Audit\sophos-workstations\Sophos_10032023_10-45-28.xlsx", self.sophos.get_file_string())
    
    def test_excel_workbook_loading(self): #test if workbook loads succesfully
        self.sophos.set_file_path("Z:\Antivirus-Audit\sophos-workstations\Sophos_10032023_10-45-28.xlsx")
        self.sophos.load_workstation_workbook_and_sheet()
        self.assertIn("Sophos_10032023_10-45-28", self.sophos.sheet.title)

    def test_excel_workbook_column_deletion(self): #Test if columns are deleted.  
        self.sophos.set_file_path("Z:\Antivirus-Audit\sophos-workstations\Sophos_10032023_10-45-28.xlsx")
        self.sophos.load_workstation_workbook_and_sheet()
        self.sophos.remove_cells_from_workbook()
        self.assertEqual(2, self.sophos.sheet.max_column)
        self.assertEqual(1221, self.sophos.sheet.max_row)
