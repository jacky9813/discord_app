
from os import environ as ENV
from typing import Union
import pytest

from test_application import app
from discord_app import channel
from discord_app import webhook


def test_webhook() -> None:
    channel_id = ENV.get("DISCORD_TEST_TEXT_CHANNEL")
    ch_data, _ = app.call_api("GET", f"/channels/{channel_id}")
    ch = channel.Channel(_app=app, **ch_data)

    # "clyde" test
    test: Union[str, webhook.Webhook] = "test"
    with pytest.raises(ValueError):
        test = ch.create_webhook("testClYdEhahaha")

    assert test == "test"
    test = ch.create_webhook("Webhook test")

    assert test.name == "Webhook test"
    assert test.get_channel().id == channel_id

    test.delete()

    assert test._valid is False
