import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
import json 

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
            configData = json.load(f)

else:
    configTemplate =  {"Token": "", "Prefix": "a!"}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)


token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(
     command_prefix=prefix,
     intents=discord.Intents.all(),
     status=discord.Status.online,
     sync_commands=False,
     delete_not_existing_commands=False
     )

@bot.event
async def on_ready():
    print("Bot is online!")
    try:
         synced = await bot.tree.sync()
         print(f"Synced {len(synced)} command(s)")
    except Exception as e:
         print(e)

         
@bot.command()
async def ping(ctx):
     latency = round(bot.latency*1000, 1)
     await ctx.send(f"🏓 Pong! **{latency}ms**")

cogs = [p.stem for p in Path('cogs').glob('**/*.py') if not p.name.startswith('_____')]
log.info('Loading %d extensions...', len(cogs))
for cog in cogs:
bot.load_extension (f'cogs. {cog}')
log.info('Loaded %s', cog)

bot.run(token)