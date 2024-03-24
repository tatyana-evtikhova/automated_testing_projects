import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Delete a meme')
    def delete_meme_by_id(self, meme_id):
        self.response = requests.delete(f"{self.url}/meme/{meme_id}", headers=self.headers)
        return self.response
