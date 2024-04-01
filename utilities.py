import requests
import os
import json
from server import USERSOCIAL_URL_BASE,COMMENTS_URL_BASE
GET="GET"
POST="POST"
PATCH="PATCH"
PUT="PUT"
DELETE="DELETE"
def generalRequest(url, method, body=None, full_response=False):
    headers = {'Content-Type': 'application/json'}
    if os.getenv('SHOW_URLS'):
        print(url)

    try:
        if method == GET:
            response = requests.get(url, headers=headers)
        elif method == POST:
            response = requests.post(url, json=body, headers=headers)
        elif method == PATCH:
            response = requests.patch(url, json=body, headers=headers)
        elif method == PUT:
            response = requests.put(url, json=body, headers=headers)
        elif method == DELETE:
            response = requests.delete(url, headers=headers,json=body)
        else:
            raise ValueError(f'Invalid method: {method}')
        return response.json()
    except requests.exceptions.RequestException as err:
        return str(err)

def serialize_to_dict(json_object):
    return json.loads(json_object)
def userExists(userId)->bool:
    user=generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={userId}",GET)
    if("error" in user):
        return False
    return True
def commentExists(commentId)->bool:
    comment=generalRequest(f"{COMMENTS_URL_BASE}comments/{commentId}",GET)
    if("message" in comment): return False
    return True