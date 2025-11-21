import pytest
import allure
from methods.order_methods import OrderMethods


@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrack:
    @allure.title("Успешный запрос возвращает объект с заказом")
    def test_get_order_by_track_success(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response, order_status = order_methods.create_order(ORDER_DATA_BLACK)
        track_number = order_response.get("track")
        
        response, status_code = order_methods.get_order_by_track(track_number)
        assert (status_code == 200 and "order" in response), (
            f"status_code: {status_code}, order: {'order' in response}")

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_get_order_without_track_fails(self, order_methods: OrderMethods):
        response, status_code = order_methods.get_order_by_track(None)
        assert status_code == 400, f"status_code: {status_code}"

    @allure.title("Запрос с несуществующим заказом возвращает ошибку")
    def test_get_order_with_nonexistent_track_fails(self, order_methods: OrderMethods):
        response, status_code = order_methods.get_order_by_track("999999")
        assert status_code == 404, f"status_code: {status_code}"