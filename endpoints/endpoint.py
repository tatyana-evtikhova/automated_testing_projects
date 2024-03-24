import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    token = "Oljr2Ttv2MUJlbh"
    headers = {"Authorization": token}

    @allure.step('Check that response is 200')
    def check_status_is_200(self, response):
        assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    @allure.step('Check that meme is deleted')
    def check_meme_is_deleted(self, response):
        assert response.status_code == 200, f"Expected status 400, got {response.status_code}"

    @allure.step('Check that list is given in response')
    def check_response_dict(self, response):
        assert isinstance(response.json(), dict), "Response is not a list"

    @allure.step('Check that meme id is equal to expected')
    def check_meme_id(self, data, expected_id):
        assert data["id"] == expected_id, f"Expected meme id {expected_id}, got {data['id']}"

    @allure.step('Check that meme text is equal to expected')
    def check_meme_text(self, data, expected_text):
        assert data['text'] == expected_text, f"Expected meme text '{expected_text}', got '{data['text']}'"

