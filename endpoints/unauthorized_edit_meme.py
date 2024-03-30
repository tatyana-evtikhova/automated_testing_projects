import requests
import allure

from endpoints.endpoint import Endpoint


class UnauthorizedEditMeme(Endpoint):

    @allure.step('Update a meme by unauthorized user')
    def edit_meme_unauthorized(self, meme_id, test_data):
        self.session.headers.pop('Authorization', None)
        self.response = self.session.put(
            f'{self.url}/meme/{meme_id}',
            json=test_data)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response
