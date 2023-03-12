import asyncio
import json
import logging
import os
import random
import typing
from pathlib import Path
from datetime import datetime

import discord
from discord.ext import commands, tasks
from discord.utils import get

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="a!",
    intents=intents,
    status=discord.Status.online,
    sync_commands=True,
    delete_not_existing_commands=True,
    case_insensitive=True,
    help_command=None
)
bot.persistent_views_added = False


@bot.event
async def on_ready():
    now = datetime.now()
    print("-----------------------------------------------------")
    print("VERBUNDENER DISCORD BOT")
    print(f"Bot wurde gestartet um {now.strftime('%H:%M:%S %d-%m-%Y')}")
    print(f"Eingeloggt als: {bot.user.name}")
    print(f"ID: {bot.user.id}")
    print(f"VERSION: {discord.__version__}")


@tasks.loop(minutes=5)
async def change_status():
    activity_list = [
        "DM me '?support'",
        "Schreibe mir '?support'",
        "Spielt ein Game"
    ]
    await bot.change_presence(activity=discord.Game(random.choice(activity_list)))


# Load extensions
cogs_folder = "cogs"
if __name__ == '__main__':
    print('Starting bot...')
    cogs = [p.stem for p in Path('cogs').glob('**/*.py') if not p.name.startswith('___')]
    print(f'Loading {len(cogs)} extensions...')

    for cog in cogs:
        try:
            bot.load_extension(f'cogs.{cog}')
            print(f'Loaded {cog}')
        except Exception as e:
            print(f'Failed to load extension {cog}: {e}')


# Load config data
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

token = configData["Token"]

bot.run(token)