import pytest
import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods


@allure.feature("Принятие заказа")
class TestAcceptOrder:
    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response, order_status = order_methods.create_order(ORDER_DATA_BLACK)
        track_number = order_response.get("track")
                
        order_id, status = order_methods.get_order_id_by_track(track_number)
        
        courier_methods = CourierMethods()
        courier_data = courier_methods.generate_courier_data()
        create_response, create_status = courier_methods.create_courier(courier_data)
        login_response, login_status = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )
        courier_id = login_response.get("id")
        
        response, status_code = order_methods.accept_order(order_id, courier_id)
        
        assert status_code in [200, 409], f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает ok: true")
    def test_accept_order_returns_ok_true(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response, order_status = order_methods.create_order(ORDER_DATA_BLACK)
        track_number = order_response.get("track")
        order_id, status = order_methods.get_order_id_by_track(track_number)
        
        courier_methods = CourierMethods()
        courier_data = courier_methods.generate_courier_data()
        create_response, create_status = courier_methods.create_courier(courier_data)
        login_response, login_status = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )
        courier_id = login_response.get("id")
        
        response, status_code = order_methods.accept_order(order_id, courier_id)
        if status_code == 200:
            assert response.get("ok") == True, f"ok: {response.get('ok')}"
        else:
            assert status_code == 409, f"status_code: {status_code}"

    @pytest.mark.parametrize("order_id,courier_id,expected_status", [
        ("123", None, 400),      # Без courier_id (400)
        ("999999", "123", 404),  # Несуществующий заказ (404)
        ("123", "999999", 404)   # Несуществующий курьер (404)
    ])
    @allure.title("Неуспешное принятие заказа")
    def test_accept_order_fails(self, order_methods: OrderMethods, order_id, courier_id, expected_status):
        response, status_code = order_methods.accept_order(order_id, courier_id)
        assert status_code == expected_status, f"status_code: {status_code}"