#!/usr/bin/python
import os
import ast
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute()))


from pathlib import Path


def save_config(
    url="https://user-api.playingwithml.com",
    dire=".nd",
    name="config",
    url_api="https://api.playingwithml.com",
):
    path = str(Path.home()) + "/" + dire
    if not os.path.exists(path):
        os.makedirs(path)

    config = {}
    config["url"] = url
    config["url_api"] = url_api
    f = open(path + "/" + name, "w")
    f.write(str(config))
    f.close()

    return "Config saved"


save_config()


def read_saved_config(dire=".nd", name="config"):
    path = str(Path.home()) + "/" + dire
    f = open(path + "/" + name, "r")
    data = f.read()
    f.close()
    resp = ast.literal_eval(data)
    return resp


# print(read_saved_config())
