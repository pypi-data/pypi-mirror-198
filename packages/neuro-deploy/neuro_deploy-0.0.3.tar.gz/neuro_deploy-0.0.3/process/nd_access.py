#!/usr/bin/python
import sys
import os
import ast

import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute()))


from pathlib import Path


def save_access(data, dire=".nd", name="secrets"):
    path = str(Path.home()) + "/" + dire
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(path + "/" + name, "w")
    f.write(str(data))
    f.close()
    return "ok"


def read_saved_access(dire=".nd", name="secrets"):
    path = str(Path.home()) + "/" + dire
    f = open(path + "/" + name, "r")
    data = f.read()
    f.close()
    resp = ast.literal_eval(data)
    return resp


# print(read_saved_access())

from process import nd_access


def auth_headers():
    access = read_saved_access(dire=".nd", name="secrets")
    headers = {}
    headers["access_token"] = access["access_token"]
    headers["secret_key"] = access["secret_key"]
    return headers
