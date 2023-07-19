"""
    This function is used to provide utility functions to the
    flask app
"""
import secrets
import string

def success_return(data):
    """
        This function is used to return the success message
        api
    """
    return {
        "data": data,
    }


def generate_cookie():
    """
        This function is used to generate the cookie key
    """
    return str(''.join(secrets.choice(string.ascii_uppercase + string.digits)
                       for _ in range(16)))


def error_return(error):
    """
        This function is used to return the error message
        api
    """
    return {
        "error": {
            "code": 404,
            "message": error}
    }