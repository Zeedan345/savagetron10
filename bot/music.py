import discord
from discord.ext import commands
import youtube_dl
from discord.utils import get

class music_(commands.Cog):
  def __init__(self,client):
    self.client = client
  @commands.command()
  async def test2(self, ctx):
    await ctx.send('Test is s')
  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in a Voice channel")

   # else:
   #   await ctx.author.voice.channel.move_to(ctx.author.voice.channel)
  async def disconnect(self,ctx):
    await ctx.author.voice.channel.disconnect() 


def setup(client):
  client.add_cog(music_(client))