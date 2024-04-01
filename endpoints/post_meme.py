import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create a new meme')
    def new_meme(self, payload):
        response = self.session.post(f"{self.url}/meme", json=payload)
        return response

    @allure.step('Create a new meme by user mascot')
    def create_meme_as_mascot(self, payload):
        headers = {'Authorization': f'{self.get_token_mascot()}'}
        response = self.session.post(f"{self.url}/meme", json=payload, headers=headers)
        return response

    @allure.step('Create a new meme by unauthorized user')
    def new_meme_unauthorized(self, payload):
        self.session.headers.pop('Authorization', None)
        response = self.session.post(f"{self.url}/meme", json=payload)
        return response
