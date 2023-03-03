import unittest
from sophos import Sophos
from pathlib import Path 

class SophosTest(unittest.TestCase):
    sophos = Sophos()
    def test_set_client_id_and_secret(self):
        self.sophos.set_id_file_path("Z:\Antivirus-Audit\keys\sophos_client_id.txt")
        self.sophos.set_secret_file_path("Z:\Antivirus-Audit\keys\sophos_client_secret.txt")
        self.sophos.set_client_id()
        self.sophos.set_client_secret()
        self.assertIn(Path(self.sophos.id_file_path).read_text(), self.sophos.get_client_id())
        self.assertIn(Path(self.sophos.secret_file_path).read_text(), self.sophos.get_client_secret())
    

