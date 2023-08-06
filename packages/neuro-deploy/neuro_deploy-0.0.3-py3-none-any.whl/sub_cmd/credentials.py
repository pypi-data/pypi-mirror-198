#!/usr/bin/python
from typing import Optional
import typer
from rich import print

from neuro_deploy import credentials

credentials_app = typer.Typer()


@credentials_app.callback()
def credentials_callback():
    print("Running a credentials command")


@credentials_app.command("create")
def credentials_create(
    credentials_name: str = typer.Option(..., help="Your credential name"),
    credentials_desc=typer.Option(..., help="Your credentials description message"),
):
    """
    #credentials create
    """
    resp = credentials.create(credentials_name, credentials_desc)
    print(resp)


@credentials_app.command("list")
def credentials_list():
    """
    #credentials delete
    """
    resp = credentials.get()
    print(resp)


@credentials_app.command("delete")
def credentials_delete(
    credentials_name: str = typer.Option(..., help="Your credential name")
):
    """
    #credentials delete
    """
    resp = credentials.delete(credentials_name)
    print(resp)
