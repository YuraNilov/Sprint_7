import pytest
import allure
from methods.courier_methods import CourierMethods


@allure.feature("Удаление курьера")
class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        create_response, create_status = courier_methods.create_courier(courier_data)
        
        login_response, login_status = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )
        courier_id = login_response.get("id")
        
        response, status_code = courier_methods.delete_courier(courier_id)
        assert status_code == 200, f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает ok: true")
    def test_delete_courier_returns_ok_true(self, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        create_response, create_status = courier_methods.create_courier(courier_data)
        login_response, login_status = courier_methods.login_courier(
            courier_data["login"], courier_data["password"]
        )
        courier_id = login_response.get("id")
        
        response, status_code = courier_methods.delete_courier(courier_id)
        assert response.get("ok") == True, f"ok: {response.get('ok')}"

    @allure.title("Запрос с несуществующим id возвращает ошибку")
    def test_delete_courier_with_nonexistent_id_fails(self, courier_methods: CourierMethods):
        response, status_code = courier_methods.delete_courier("999999")
        assert status_code == 404, f"status_code: {status_code}"

    @allure.title("Запрос без id возвращает ошибку")
    def test_delete_courier_without_id_fails(self, courier_methods: CourierMethods):
        response, status_code = courier_methods.delete_courier("")
        assert status_code == 404, f"status_code: {status_code}"