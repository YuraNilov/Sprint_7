import pytest
import allure
from methods.courier_methods import CourierMethods


@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        courier_methods = CourierMethods()
        response, status_code = courier_methods.login_courier(
            courier["login"], courier["password"]
        )
        assert status_code == 200, f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает id")
    def test_login_returns_id(self, courier):
        courier_methods = CourierMethods()
        response, status_code = courier_methods.login_courier(
            courier["login"], courier["password"]
        )
        assert (status_code == 200 and "id" in response), (
            f"status_code: {status_code}, id: {response.get('id')}")

    @pytest.mark.parametrize("login,password,expected_status", [
        ("", "password", 400),
        ("login", "", 400),
        ("nonexistent_login", "password", 404),
        ("login", "wrong_password", 404)
    ])
    @allure.title("Авторизация с ошибками")
    def test_login_with_errors_fails(self, courier_methods: CourierMethods, login, password, expected_status):
        response, status_code = courier_methods.login_courier(login, password)
        assert status_code == expected_status, f"status_code: {status_code}"