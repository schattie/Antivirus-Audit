from src.sophos import Sophos
from decouple import config

def main():
    sophos = Sophos()
    url = "https://id.sophos.com/api/v2/oauth2/token"

    sophos.set_client_id()
    sophos.set_client_secret()
    print(sophos.authenticate_with_api(config('SOPHOS_CLIENT_ID'), config('SOPHOS_CLIENT_SECRET'), url))


if __name__ == "__main__":
    main()