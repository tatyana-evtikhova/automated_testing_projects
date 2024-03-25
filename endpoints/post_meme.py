import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create a new meme')
    def new_meme(self, payload):
        response = self.session.post(f"{self.url}/meme", json=payload)
        return response
