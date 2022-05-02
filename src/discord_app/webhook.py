
from dataclasses import dataclass
from typing import Any, Optional

from . import discord_types
from . import user as user_module
from . import guild as guild_module
from . import channel
from . import application


def _webhook_name_test(name: str) -> None:
    if "clyde" in name.lower():
        raise ValueError("'clyde' cannot exist in name (case-insensitive)")
    name = name.strip()
    if len(name) > 80:
        raise ValueError("name cannot longer than 80 characters.")


@dataclass
class Webhook(discord_types.DiscordDataClass):
    id: discord_types.Snowflake
    type: discord_types.WebhookType
    channel_id: discord_types.Snowflake
    name: str
    avatar: str
    application_id: discord_types.Snowflake
    guild_id: Optional[discord_types.Snowflake] = None
    user: Optional['user_module.User'] = None
    token: Optional[str] = None
    source_guild: Optional['guild_module.PartialGuild'] = None
    url: Optional[str] = None

    _app: Optional['application.Application'] = None
    _valid: Optional[bool] = True

    def __post_init__(self) -> None:
        self.type = discord_types.WebhookType(self.type)
        if isinstance(self.user, dict):
            self.user = user_module.User(**self.user)  # type: ignore[unreachable]
        if isinstance(self.source_guild, dict):
            self.source_guild = guild_module.PartialGuild(**self.source_guild)  # type: ignore[unreachable]

    def edit(self, *_: Any, name: Optional[str] = None, avatar: Optional[str] = None, channel_id: Optional[discord_types.Snowflake] = None) -> None:
        """
            Modify this webhook

            :param Optional[str] name: New name for the webhook.
            :param Optional[str] avatar: New avatar for the webhook.
            :param Optional[:py:class:`discord_types.Snowflake`] channel_id: Bind this webhook to another channel.
        """
        if self._app is None or not self._app._is_authorized:
            raise RuntimeError("Unable to create Webhook: application is not authorized.")
        if not self._valid:
            raise RuntimeError("Not a valid webhook. (Could be deleted)")
        edit_obj = {
            "name": name if name is not None else self.name,
            "channel_id": channel_id if channel_id is not None else self.channel_id
        }
        _webhook_name_test(edit_obj["name"])
        if avatar:
            edit_obj["avatar"] = avatar
        new_wh, resp = self._app.call_api(
            "PATCH",
            f"/webhooks/{self.id}",
            json=edit_obj
        )
        obj = Webhook(_app=self._app, **new_wh)
        self.__dict__.update(obj.__dict__)

    def delete(self) -> None:
        """
            Delete this webhook.
        """
        if self._app is None or not self._app._is_authorized:
            raise RuntimeError("Unable to create Webhook: application is not authorized.")
        if not self._valid:
            raise RuntimeError("Not a valid webhook. (Could be deleted)")
        self._app.call_api(
            "DELETE",
            f"/webhooks/{self.id}"
        )
        self._valid = False

    def get_channel(self) -> 'channel.Channel':
        """
            Get the binded channel object.
        """
        if self._app is None or not self._app._is_authorized:
            raise RuntimeError("Unable to create Webhook: application is not authorized.")
        chn_info, _ = self._app.call_api(
            "GET",
            f"/channels/{self.channel_id}"
        )
        return channel.Channel(_app=self._app, **chn_info)

    def get_guild(self) -> 'guild_module.Guild':
        """
            Get the guild where this webhook is binded to.
        """
        if self._app is None or not self._app._is_authorized:
            raise RuntimeError("Unable to create Webhook: application is not authorized.")
        if self.guild_id:
            guild_info, _ = self._app.call_api(
                "GET",
                f"/guilds/{self.guild_id}"
            )
            return guild_module.Guild(_app=self._app, **guild_info)
        else:
            raise ValueError("No valid guild_id in this webhook.")
