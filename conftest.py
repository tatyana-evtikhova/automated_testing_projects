import pytest
import requests
from endpoints.post_meme import CreateMeme
from endpoints.edit_meme import EditMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_one_meme import GetOneMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.unauthorized_get_meme import UnauthorizedGetMeme
from endpoints.unauthorized_get_all_memes import UnauthorizedGetAllMemes
from endpoints.unauthorized_create_meme import UnauthorizedCreateMeme
from endpoints.unauthorized_edit_meme import UnauthorizedEditMeme
from endpoints.unauthorized_delete_meme import UnauthorizedDeleteMeme
from endpoints.create_meme_by_another_user import CreateMemeAsMascot
from authorize import Authorize
from endpoints.check_token import CheckToken
from endpoints.endpoint import Endpoint


@pytest.fixture(scope='session', autouse=True)
def api_client():
    endpoint = Endpoint()
    endpoint.init_session()
    return endpoint


@pytest.fixture()
def authorize_endpoint():
    return Authorize()


@pytest.fixture()
def check_token_endpoint():
    return CheckToken()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def create_meme_as_mascot_endpoint():
    return CreateMemeAsMascot()


@pytest.fixture()
def unauthorized_create_meme_endpoint():
    return UnauthorizedCreateMeme()


@pytest.fixture()
def edit_meme_endpoint():
    return EditMeme()


@pytest.fixture()
def unauthorized_edit_meme_endpoint():
    return UnauthorizedEditMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def unauthorized_delete_meme_endpoint():
    return UnauthorizedDeleteMeme()


@pytest.fixture()
def get_meme_endpoint():
    return GetOneMeme()


@pytest.fixture()
def unauthorized_get_meme_endpoint():
    return UnauthorizedGetMeme()


@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()


@pytest.fixture()
def unauthorized_get_all_memes_endpoint():
    return UnauthorizedGetAllMemes()


@pytest.fixture()
def meme_id(create_meme_endpoint, delete_meme_endpoint):
    payload = {
        "text": "Meme to test",
        "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
        "tags": ["IT", "meme", "software tester"],
        "info": {
            "colours": ["white", "brown", "grey"],
            "objects": ["picture", "text"]
        }
    }
    response = create_meme_endpoint.new_meme(payload)
    json_response = response.json()
    meme_id = json_response['id']
    yield meme_id
    delete_meme_endpoint.delete_meme_by_id(meme_id)


@pytest.fixture
def editable_meme(meme_id):
    test_data = {
        "id": meme_id,
        "text": "updated meme",
        "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
        "tags": ["IT", "meme", "Voity v IT"],
        "info": {
            "colours": ["blue", "green"],
            "objects": ["picture", "text"]
        }
    }
    return test_data


@pytest.fixture
def negative_payload(request):
    payloads = [
        {
            "text": "testing meme",
            "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
            "tags": ["IT", "meme", "software tester"],
            "info": ["white", "brown", "grey", "picture", "text"]
        },
        {
            "text": "testing meme",
            "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
            "tags": ["IT", "meme", "software tester"],
            "info": ["white", "brown", "grey", "picture", "text"]
        },
        {
            "text": "testing meme",
            "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
            "tags": ["IT", "meme", "software tester"],
            "info": ["white", "brown", "grey", "picture", "text"]
        },
    ]
    return request.param
