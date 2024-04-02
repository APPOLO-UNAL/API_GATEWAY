import requests
import os
import json
import logging

# Constants for HTTP methods
GET = "GET"
POST = "POST"
PATCH = "PATCH"
PUT = "PUT"
DELETE = "DELETE"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generalRequest(url, method, body=None, full_response=False):
    headers = {'Content-Type': 'application/json'}
    if os.getenv('SHOW_URLS'):
        logging.info(f"Request URL: {url}")

    try:
        logging.info(f"Sending {method} request to {url} with body: {body}")
        if method == GET:
            response = requests.get(url, headers=headers)
        elif method == POST:
            response = requests.post(url, json=body, headers=headers)
        elif method == PATCH:
            response = requests.patch(url, json=body, headers=headers)
        elif method == PUT:
            response = requests.put(url, json=body, headers=headers)
        elif method == DELETE:
            response = requests.delete(url, headers=headers, json=body)
        else:
            raise ValueError(f'Invalid method: {method}')

        logging.info(f"Received response with status code: {response.status_code}")
        logging.debug(f"Response headers: {response.headers}")
        logging.debug(f"Response body: {response.text}")
        if full_response:
            return response
        else:
            return response.json()
    except requests.exceptions.RequestException as err:
        logging.error(f"HTTP Request failed: {err}")
        return None

def serialize_to_dict(json_object):
    return json.loads(json_object)