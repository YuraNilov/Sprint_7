import requests
import allure
import random
import string


class CourierMethods:
    def __init__(self):
        from data import BASE_URL, COURIERS_URL, LOGIN_URL
        self.base_url = BASE_URL
        self.couriers_url = COURIERS_URL
        self.login_url = LOGIN_URL

    @staticmethod
    def generate_courier_data():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))

        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    @allure.step("Создать курьера")
    def create_courier(self, payload=None):
        if payload is None:
            payload = self.generate_courier_data()
        
        response = requests.post(f'{self.base_url}{self.couriers_url}', json=payload)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(f'{self.base_url}{self.login_url}', json=payload)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(f'{self.base_url}{self.couriers_url}/{courier_id}')
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code