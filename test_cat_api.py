import pytest
from cat_api import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('cat_api.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'url': 'https://cdn2.thecatapi.com/images/abc.jpg'
    }]

    url = get_random_cat_image()
    assert url == 'https://cdn2.thecatapi.com/images/abc.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('cat_api.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    url = get_random_cat_image()
    assert url is None
