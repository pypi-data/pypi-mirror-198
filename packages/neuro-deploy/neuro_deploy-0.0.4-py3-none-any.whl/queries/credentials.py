import sys
import json


from utils import query
from process import nd_access
from process import nd_config
from process.nd_token import token_headers


def get():
    conf = nd_config.read_saved_config()
    main_url = conf["url"]
    url = main_url + "/credentials"
    headers = nd_access.auth_headers()
    headers.update(token_headers())

    response_data = query.get(url, headers)

    return response_data


# print(get())


def create(credentials_name, credentials_desc):
    conf = nd_config.read_saved_config()
    main_url = conf["url"]
    url = main_url + "/credentials"
    headers = nd_access.auth_headers()
    headers.update(token_headers())
    headers["credential_name"] = credentials_name
    headers["description"] = credentials_desc
    data = None
    response_data = query.post(url, data, headers)

    return response_data


# print(create('test3','fff'))


def delete(credentials_name):
    conf = nd_config.read_saved_config()
    main_url = conf["url"]
    url = main_url + "/credentials" + "/" + credentials_name
    headers = nd_access.auth_headers()
    headers.update(token_headers())
    response_data = query.delete(url, headers)

    return response_data


# print(delete('test3'))
