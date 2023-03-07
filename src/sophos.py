from pathlib import Path
import requests
from decouple import config

class Sophos:
    client_id = None 
    client_secret = None
    api_response = None
    api_session = requests.Session()

    def set_client_id(self):
        self.client_id = config('SOPHOS_CLIENT_ID')

    def set_client_secret(self):
        self.client_secret = config('SOPHOS_CLIENT_SECRET')
    
    def get_client_id(self):
        return self.client_id
    
    def get_client_secret(self):
        return self.client_secret
    
    def authenticate_with_api(self, client_id, client_secret, url):
        d = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'token'
        }
        request_token = requests.post(url, auth=(client_id, client_secret), data=d)
        json_token = request_token.json()
        headers = {'Authorization': f"Bearer {json_token['access_token']}"}
        return headers
