import unittest
from continuum import Continuum

class ContinuumTest(unittest.TestCase):
    continuum = Continuum()
    def test_file_path_set(self):
        self.continuum.set_file_path("hello")
        self.assertIn("hello", self.continuum.get_file_path())
       