import pytest
import allure
from methods.order_methods import OrderMethods


@allure.feature("Получение списка заказов")
class TestGetOrders:
    @allure.title("В тело ответа возвращается список заказов")
    def test_get_orders_list_returns_orders(self, order_methods: OrderMethods):
        response, status_code = order_methods.get_orders_list()
        assert (status_code == 200 and "orders" in response), (
            f"status_code: {status_code}, orders: {'orders' in response}")