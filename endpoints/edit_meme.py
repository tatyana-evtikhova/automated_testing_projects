import requests
import allure

from endpoints.endpoint import Endpoint


class EditMeme(Endpoint):

    @allure.step('Update a meme')
    def edit_meme(self, meme_id, test_data):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=test_data,
            headers=self.headers)
        self.json = self.response.json()
        return self.response
