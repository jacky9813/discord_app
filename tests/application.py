
from os import environ as ENV  # For importing test secrets

import discord_app.application
import discord_app.command
import discord_app.discord_types
import discord_app.emoji
import discord_app.user
import discord_app.channel
import discord_app.interaction


app = discord_app.application.Application.from_basic_data(
    ENV.get("DISCORD_APP_ID"),
    ENV.get("DISCORD_APP_PUBLIC_KEY"),
    ENV.get("DISCORD_APP_BOT_TOKEN")
)


def test_application() -> None:
    assert app.id == ENV.get("DISCORD_APP_ID")
