import os
import discord
import random
import time
import requests
import json
from replit import db
from discord.ext import commands


class help_(commands.Cog):
  def __init__(self,client):
    self.client = client
  @commands.group(invoke_without_command=True )
  async def help(self,ctx):
    hm= discord.Embed(title='Help', description = 'For details of a specific feature type help<command>')
    hm.add_field(name='Basic',value='hello\nroast')
    hm.add_field(name='memes',value='memes\nshitpost\nretardmemes')
    hm.add_field(name='music',value = 'con\nplay\ndisconnect\nequilizer\nvolume\npause\nresume')
    await ctx.send(embed=hm)
  @help.command()
  async def hello(self,ctx):
    hm= discord.Embed(title='Hello')
    hm.add_field(name='**Syntax**', value = '-hello')
    await ctx.send(embed=hm)
  @help.command()
  async def roast(self,ctx):
    hm= discord.Embed(title='roast', description='Roasts A person Savagly')
    hm.add_field(name='**Syntax**', value = '-hello @<username>')
    await ctx.send(embed=hm)
  @help.command()
  async def con(self,ctx):
    hm= discord.Embed(title='connect', description='Connects to a Voice channel')
    hm.add_field(name='**Syntax**', value = '-con Make sure you are in a voice channel')
    await ctx.send(embed=hm)
  @help.command()
  async def play(self,ctx):
    hm= discord.Embed(title='play',description='Plays a song')
    hm.add_field(name='**Syntax**', value = '-play <song name>')
    await ctx.send(embed=hm)
  @help.command()
  async def disconnect(self,ctx):
    hm= discord.Embed(title='disconnect',description='Disconnects the bot from a voice channel')
    hm.add_field(name='**Syntax**', value = '-disconnect')
    await ctx.send(embed=hm)
  @help.command()
  async def equilizer(self,ctx):
    hm= discord.Embed(title='equilizers',description='Control the Bass and other things of music')
    hm.add_field(name='**Syntax**', value = '-eq')
    await ctx.send(embed=hm)
  @help.command()
  async def volume(self,ctx):
    hm= discord.Embed(title='volume',description='Controls the volume of the song')
    hm.add_field(name='**Syntax**', value = '-volume <value>')
    await ctx.send(embed=hm)
  @help.command()
  async def pause(self,ctx):
    hm= discord.Embed(title='pause',description='Pause the song currently playing')
    hm.add_field(name='**Syntax**', value = '-pause')
    await ctx.send(embed=hm)
  @help.command()
  async def resume(self,ctx):
    hm= discord.Embed(title='resume',description='Resumes the song that was paused')
    hm.add_field(name='**Syntax**', value = '-disconnect')
    await ctx.send(embed=hm)
  @help.command()
  async def memes(self,ctx):
    hm= discord.Embed(title='memes',description='Shows Random memes from r/memes')
    hm.add_field(name='**Syntax**', value = '-memes')
    await ctx.send(embed=hm)
  @help.command()
  async def shitpost(self,ctx):
    hm= discord.Embed(title='shitpost',description='Shows Random memes from r/shitpost')
    hm.add_field(name='**Syntax**', value = '-sitpost')
    await ctx.send(embed=hm)  
  @help.command()
  async def retardmemes(self,ctx):
    hm= discord.Embed(title='reatradmemes',description='Shows Random memes from r/reatrdmemes')
    hm.add_field(name='**Syntax**', value = '-retardmemes')
    await ctx.send(embed=hm)

def setup(client):
  client.add_cog(help_(client))