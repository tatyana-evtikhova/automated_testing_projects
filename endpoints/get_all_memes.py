import requests
import allure

from endpoints.endpoint import Endpoint
from authorize import Authorize


class GetAllMemes(Endpoint):

    @allure.step('Get all memes')
    def get_all_memes(self):
        self.response = self.session.get(
            f'{self.url}/meme')
        return self.response
