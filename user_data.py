from faker import Faker

class User:

    @staticmethod
    def create_data_user():
        fake_user = Faker()

        reg_data = {
            "email": fake_user.email() + 'name',
            "password": fake_user.password(),
            "name": fake_user.name()}
        return reg_data

    data_no_email = {
        "email": "",
        "password": "password",
        "name": "username"}

    data_no_password = {
        "email": "catherina@yandex.ru",
        "password": "",
        "name": "username"}

    data_no_name = {
        "email": "catherina@yandex.ru",
        "password": "password",
        "name": ""}
