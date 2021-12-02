import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

client = commands.Bot(command_prefix='-', intents= discord.Intents.all())
TOKEN = os.getenv("DISCORD_TOKEN")
cogs = ['Basic','music']
client.lava_nodes = [
  {
    'host': 'lava.link',
    'port': 80,
    'rest_uri' : f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region': 'singapore'
  }
]

@client.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    client.load_extension('dismusic')
    print('Loading Cogs.....')
    for cog in cogs:
        try:
            client.load_extension(cog)
            print(cog + " was Loaded")

        except Exception as e:
            print(e) 

@client.command()
async def ping(ctx):
    await ctx.send("pong")

server.server()
client.run(TOKEN)
