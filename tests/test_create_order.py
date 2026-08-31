import allure
import requests
from urls import Urls
from handlers import Handlers
from ingredients_data import Ingredients


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем с ингредиентами")
    def test_create_order_with_auth(self, user_data):
        response = requests.post(f"{Urls.HOME_PAGE}{Handlers.MAKE_ORDER}", headers=user_data[1], data=Ingredients.correct_ing_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_not_auth(self):
        response = requests.post(f"{Urls.HOME_PAGE}{Handlers.MAKE_ORDER}", data=Ingredients.correct_ing_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа авторизованным пользователем без ингредиентов")
    def test_create_order_without_ingredients(self, user_data):
        response = requests.post(f"{Urls.HOME_PAGE}{Handlers.MAKE_ORDER}", headers=user_data[1])
        assert response.status_code == 400
        assert response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным хешем ингредиентов")
    def test_create_order_hash_ingredient_invalid(self, user_data):
        response = requests.post(f"{Urls.HOME_PAGE}{Handlers.MAKE_ORDER}", headers=user_data[1], data=Ingredients.incorrect_ing_data)
        assert response.status_code == 500
        assert 'Internal Server Error' in response.text