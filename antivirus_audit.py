from src.sophos import Sophos

def main():
    sophos = Sophos()

    sophos.set_client_id()
    sophos.set_client_secret()
    print(sophos.client_id)
    print(sophos.client_secret)


if __name__ == "__main__":
    main()