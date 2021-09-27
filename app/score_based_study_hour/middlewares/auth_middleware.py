import os
import json
import requests
from flask import request, g
from sqlalchemy.sql.expression import true

from ..handlers.exceptions import InternalServerError, InvalidPermissions

def auth_routes():
    base_url = os.environ.get('baseurl')
    prediction = f"{base_url}api/v1/prediction/"
    
    url = request.url

    if(url.startswith(f"{prediction}")):
        return true

def authenticate_user():
    if(auth_routes()):
        try:
            token = request.headers.get('Authorization').split()[1]

            url = 'http://studaid-gateway.herokuapp.com/api/v1/auth/permissions'
            headers = {'Authorization': f'Bearer {token}'}
                        
            response = requests.get(url, headers=headers).text
            jsonResponse = json.loads(response)
            if 'error' in jsonResponse.keys():
                message = jsonResponse['message']
                raise InvalidPermissions(f'{message}')

            g.user_id = jsonResponse['user']['id']

            
        except Exception as err: raise err
  
