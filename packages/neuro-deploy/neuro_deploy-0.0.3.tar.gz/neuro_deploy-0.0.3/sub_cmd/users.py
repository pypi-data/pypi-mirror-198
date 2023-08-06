#!/usr/bin/python
from typing import Optional
import typer
from rich import print
import neuro_deploy
import process.nd_config as config


user_app = typer.Typer()


@user_app.callback()
def user_callback():
    print("Running a user command")


@user_app.command("login")
def user_login(user_name: str = typer.Option(...), password: str = typer.Option(...)):
    """
    #user create
    """
    conf = config.read_saved_config()
    neuro_deploy.users.login(user_name, password, conf["url"])
    print("[green]Token saved after login[/green] ")
