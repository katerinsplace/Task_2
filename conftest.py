import pytest
import requests
from user_data import User
from urls import Urls
from handlers import Handlers


@pytest.fixture
def delete_user():
    tokens = []
    yield tokens

    for token in tokens:
        headers = {"Authorization": token}
        requests.delete(f'{Urls.HOME_PAGE}{Handlers.DELETE_USER}', headers=headers)

@pytest.fixture
def user_data(delete_user):
    data = User.create_data_user()
    response = requests.post(f'{Urls.HOME_PAGE}{Handlers.CREATE_USER}', data=data)
    token = response.json().get("accessToken")
    if token:
        delete_user.append(token)
    return (data, {'Authorization': token})
    
            