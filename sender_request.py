import requests
import configuration


def post_new_order():
    url = configuration.URL + configuration.CREATE_ORDER_PATH
    body = {
        "firstName": "Петр",
        "lastName": "Петров",
        "address": "Перекресток 7-ми дорог",
        "metroStation": "5",
        "phone": "78965412369",
        "rentTime": 8,
        "deliveryDate": "2023-09-16",
        "comment": "Куда катится мир",
        "color": "BLACK"
    }

    return requests.post(url, json=body, headers=configuration.HEADERS)


def get_order_by_track(track_number):
    url = configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + "?t=" + str(track_number)
    return requests.get(url, headers=configuration.HEADERS)
