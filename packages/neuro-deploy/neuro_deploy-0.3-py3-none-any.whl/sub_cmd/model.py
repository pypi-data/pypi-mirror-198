#!/usr/bin/python
from typing import Optional
import typer
import time
from rich import print

from neuro_deploy import model

model_app = typer.Typer()


@model_app.callback()
def model_callback():
    print("Running a model command")


@model_app.command("push")
def model_push(
    model_name: str = typer.Option(..., help="Your model name"),
    file_path: str = typer.Option("None", help="Your model file path on your computer"),
    model_type: str = typer.Option("tensorflow", help="Your model library"),
    model_persistance_type: str = typer.Option(
        "h5", help="Your model persistance type"
    ),
):
    """
    #model create update
    """
    resp = model.create_update(
        model_name, file_path, model_type, model_persistance_type
    )
    print(resp)


@model_app.command("delete")
def model_delete(model_name: str = typer.Option(..., help="Your model name to delete")):
    """
    #model delete
    """
    resp = model.delete(model_name)
    print(resp)


@model_app.command("get")
def model_get(model_name: str = typer.Option(..., help="Your model name to get info")):
    """
    #model get
    """
    resp = model.get(model_name)
    print(resp)


@model_app.command("list")
def models_list():
    """
    #model get
    """
    resp = model.list()
    print(resp)


@model_app.command("predict")
def model_predict(
    model_name: str = typer.Option(..., help="Your model name"),
    user_name: str = typer.Option(..., help="Your user name"),
    data: str = typer.Option(..., help="Your payload"),
):
    """
    #model predict
    """
    resp = model.predict(user_name, model_name, data)
    print(resp)
