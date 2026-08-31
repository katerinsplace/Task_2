import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import User


@allure.suite('Изменение данных пользовователя')
class TestChangeUserData:

    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, user_data):
        payload = {'email': User.create_data_user()["email"]}
        response = requests.patch(f"{Urls.HOME_PAGE}{Handlers.CHANGE_USER_DATA}", headers=user_data[1], data=payload)
        assert response.status_code == 200
        assert response.json()['user']['email'] == payload["email"]

    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, user_data):
        payload = {'password': User.create_data_user()["password"]}
        response = requests.patch(f"{Urls.HOME_PAGE}{Handlers.CHANGE_USER_DATA}", headers=user_data[1], data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, user_data):
        payload = {'name': User.create_data_user()["name"]}
        response = requests.patch(f"{Urls.HOME_PAGE}{Handlers.CHANGE_USER_DATA}", headers=user_data[1], data=payload)
        assert response.status_code == 200
        assert response.json()['user']['name'] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_not_auth(self):
        response = requests.patch(f"{Urls.HOME_PAGE}{Handlers.CHANGE_USER_DATA}", data=User.create_data_user())
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'