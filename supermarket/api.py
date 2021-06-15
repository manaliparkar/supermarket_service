"""Api.
The API application is a `flask` application. It provides simple features such
as registering a url for a specific handlers.
"""

from flask import Flask
from supermarket import config


app = Flask(config.SERVICE_NAME)
