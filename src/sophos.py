from pathlib import Path
import requests

class Sophos:
    id_file_string = None #file path where client id is stored
    id_file_path = None #converts string into path 
    secret_file_string = None
    secret_file_path = None
    client_id = None 
    client_secret = None
    api_response = None
    api_session = requests.Session()

    def set_id_file_path(self, id_file_string):
        self.id_file_string = id_file_string
        self.id_file_path = Path(self.id_file_string)

    def set_secret_file_path(self, secret_file_string):
        self.secret_file_string = secret_file_string
        self.secret_file_path = Path(self.secret_file_string)

    def set_client_id(self):
        self.client_id = Path(self.id_file_path).read_text()

    def set_client_secret(self):
        self.client_secret = Path(self.secret_file_path).read_text()

    def get_id_file_path(self):
        return self.id_file_path
    
    def get_secret_file_path(self):
        return self.secret_file_path
    
    def get_id_file_string(self):
        return self.id_file_string
    
    def get_secret_file_string(self):
        return self.secret_file_string
    
    def get_client_id(self):
        return self.client_id
    
    def get_client_secret(self):
        return self.client_secret
    
    def authenticate_with_api(self):
        self.api_session.headers.update({'Content-Type:application/x-www-form-urlencoded'})
        self.api_response = self.api_session.post('https://id.sophos.com/api/v2/oauth2/token', data = 'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}&scope=token')
        print(self.api_response)
