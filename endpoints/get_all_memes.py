import requests
import allure

from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    @allure.step('Get all memes')
    def get_all_memes(self):
        self.response = requests.get(
            f'{self.url}/meme',
            headers=self.headers)
        return self.response
