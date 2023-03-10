from src.sophos import Sophos
from src.continuum import Continuum
from decouple import config

def main():
    sophos = Sophos()
    continuum = Continuum()

    sophos_file_path = None
    continuum_file_path = None

    print("Enter the file path where the Continuum workstations are located(Include .xlsx extension)")
    continuum_file_path = input()

    print("Enter the file path where the Sophos workstations are located(Include .xlsx extension)")
    sophos_file_path = input()

    continuum.set_file_path(continuum_file_path)
    sophos.set_file_path(sophos_file_path)

    continuum.load_workstation_workbook_and_sheet()
    sophos.load_workstation_workbook_and_sheet()

    continuum.remove_cells_from_workbook()
    sophos.remove_cells_from_workbook()

    continuum.save_workbook()
    sophos.save_workbook()

if __name__ == "__main__":
    main()