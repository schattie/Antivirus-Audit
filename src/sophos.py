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
    
    def authenticate_with_api(self):
        self.api_session.headers.update({'Content-Type:application/x-www-form-urlencoded'})
        self.api_response = self.api_session.post('https://id.sophos.com/api/v2/oauth2/token', data = 'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}&scope=token')
        print(self.api_response)
