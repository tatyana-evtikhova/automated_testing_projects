import requests
import allure

from endpoints.endpoint import Endpoint


class UnauthorizedDeleteMeme(Endpoint):

    @allure.step('Delete a meme by unauthorized user')
    def delete_meme_by_id_unauthorized(self, meme_id):
        self.session.headers.pop('Authorization', None)
        self.response = self.session.delete(f"{self.url}/meme/{meme_id}")
        return self.response
