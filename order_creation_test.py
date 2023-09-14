import sender_request


def test_order_creation_and_retrieval():
    response = sender_request.post_new_order()
    assert response.status_code == 201, "Expected 201, but got {}".format(response.status_code)
    track_number = response.json()["track"]

    response = sender_request.get_order_by_track(track_number)

    assert response.status_code == 200, "Expected 200, but got {}".format(response.status_code)


# Комова Наталия, 8-я когорта — Диплом. Инженер по тестированию +.