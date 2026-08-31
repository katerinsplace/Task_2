import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import User

@allure.suite('Авторизация пользователя')
class TestLoginUser:

    @allure.title('Авторизация под существующим пользователем')
    def test_login_user(self, user_data):
        payload = {'email': user_data[0]['email'], 'password': user_data[0]['password']}
        response = requests.post(f'{Urls.HOME_PAGE}{Handlers.LOGIN}', data=payload)
        assert response.status_code == 200
        assert response.json().get('success') == True

    @allure.title('Авторизация с некорректным логином и паролем')
    def test_login_user_error(self):
        payload = {'email': User.create_data_user()['email'], 'password': User.create_data_user()['password']}
        response = requests.post(f'{Urls.HOME_PAGE}{Handlers.LOGIN}', data=payload)
        assert response.status_code == 401
        assert response.json().get('success') == False