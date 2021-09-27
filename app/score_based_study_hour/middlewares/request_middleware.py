import os
from flask import current_app, request
from sqlalchemy.sql.expression import true

from ..handlers.exceptions import InvalidContentType, InvalidPermissions

def auth_routes():
    base_url = os.environ.get('baseurl')
    prediction = f"{base_url}api/v1/prediction/"
    
    url = request.url

    if(url.startswith(f"{prediction}")):
        return true

def ensure_content_type():
    content_type = request.headers.get('Content-type')
    if(auth_routes()):
        if not content_type == 'application/json':
            raise InvalidContentType('Invalid content-type. Only `application-json` is allowed.')


def ensure_public_unavailability():
    security_key = request.headers.get('X-Api-Key', '')
    if(auth_routes()):
        if not security_key == os.environ.get('DEV_SECRET_KEY'):
            raise InvalidPermissions('You don\'t have enough permissions to perform this action.')


ACL_ORIGIN = 'Access-Control-Allow-Origin'
ACL_METHODS = 'Access-Control-Allow-Methods'
ACL_ALLOWED_HEADERS = 'Access-Control-Allow-Headers'

OPTIONS_METHOD = 'OPTIONS'
ALLOWED_ORIGINS = 'http://localhost:5000'
ALLOWED_METHODS = 'GET, POST, PUT, OPTIONS'
ALLOWED_HEADERS = 'Authorization, DNT, X-CustomHeader, Keep-Alive, User-Agent, ' \
                  'X-Requested-With, If-Modified-Since, Cache-Control, Content-Type'


def enable_cors(response):
    """
    Enable Cross-origin resource sharing.
    These headers are needed for the clients that
    will consume the API via AJAX requests.
    """
    if request.method == OPTIONS_METHOD:
        response = current_app.make_default_options_response()
    response.headers[ACL_ORIGIN] = ALLOWED_ORIGINS
    response.headers[ACL_METHODS] = ALLOWED_METHODS
    response.headers[ACL_ALLOWED_HEADERS] = ALLOWED_HEADERS

    return response
