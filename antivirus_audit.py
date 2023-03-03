from src.sophos import Sophos

def main():
    sophos = Sophos()

    sophos.set_id_file_path("Z:\Antivirus-Audit\keys\sophos_client_id.txt")
    sophos.set_secret_file_path("Z:\Antivirus-Audit\keys\sophos_client_secret.txt")
    sophos.set_client_id()
    sophos.set_client_secret()
    sophos.authenticate_with_api()

if __name__ == "__main__":
    main()