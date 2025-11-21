import pytest
import allure
from methods.order_methods import OrderMethods
from data import ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BOTH, ORDER_DATA_NO_COLOR


@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize("order_data,description", [
        (ORDER_DATA_BLACK, "цвет BLACK"),
        (ORDER_DATA_GREY, "цвет GREY"), 
        (ORDER_DATA_BOTH, "оба цвета"),
        (ORDER_DATA_NO_COLOR, "без цвета")
    ])
    @allure.title("Создание заказа с разными параметрами цвета")
    def test_create_order_with_different_colors(self, order_methods: OrderMethods, order_data, description):
        response, status_code = order_methods.create_order(order_data)
        assert status_code == 201, f"status_code: {status_code} для {description}"

    @allure.title("Тело ответа содержит track")
    def test_create_order_returns_track(self, order_methods: OrderMethods):
        response, status_code = order_methods.create_order(ORDER_DATA_BLACK)
        assert (status_code == 201 and "track" in response), (
            f"status_code: {status_code}, track: {response.get('track')}")