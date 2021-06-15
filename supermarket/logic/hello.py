"""Logic for Hello."""
from oto import response


def say_hello(name=None):
    """Application health check.
    Args:
        name (str): the name to display alongside the Hello.
    Returns:
        Response: the hello message.
    """
    if not name or isinstance(name, str) and not name.strip():
        return response.Response('Hello')

    return response.Response('Hello {}!'.format(name))
