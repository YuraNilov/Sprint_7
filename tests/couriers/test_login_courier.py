import pytest
import allure
from methods.courier_methods import CourierMethods


@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        courier_methods = CourierMethods()
        status_code = courier_methods.login_courier(
            courier["login"], courier["password"]
        )[1]
        assert status_code == 200, f"status_code: {status_code}"

    @allure.title("Успешный запрос возвращает id")
    def test_login_returns_id(self, courier):
        courier_methods = CourierMethods()
        response = courier_methods.login_courier(
            courier["login"], courier["password"]
        )[0]
        assert "id" in response, f"id: {response.get('id')}"

    @pytest.mark.parametrize("login,password,expected_status", [
        ("", "password", 400),
        ("login", "", 400),
        ("nonexistent_login", "password", 404),
        ("login", "wrong_password", 404)
    ])
    @allure.title("Авторизация с ошибками")
    def test_login_with_errors_fails(self, courier_methods: CourierMethods, login, password, expected_status):
        status_code = courier_methods.login_courier(login, password)[1]
        assert status_code == expected_status, f"status_code: {status_code}"