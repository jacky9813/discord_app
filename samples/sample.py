
import json
import logging
import dataclasses
import discord_app

from . import app_config


app = discord_app.Application.from_basic_data(
    id=app_config.APPLICATION_ID,
    public_key=app_config.PUBLIC_KEY,
    bot_token=app_config.BOT_TOKEN,
    endpoint="/api/discord/command"
)

app._flask.testing = True
app._logger.setLevel(logging.DEBUG)


@app.application_command(
    options=discord_app.ApplicationCommand(
        name="version",
        name_localizations={
            "zh-TW": "顯示程式版本"
        },
        type=discord_app.ApplicationCommandType.CHAT_INPUT,
        description="Show application version",
        description_localizations={
            "zh-TW": "顯示程式版本"
        }
    ),
    register_on_change=False
)
def show_version(_: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    return discord_app.InteractionResponse(
        type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=discord_app.InteractionResponseMessage(
            content="test application/0.0.1"
        )
    )


@app.application_command(discord_app.ApplicationCommand(**{
    "name": "mydetail",
    "name_localizations": {
        "zh-TW": "顯示個人資訊"
    },
    "type": discord_app.ApplicationCommandType.CHAT_INPUT,
    "description": "Show informations about command issuer",
    "description_localizations": {
        "zh-TW": "包含用戶名稱、ID"
    }
}), register_on_change=True)
def whoami(request: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    if request.member:
        return discord_app.InteractionResponse(
            type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=discord_app.InteractionResponseMessage(
                content=f"Username: {request.member.user.username}\nUser id: {request.member.user.id}"
            )
        )
    if request.user:
        return discord_app.InteractionResponse(
            type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=discord_app.InteractionResponseMessage(
                content=f"Username: {request.user.username}\nUser id: {request.user.id}"
            )
        )
    return discord_app.InteractionResponse(
        type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=discord_app.InteractionResponseMessage(
            content="No such data can be fetched"
        )
    )



@app.application_command(discord_app.ApplicationCommand(**{
    "name": "new_command",
    "type": discord_app.ApplicationCommandType.CHAT_INPUT,
    "description": "Test"
}), register_on_change=False)
def test(_: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    return discord_app.InteractionResponse(
        type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=discord_app.InteractionResponseMessage(
            content="just testing"
        )
    )


@app.application_command(discord_app.ApplicationCommand(
    name="debug_msg",
    type=discord_app.ApplicationCommandType.CHAT_INPUT,
    description="output interaction request as JSON in response message"
))
def appcmd_debug_msg(request: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    return discord_app.InteractionResponse(
        type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=discord_app.InteractionResponseMessage(
            content=json.dumps(
                dataclasses.asdict(
                    request,
                    dict_factory=discord_app.application.asdict_ignore_none
                ),
                indent=4
            )
        )
    )


@app.application_command(discord_app.ApplicationCommand(
    name="debug_channel",
    type=discord_app.ApplicationCommandType.CHAT_INPUT,
    description="Output channel information about this channel"
))
def appcmd_debug_channel(request: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    channel_info = request.get_channel()
    if channel_info:
        return discord_app.InteractionResponse(
            type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=discord_app.InteractionResponseMessage(
                content=json.dumps(
                    dataclasses.asdict(
                        channel_info,
                        dict_factory=discord_app.application.asdict_ignore_none
                    ),
                    indent=4
                )
            )
        )
    else:
        return discord_app.InteractionResponse(
            type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=discord_app.InteractionResponseMessage(
                content="Failed to fetch data"
            )
        )


@app.application_command(discord_app.ApplicationCommand(
    name="about_app",
    description="Display full information about this app",
    type=discord_app.ApplicationCommandType.CHAT_INPUT
))
def appcmd_about_app(_: discord_app.InteractionRequest) -> discord_app.InteractionResponse:
    return discord_app.InteractionResponse(
        type=discord_app.InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=discord_app.InteractionResponseMessage(
            content=json.dumps(
                dataclasses.asdict(
                    app,
                    dict_factory=discord_app.application.asdict_ignore_none
                ),
                indent=4
            )
        )
    )

app.run(
    host="127.0.0.1",
    port=8765,
    debug=True
)
