import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMemeAsMascot(Endpoint):
    meme_id = None

    @allure.step('Create a new meme by user mascot')
    def create_meme_as_mascot(self, payload):
        headers = {'Authorization': f'{self.get_token_mascot()}'}
        response = self.session.post(f"{self.url}/meme", json=payload, headers=headers)
        return response
