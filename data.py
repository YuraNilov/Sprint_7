BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

COURIERS_URL = 'courier'
LOGIN_URL = 'courier/login'
ORDERS_URL = 'orders'
ACCEPT_ORDER_URL = 'orders/accept/'
TRACK_ORDER_URL = 'orders/track'

ORDER_DATA_BLACK = {
    "firstName": "Иван",
    "lastName": "Иванов", 
    "address": "Москва, ул. Ленина, 1",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 3,
    "deliveryDate": "2025-12-31",
    "comment": "Позвонить за час",
    "color": ["BLACK"]
}

ORDER_DATA_GREY = {
    "firstName": "Петр",
    "lastName": "Петров",
    "address": "Москва, ул. Пушкина, 10",
    "metroStation": 5,
    "phone": "+7 900 123 45 67", 
    "rentTime": 2,
    "deliveryDate": "2025-11-30",
    "comment": "Оставить у двери",
    "color": ["GREY"]
}

ORDER_DATA_BOTH = {
    "firstName": "Сергей",
    "lastName": "Сергеев",
    "address": "Москва, пр. Мира, 25",
    "metroStation": 6,
    "phone": "+7 916 555 44 33",
    "rentTime": 4,
    "deliveryDate": "2025-10-15",
    "comment": "Доставить до 18:00",
    "color": ["BLACK", "GREY"]
}

ORDER_DATA_NO_COLOR = {
    "firstName": "Анна", 
    "lastName": "Смирнова",
    "address": "Москва, ул. Тверская, 15",
    "metroStation": 7,
    "phone": "+7 495 111 22 33",
    "rentTime": 1,
    "deliveryDate": "2025-09-20",
    "comment": "Без комментариев"
}