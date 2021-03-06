
## 0.0.1-alpha.1
(2022-04-24)

Changes:
* chore: Change Python requirement to >= 3.9 (7f4ec50)
* chore: depends on Python <4 (1ec897b)
* chore: GitHub Action for publishing package (ddb5e47)
* chore: updated: flake8, pytest, mypy; removed: sphinx (da0d9db)
* docs: Added GitHub Action test result image (68bad96)
* docs: Added install from pypi section (15e21a2)
* docs: Added known limitation section (40f5ff3)
* docs: Added version badge (4a15351)
* docs: project property will show up at pypi in future release (69c961f)
* docs: Version bump (fe8865a)
* feat: All resource defined (Initial commit) (8502c59)
* feat: (guild.Ban) __post_init__ implemented (7aac0f4)
* feat: (guild.py) __post_init__ for most data classes (0527cbb)
* feat: (GuildScheduledEvent) __post_init__ implemented (b750fc3)
* feat: (GuildTemplate) __post_init__ implemented (ed0c211)
* feat: (invite.py) __post_init__ implemented (6d8932a)
* feat: (presence.py) Activity related dataclasses (9fd2cbe)
* feat: (user.Connection) __post_init__ implemented (8159270)
* feat: (VoiceState) __post_init__ implemented (72e6d34)
* feat: (Webhook) __post_init__ implemented (4d3d2ed)
* fix: Circular import when creating classes (0392142)
* fix: (Guild) now calls parent's __post_init__ (1af954b)
* fix: (pyproject.toml) invalid classifiers (c2a8dbe)
* refactor: (ApplicationCommandOption) type is not optional but with default value (aaa5ccd)
* refactor: (ApplicationCommand) type is not optional but with default value (a5dab15)
* refactor: Expected typing error changes (b7406c4)
* refactor: Guild object uses PartialVoiceState (04c2183)
* refactor: typing issue reported by mypy (24745f0)
* style: (channel.py) Message.applicaiton is PartialApplication (48be900)
* style: (guild.py) Guild.presences is PresenceUpdateEvent (f9bc253)
* style: (interaction.py) _app is now application.Application (b5662d7)
* style: (interaction.py) no type check required on required IntEnum property (c28a02f)
* style: (Role) __post_init__ removed unnecessary code (3dcb403)
* test: (application.py) remove unused imports (4c13e97)
* test: rename command.py to interaction.py (bffd3af)
* test: Specify which environment secret to use (89d80a0)
* test: Testing with GitHub Action (ca83451)

## 0.0.1-alpha.0
(2022-04-22)

Changes:
* 8502c59 feat: All resource defined (Initial commit)