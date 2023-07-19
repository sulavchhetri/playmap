"""
    This module is test the utils module of the flask folder
"""
from src.app import app
from src.utils import (
    generate_cookie,
    success_return,
    error_return,
)


def test_generate_cookie():
    """
        This function is used to test the get_cookie function which returns the
        cookie,

        In first case, we only checksif the generated cookie is of type str or not
        because the generated cookie is completely random and unique
    """
    result = generate_cookie()
    assert result
    assert isinstance(result, str)


def test_success_return():
    """
        This function is used to test whether data is correctly returned
        or not.
    """
    with app.app_context():
        data = {
            "data": [],
            "index": 0
        }
        result = success_return(data)
        assert result.get_json() == {'data': {'data': [], 'index': 0}}


def test_error_return():
    """
        This function is used to test whether data is correctly returned
        or not.
    """
    with app.app_context():
        message = "Error No task present with this id has occured"
        result = error_return(message)
        assert result.get_json() == {'error': {
            'code': 404, 'message': 'Error Error No task present with this id has occured has occured'}}


if __name__ == "__main__":
    test_generate_cookie()
    test_success_return()
    test_error_return()
