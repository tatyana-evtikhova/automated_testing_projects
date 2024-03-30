import requests
import allure

from endpoints.endpoint import Endpoint


class UnauthorizedGetAllMemes(Endpoint):

    @allure.step('Get all memes by unauthorized user')
    def get_all_memes_unauthorized(self, authorized=False):
        self.session.headers.pop('Authorization', None)
        self.response = self.session.get(f'{self.url}/meme')
        return self.response
