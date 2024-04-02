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
        assert check_response.status_code == 404, f"Meme with ID {meme_id} still exists"

    @allure.step('Delete a meme by unauthorized user')
    def delete_meme_by_id_unauthorized(self, meme_id):
        self.session.headers.pop('Authorization', None)
        self.response = self.session.delete(f"{self.url}/meme/{meme_id}")
        return self.response
