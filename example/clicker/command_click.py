# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

import click
from slack_bolt.request.async_request import AsyncBoltRequest as Request
from slack_click import SlackClickGroup, version_option

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from .app_data import slack_commands

# -----------------------------------------------------------------------------
#
#                                 CODE BEGINS
#
# -----------------------------------------------------------------------------

# Register the "/click" command with the Slack app for async-handling


@slack_commands.register()
@click.group(name="/click", cls=SlackClickGroup)
@version_option(version="0.1.0")
@click.pass_obj
async def cli_click_group(obj: dict):
    """
    This is the Clicker /click command group
    """
    request: Request = obj["request"]
    say = request.context["say"]
    await say("`/click` command invoked without any commands or options.")


@cli_click_group.command("hello")
@click.pass_obj
async def click_hello_command(obj):
    request: Request = obj["request"]
    await request.context.say(f"Hi there <@{request.context.user_id}> :eyes:")
