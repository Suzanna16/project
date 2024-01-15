# Сюзанна Ширинян, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Запрос на создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=order_body)

#  Запрос на получение информации о заказе по треку заказа
def get_order_information_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.INFORMATION_ABOUT_THE_ORDER + str(track))

# Автотест
def test_get_order_information_by_track():
    track = create_order(data.order_body).json()['track']
    response = get_order_information_by_track(track)
    assert response.status_code == 200