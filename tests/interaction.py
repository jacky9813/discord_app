
import discord_app.interaction
import discord_app.application
import discord_app.discord_types
import discord_app.channel

import dataclasses


def test_command_1() -> None:
    spec = {
        "name": "test_command",
        "description": "test function description",
        "name_localizations": {
            "zh-TW": "測試指令"
        },
        "description_localizations": {
            "zh-TW": "測試指令說明"
        },
        "id": 98765432109876543210,
        "application_id": 12345678901234567890,
        "type": 1,
        "guild_id": 11223344556677889900,
        "default_permission": True,
        "version": 11122233344455566677,
        "options": [
            {
                "name": "test_command_option_1",
                "description": "test function option 1",
                "type": 3,
                "name_localizations": {
                    "zh-TW": "測試指令參數1"
                },
                "description_localizations": {
                    "zh-TW": "測試指令參數1 說明"
                },
                "required": True,
                "autocomplete": True,
                "choices": [
                    {
                        "name": "test_command_option_1_choice_1",
                        "name_localizations": {
                            "zh-TW": "測試指令參數1選項1"
                        },
                        "value": "choice_1"
                    }
                ]
            }
        ]
    }

    a = discord_app.interaction.ApplicationCommand(**spec)  # type: ignore[arg-type]
    b = dataclasses.asdict(a, dict_factory=discord_app.application.asdict_ignore_none)
    c = discord_app.interaction.ApplicationCommand(**b)

    assert a == c
    assert a.type is discord_app.discord_types.ApplicationCommandType.CHAT_INPUT
    assert type(a.options[0]) == discord_app.interaction.ApplicationCommandOption  # type: ignore[index]
    assert type(a.options[0].choices[0]) == discord_app.interaction.ApplicationCommandOptionChoice  # type: ignore[index]


def test_command_2() -> None:
    a = discord_app.interaction.ApplicationCommandOption(
        name="Option",
        description="option group test",
        type=discord_app.discord_types.ApplicationCommandOptionType.SUB_COMMAND,
        required=True,
        options=[
            discord_app.interaction.ApplicationCommandOption(
                name="Sub_Option",
                description="sub option test",
                type=discord_app.discord_types.ApplicationCommandOptionType.STRING
            ),
            discord_app.interaction.ApplicationCommandOption(
                name="Sub channel option",
                description="channel as an option",
                type=discord_app.discord_types.ApplicationCommandOptionType.CHANNEL,
                channel_types=[
                    discord_app.discord_types.ChannelType.GUILD_VOICE,
                    discord_app.discord_types.ChannelType.GUILD_STAGE_VOICE
                ]
            )
        ]
    )
    b = discord_app.interaction.ApplicationCommandOption(**{  # type: ignore[arg-type]
        "name": "Option",
        "description": "option group test",
        "type": 1,
        "required": True,
        "options": [
            {
                "name": "Sub_Option",
                "description": "sub option test",
                "type": 3
            }, {
                "name": "Sub channel option",
                "description": "channel as an option",
                "type": 7,
                "channel_types": [2, 13]
            }
        ]
    })

    c = discord_app.interaction.ApplicationCommandOption(**{  # type: ignore[arg-type]
        "name": "Option",
        "description": "option group test",
        "type": 1,
        "required": True,
        "options": [
            {
                "name": "Sub_Option",
                "description": "sub option test",
                "type": 3
            }, {
                "name": "Sub channel option",
                "description": "channel as an option",
                "type": 7,
                "channel_types": [2, 14]
            }
        ]
    })

    assert a == b
    assert a != c


def test_create_from_parent_class() -> None:
    a = discord_app.interaction.InteractionResponseData(
        content="test"
    )
    assert isinstance(a, discord_app.interaction.InteractionResponseMessage)
    assert isinstance(a, discord_app.interaction.InteractionResponseData)

    b = discord_app.interaction.InteractionResponseModal(
        custom_id="test_id",
        title="Test title",
        components=[
            discord_app.channel.MessageComponentButton(
                style=discord_app.discord_types.MessageComponentButtonStyle.PRIMARY,
                label="Test",
                custom_id="btn_test_id",
                type=discord_app.discord_types.MessageComponentType.BUTTON
            )
        ]
    )
    assert isinstance(b, discord_app.interaction.InteractionResponseModal)
    assert isinstance(b, discord_app.interaction.InteractionResponseData)
