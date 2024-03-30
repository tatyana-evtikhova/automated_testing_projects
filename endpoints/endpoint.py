import allure
import requests
from authorize import Authorize


class Endpoint(Authorize):
    url = 'http://167.172.172.115:52355'
    session = None
    token = None

    def init_session(self):
        self.ensure_token_valid()

    @allure.step('Check that response is 200')
    def check_status_is_200(self, response):
        assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    @allure.step('Check that response is 401')
    def check_status_is_401(self, response):
        assert response.status_code == 401, f"Expected status 401, got {response.status_code}"

    @allure.step('Check that response is 400 Bad Request')
    def check_status_is_400(self, response):
        assert response.status_code == 400, f"Expected status 400, got {response.status_code}"

    @allure.step('Check that response is 404 Not Found')
    def check_status_is_404(self, response):
        assert response.status_code == 404, f"Expected status 404, got {response.status_code}"

    @allure.step('Check that response is 403 Forbidden')
    def check_status_is_403(self, response):
        assert response.status_code == 404, f"Expected status 403, got {response.status_code}"

    @allure.step('Check that list is given in response')
    def check_response_dict(self, response):
        assert isinstance(response.json(), dict), "Response is not a list"

    @allure.step('Check that meme id is equal to expected')
    def check_meme_id(self, data, expected_id):
        assert data["id"] == expected_id, f"Expected meme id {expected_id}, got {data['id']}"

    @allure.step('Check that meme text is equal to expected')
    def check_meme_text(self, data, expected_text):
        assert data['text'] == expected_text, f"Expected meme text '{expected_text}', got '{data['text']}'"
