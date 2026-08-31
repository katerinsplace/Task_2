import allure
import requests
from handlers import Handlers
from urls import Urls
from ingredients_data import Ingredients


@allure.suite("Получение доступных заказов пользователя")
class TestGetOrderUser:

    @allure.title("Получение доступных заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, user_data):
        response_create_order = requests.post(f"{Urls.HOME_PAGE}{Handlers.MAKE_ORDER}", headers=user_data[1], data=Ingredients.correct_ing_data)
        response_get_order = requests.get(f"{Urls.HOME_PAGE}{Handlers.GET_ORDERS}", headers=user_data[1])
        assert response_get_order.status_code == 200
        assert response_get_order.json()['orders'][0]['number'] == response_create_order.json()['order']['number']

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_order_user_not_auth(self):
        response = requests.get(f"{Urls.HOME_PAGE}{Handlers.GET_ORDERS}")
        assert response.status_code == 401
        assert response.json()['message'] == "You should be authorised"