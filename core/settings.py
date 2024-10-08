from typing import Any
from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    creator: int

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.str("ADMIN_ID"),
            creator=env.str("CREATOR"),
        )
    )

settings = get_settings('input')

adminlar = [settings.bots.admin_id,]