import json
import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute()))

from utils import query
from process import nd_access
from process import nd_token


def subscribe(username, password, email, main_url, dire=".nd", name="secrets"):
    url = main_url + "/sign-up"
    headers = {}
    headers["username"] = username
    headers["password"] = password
    headers["email"] = email
    data = None
    response_data = query.post(url, data, headers)
    if "Error" not in response_data:
        nd_access.save_access(response_data, dire, name)

    return response_data


def login(username, password, main_url):
    url = main_url + "/sign-in"
    headers = {}
    headers["username"] = username
    headers["password"] = password
    data = None
    response_data = query.post(url, data, headers)
    resp = nd_token.save_token(response_data)

    return resp
