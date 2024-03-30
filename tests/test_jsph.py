import pytest

payload = {
    "text": "testing meme",
    "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
    "tags": ["IT", "meme", "software tester"],
    "info": {
        "colours": ["white", "brown", "grey"],
        "objects": ["picture", "text"]
    }
}


negative_payload = [
    {
        "text": "testing meme",
        "url": "link",
        "tags": ["IT", "meme", "software tester"],
        "info": ["white", "brown", "grey", "picture", "text"]
    },
    {
        "text": "testing meme",
        "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
        "tags": [25, 1996, 12],
        "info": ["white", "brown", "grey", "picture", "text"]
    },
    {
        "text": 13,
        "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
        "tags": ["IT", "meme", "software tester"],
        "info": ["white", "brown", "grey", "picture", "text"]
    },
]


def test_get_all_memes(get_all_memes_endpoint):
    response = get_all_memes_endpoint.get_all_memes()
    get_all_memes_endpoint.check_status_is_200(response)
    get_all_memes_endpoint.check_response_dict(response)


def test_get_one_meme(get_meme_endpoint, meme_id):
    response = get_meme_endpoint.get_meme(meme_id)
    get_meme_endpoint.check_status_is_200(response)
    data = response.json()
    expected_text = "Meme to test"
    get_meme_endpoint.check_meme_id(data, meme_id)


def test_create_meme(create_meme_endpoint):
    response = create_meme_endpoint.new_meme(payload)
    create_meme_endpoint.check_status_is_200(response)
    data = response.json()
    expected_text = payload['text']
    create_meme_endpoint.check_meme_id(data, data['id'])


def test_edit_meme(edit_meme_endpoint, meme_id, editable_meme):
    response = edit_meme_endpoint.edit_meme(meme_id, editable_meme)
    edit_meme_endpoint.check_status_is_200(response)
    data = response.json()
    edit_meme_endpoint.check_meme_text(data, editable_meme['text'])


def test_delete_meme(delete_meme_endpoint, meme_id):
    response = delete_meme_endpoint.delete_meme_by_id(meme_id)
    delete_meme_endpoint.check_meme_is_deleted(response)


def test_get_all_memes_unauthorized(unauthorized_get_all_memes_endpoint):
    response = unauthorized_get_all_memes_endpoint.get_all_memes_unauthorized()
    unauthorized_get_all_memes_endpoint.check_status_is_401(response)


def test_get_one_meme_unauthorized(unauthorized_get_meme_endpoint, meme_id):
    response = unauthorized_get_meme_endpoint.get_meme_unauthorized(meme_id)
    unauthorized_get_meme_endpoint.check_status_is_401(response)


def test_create_meme_unauthorized(unauthorized_create_meme_endpoint):
    response = unauthorized_create_meme_endpoint.new_meme_unauthorized(payload)
    unauthorized_create_meme_endpoint.check_status_is_401(response)


def test_edit_meme_unauthorized(unauthorized_edit_meme_endpoint, meme_id, editable_meme):
    response = unauthorized_edit_meme_endpoint.edit_meme_unauthorized(meme_id, editable_meme)
    unauthorized_edit_meme_endpoint.check_status_is_401(response)


def test_delete_meme_unauthorized(unauthorized_delete_meme_endpoint, meme_id):
    response = unauthorized_delete_meme_endpoint.delete_meme_by_id_unauthorized(meme_id)
    unauthorized_delete_meme_endpoint.check_status_is_401(response)


@pytest.mark.parametrize("data", negative_payload)
def test_create_meme_negative_testing(create_meme_endpoint, data):
    response = create_meme_endpoint.new_meme(negative_payload)
    create_meme_endpoint.check_status_is_400(response)


def test_check_token_alive(check_token_endpoint, authorize_endpoint):
    token = authorize_endpoint.ensure_token_valid()
    response = check_token_endpoint.check_token(token)
    check_token_endpoint.check_status_is_200(response)


def test_check_token_dead(check_token_endpoint, authorize_endpoint):
    valid_token = authorize_endpoint.ensure_token_valid()
    invalid_token = authorize_endpoint.invalid_token(valid_token)
    response = check_token_endpoint.check_token(invalid_token)
    check_token_endpoint.check_status_is_404(response)


def test_create_meme_and_delete_as_different_user(create_meme_as_mascot_endpoint, delete_meme_endpoint, authorize_endpoint):
    response = create_meme_as_mascot_endpoint.create_meme_as_mascot(payload)
    create_meme_as_mascot_endpoint.check_status_is_200(response)
    meme_id = response.json()["id"]
    response = delete_meme_endpoint.delete_meme_by_id(meme_id)
    assert response.status_code == 403, "Expected status code 403 for trying to delete another user's meme"
