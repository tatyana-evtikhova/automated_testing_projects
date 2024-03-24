import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create a new meme')
    def new_meme(self, payload):
        response = requests.post(f"{self.url}/meme", headers=self.headers, json=payload)
        return response
