import requests
import allure

from endpoints.endpoint import Endpoint


class EditMeme(Endpoint):

    @allure.step('Update a meme')
    def edit_meme(self, meme_id, test_data):
        self.response = self.session.put(
            f'{self.url}/meme/{meme_id}',
            json=test_data)
        self.json = self.response.json()
        return self.response
