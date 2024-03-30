import requests
import allure

from endpoints.endpoint import Endpoint


class UnauthorizedCreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create a new meme by unauthorized user')
    def new_meme_unauthorized(self, payload):
        self.session.headers.pop('Authorization', None)
        response = self.session.post(f"{self.url}/meme", json=payload)
        return response
