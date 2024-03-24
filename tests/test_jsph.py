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


def test_get_all_memes(get_all_memes_endpoint, api_session):
    response = get_all_memes_endpoint.get_all_memes()
    get_all_memes_endpoint.check_status_is_200(response)
    get_all_memes_endpoint.check_response_dict(response)


def test_get_one_meme(get_meme_endpoint, api_session, meme_id):
    response = get_meme_endpoint.get_meme(meme_id)
    get_meme_endpoint.check_status_is_200(response)
    data = response.json()
    expected_text = "Meme to test"
    get_meme_endpoint.check_meme_id(data, meme_id)
    get_meme_endpoint.check_meme_text(data, expected_text)


def test_create_meme(create_meme_endpoint):
    response = create_meme_endpoint.new_meme(payload)
    create_meme_endpoint.check_status_is_200(response)
    data = response.json()
    expected_text = payload['text']
    create_meme_endpoint.check_meme_id(data, data['id'])
    create_meme_endpoint.check_meme_text(data, expected_text)


def test_edit_meme(edit_meme_endpoint, meme_id, editable_meme):
    response = edit_meme_endpoint.edit_meme(meme_id, editable_meme)
    edit_meme_endpoint.check_status_is_200(response)
    data = response.json()
    edit_meme_endpoint.check_meme_text(data, editable_meme['text'])


def test_delete_meme(delete_meme_endpoint, meme_id):
    response = delete_meme_endpoint.delete_meme_by_id(meme_id)
    delete_meme_endpoint.check_meme_is_deleted(response)
