import requests
import allure

from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):

    @allure.step('Check if the token is alive')
    def check_token(self, token):
        response = self.session.get(f'{self.url}/authorize/{token}')
        return response
