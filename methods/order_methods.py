import requests
import allure
from data import BASE_URL, ORDERS_URL, ACCEPT_ORDER_URL, TRACK_ORDER_URL


class OrderMethods:
    def __init__(self):
        self.base_url = BASE_URL
        self.orders_url = ORDERS_URL
        self.accept_order_url = ACCEPT_ORDER_URL
        self.track_order_url = TRACK_ORDER_URL

    @allure.step("Создание заказа")
    def create_order(self, payload):
        response = requests.post(f'{self.base_url}{self.orders_url}', json=payload)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получение списка заказов")
    def get_orders_list(self, params=None):
        response = requests.get(f'{self.base_url}{self.orders_url}', params=params)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Принять заказ")
    def accept_order(self, order_id, courier_id):
        url = f'{self.base_url}{self.accept_order_url}{order_id}'
        params = {'courierId': courier_id}
        response = requests.put(url, params=params)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получить заказ по трек-номеру")
    def get_order_by_track(self, track_number):
        params = {'t': track_number}
        response = requests.get(f'{self.base_url}{self.track_order_url}', params=params)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получить ID заказа по трек-номеру")
    def get_order_id_by_track(self, track_number):
        """Получает ID заказа по трек-номеру"""
        params = {'t': track_number}
        response = requests.get(f'{self.base_url}{self.track_order_url}', params=params)
        try:
            order_data = response.json()
            return order_data.get("order", {}).get("id"), response.status_code
        except requests.exceptions.JSONDecodeError:
            return None, response.status_code