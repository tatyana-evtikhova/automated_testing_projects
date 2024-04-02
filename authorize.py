import requests


class Authorize:
    url = 'http://167.172.172.115:52355'

    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.ensure_token_valid()

    def get_new_token(self):
        response = requests.post(f'{self.url}/authorize', json={"name": "Tatyana"})
        self.token = response.json().get('token')
        self.session.headers.update({"Authorization": self.token})
        return self.token

    def is_token_valid(self):
        if self.token is None:
            return False
        response = self.session.get(f'{self.url}/authorize/{self.token}')
        return response.status_code == 200

    def ensure_token_valid(self):
        if not self.is_token_valid():
            return self.get_new_token()
        return self.token

    def invalid_token(self, token):
        return token + "*"

    def get_token_mascot(self):
        response = requests.post(f'{self.url}/authorize', json={"name": "mascot"})
        return response.json().get('token')
