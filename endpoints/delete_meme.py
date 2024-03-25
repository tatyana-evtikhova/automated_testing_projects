import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Delete a meme')
    def delete_meme_by_id(self, meme_id):
        self.response = self.session.delete(f"{self.url}/meme/{meme_id}")
        return self.response

    @allure.step('Check that meme is deleted')
    def check_meme_is_deleted(self, meme_id):
        check_response = self.session.get(f'{self.url}/meme/{meme_id}')
