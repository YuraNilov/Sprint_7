import pytest
import allure
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_methods():
    return CourierMethods()


@pytest.fixture
def order_methods():
    from methods.order_methods import OrderMethods
    return OrderMethods()


@pytest.fixture
def courier():
    """Фикстура для основного задания - создает курьера"""
    courier_methods = CourierMethods()
    courier_data = courier_methods.generate_courier_data()
    
    response, status_code = courier_methods.create_courier(courier_data)
    
    login_response, login_status = courier_methods.login_courier(
        courier_data["login"], courier_data["password"]
    )
    courier_id = login_response.get("id") if login_status == 200 else None
    
    yield {
        "login": courier_data["login"],
        "password": courier_data["password"], 
        "first_name": courier_data["firstName"],
        "id": courier_id
    }
    
    if courier_id:
        try:
            courier_methods.delete_courier(courier_id)
        except:
            allure.attach(f"Не удалось удалить курьера {courier_id}", "Ошибка очистки")


@pytest.fixture
def order_with_track(order_methods):
    """Фикстура создает заказ для тестов"""
    from data import ORDER_DATA_BLACK
    response, status_code = order_methods.create_order(ORDER_DATA_BLACK)
    
    track_number = response.get("track")
    order_id = response.get("id")
    
    yield {
        "track": track_number,
        "id": order_id,
        "response": response
    }