import pytest
import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods


@allure.feature("Принятие заказа")
class TestAcceptOrder:
    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response = order_methods.create_order(ORDER_DATA_BLACK)[0]
        track_number = order_response.get("track")
        order_id = order_methods.get_order_id_by_track(track_number)[0]
        
        courier_methods = CourierMethods()
        courier_data = courier_methods.generate_courier_data()
        courier_methods.create_courier(courier_data)
        login_response = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )[0]
        courier_id = login_response.get("id")
        
        status_code = order_methods.accept_order(order_id, courier_id)[1]
        assert status_code == 200, f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает ok: true")
    def test_accept_order_returns_ok_true(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response = order_methods.create_order(ORDER_DATA_BLACK)[0]
        track_number = order_response.get("track")
        order_id = order_methods.get_order_id_by_track(track_number)[0]
        
        courier_methods = CourierMethods()
        courier_data = courier_methods.generate_courier_data()
        courier_methods.create_courier(courier_data)
        login_response = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )[0]
        courier_id = login_response.get("id")
        
        response = order_methods.accept_order(order_id, courier_id)[0]
        assert response.get("ok") == True, f"ok: {response.get('ok')}"

    @allure.title("Запрос без id заказа возвращает ошибку")
    def test_accept_order_without_order_id_fails(self, order_methods: OrderMethods, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        courier_methods.create_courier(courier_data)
        login_response = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )[0]
        courier_id = login_response.get("id")
        
        status_code = order_methods.accept_order("", courier_id)[1]
        assert status_code == 404, f"status_code: {status_code}"

    @allure.title("Запрос без id курьера возвращает ошибку")
    def test_accept_order_without_courier_id_fails(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response = order_methods.create_order(ORDER_DATA_BLACK)[0]
        track_number = order_response.get("track")
        order_id = order_methods.get_order_id_by_track(track_number)[0]
        
        status_code = order_methods.accept_order(order_id, None)[1]
        assert status_code == 400, f"status_code: {status_code}"

    @allure.title("Запрос с несуществующим id заказа возвращает ошибку")
    def test_accept_order_with_nonexistent_order_id_fails(self, order_methods: OrderMethods, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        courier_methods.create_courier(courier_data)
        login_response = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )[0]
        courier_id = login_response.get("id")
        
        status_code = order_methods.accept_order("999999", courier_id)[1]
        assert status_code == 404, f"status_code: {status_code}"

    @allure.title("Запрос с несуществующим id курьера возвращает ошибку")
    def test_accept_order_with_nonexistent_courier_id_fails(self, order_methods: OrderMethods):
        from data import ORDER_DATA_BLACK
        order_response = order_methods.create_order(ORDER_DATA_BLACK)[0]
        track_number = order_response.get("track")
        order_id = order_methods.get_order_id_by_track(track_number)[0]
        
        status_code = order_methods.accept_order(order_id, "999999")[1]
        assert status_code == 404, f"status_code: {status_code}"