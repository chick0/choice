from os.path import join
from json import load
from random import choice

from flask import current_app

KEY = "MENUS"


def read(app_dir: str) -> list:
    file_name = join(app_dir, "menus.json")
    return load(
        fp=open(
            file_name,
            mode="r",
            encoding="utf-8",
        )
    )


def one() -> str:
    menus = current_app.config[KEY]
    return choice(menus)


def length() -> int:
    return current_app.config[KEY].__len__()
