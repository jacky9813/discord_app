
from os import environ as ENV

from discord_app import channel
from test_application import app


def test_channel_post_message() -> None:
    channel_id = ENV.get("DISCORD_TEST_TEXT_CHANNEL")
    ch_data, _ = app.call_api("GET", f"/channels/{channel_id}")
    ch = channel.Channel(_app=app, **ch_data)
    msg = ch.post_message(
        content="Test content 1"
    )
    assert isinstance(msg, channel.Message)
    assert msg.content == "Test content 1"

    msg.edit(content="Changed content test.")

    assert msg._valid
    assert msg.content == "Changed content test."

    msg.delete()

    assert msg._valid is False

    msg_chn = msg.get_channel()  # type: ignore[unreachable]

    assert msg_chn.id == channel_id
