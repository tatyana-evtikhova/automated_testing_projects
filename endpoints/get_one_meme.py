import requests
import allure

from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):

    @allure.step('Get one meme by its ID')
    def get_meme(self, meme_id):
        self.response = self.session.get(
            f'{self.url}/meme/{meme_id}')
        return self.response

    @allure.step('Get one meme by its ID')
    def get_meme_unauthorized(self, meme_id, authorized=False):
        self.session.headers.pop('Authorization', None)
        self.response = self.session.get(f'{self.url}/meme/{meme_id}')
        return self.response