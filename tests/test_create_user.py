import pytest
import allure
import requests
from urls import Urls
from handlers import Handlers
from user_data import User

@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user_success(self, delete_user):
        response = requests.post(f'{Urls.HOME_PAGE}{Handlers.CREATE_USER}', data=User.create_data_user())
        token = response.json()["accessToken"]
        if token:
            delete_user.append(token)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user_error(self, user_data):
        response = requests.post(f'{Urls.HOME_PAGE}{Handlers.CREATE_USER}', data=user_data[0])
        assert response.status_code == 403
        assert 'User already exists' in response.text

    @allure.title('Создание пользователя с незаполненными обязательными полями')
    @pytest.mark.parametrize('user_data_incorrect', [User.data_no_email, User.data_no_password, User.data_no_name])
    def test_create_user_without_field(self, user_data_incorrect):
        response = requests.post(f'{Urls.HOME_PAGE}{Handlers.CREATE_USER}', data=user_data_incorrect)
        assert response.status_code == 403
        assert 'Email, password and name are required fields' in response.text

