import sys
import json
from pathlib import Path

sys.path.append(str(Path(".").absolute()))


from utils import query
from utils import file

from process import nd_config
from process import nd_access
from process.nd_token import token_headers


def create_update(
    model_name, model_file_path="None", model_type="tensorflow", persistance_type="h5"
):
    conf = nd_config.read_saved_config()
    main_url = conf["url"]
    url = main_url + "/" + "ml-models/" + model_name
    params = {}
    params["model_type"] = model_type
    params["persistence_type"] = persistance_type
    headers = nd_access.auth_headers()
    headers.update(token_headers())

    response_data = query.put(url, headers, params)
    if model_file_path != "None":
        resp = file.upload_file(response_data, model_file_path)
        return resp
    return {"message": "your model params updated ", "status_code": "200"}


def delete(model_name):
    conf = nd_config.read_saved_config()
    main_url = conf["url"]

    url = main_url + "/ml-models" + "/" + model_name
    headers = nd_access.auth_headers()
    headers.update(token_headers())

    response_data = query.delete(url, headers)
    return {"message": response_data["message"], "status_code": "200"}


def list():
    conf = nd_config.read_saved_config()
    main_url = conf["url"]

    url = main_url + "/ml-models"
    headers = nd_access.auth_headers()
    headers.update(token_headers())

    response_data = query.get(url, headers)
    return response_data


def get(model_name):
    conf = nd_config.read_saved_config()
    main_url = conf["url"]

    url = main_url + "/ml-models" + "/" + model_name
    headers = nd_access.auth_headers()
    headers.update(token_headers())

    response_data = query.get(url, headers)
    return response_data


def predict(user_name, model_name, data):
    conf = nd_config.read_saved_config()
    main_url = conf["url_api"]
    url = main_url + "/" + user_name + "/" + model_name
    headers = nd_access.auth_headers()
    headers.update(token_headers())
    j = data
    response_data = query.post(url, j, headers)
    return response_data
