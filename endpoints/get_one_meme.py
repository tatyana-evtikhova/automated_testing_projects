import requests
import allure

from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):

    @allure.step('Get one meme by its ID')
    def get_meme(self, meme_id):
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=self.headers)
        return self.response

