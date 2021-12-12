import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='-', intents= intents)
TOKEN = os.getenv("DISCORD_TOKEN")
client.remove_command('help')
cogs = ['Basic','music','help']
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
    print(f"Logged in as {client.user.name}({client.user.id})")
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
