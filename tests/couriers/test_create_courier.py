import pytest
import allure
from methods.courier_methods import CourierMethods


@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        status_code = courier_methods.create_courier(courier_data)[1]
        assert status_code == 201, f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает ok: true")
    def test_create_courier_returns_ok_true(self, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        response = courier_methods.create_courier(courier_data)[0]
        assert response.get("ok") == True, f"ok: {response.get('ok')}"

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, courier_methods: CourierMethods):
        courier_data = courier_methods.generate_courier_data()
        courier_methods.create_courier(courier_data)
        status_code = courier_methods.create_courier(courier_data)[1]
        assert status_code == 409, f"status_code: {status_code}"

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Создание курьера без обязательного поля")
    def test_create_courier_without_required_field_fails(self, courier_methods: CourierMethods, missing_field: str):
        courier_data = courier_methods.generate_courier_data()
        courier_data.pop(missing_field)
        status_code = courier_methods.create_courier(courier_data)[1]
        assert status_code == 400, f"status_code: {status_code} для поля {missing_field}"