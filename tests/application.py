
from os import environ as ENV  # For importing test secrets

import discord_app.application


app = discord_app.application.Application.from_basic_data(
    ENV.get("DISCORD_APP_ID"),  # type: ignore[arg-type]
    ENV.get("DISCORD_APP_PUBLIC_KEY"),  # type: ignore[arg-type]
    ENV.get("DISCORD_APP_BOT_TOKEN")  # type: ignore[arg-type]
)


def test_application() -> None:
    assert app.id == ENV.get("DISCORD_APP_ID")  # type: ignore[attr-defined]
