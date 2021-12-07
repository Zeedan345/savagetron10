import os
import discord
import random
import time
import requests
import json
from discord.ext import commands


class Basic_(commands.Cog):
  def __init__(self,client):
    self.client = client
  @commands.command()
  async def hello(self, ctx):
    await ctx.send("No :sunglasses:\nhttps://tenor.com/view/savage-squad-burn-gif-11523021")
  @commands.command()
  async def roast(self, ctx):
    arth = ctx.message.author
    roast = ctx.message.content.split('-roast ', 1)[1]
    rs = roast.split('@',1)[1]
    await ctx.send(roast) 
    time.sleep(2)
    await ctx.send(roast)
    time.sleep(2)
    await ctx.send(roast)
    def check(m):
      return m.author == arth 

    msg = await self.client.wait_for('message', check=check)
    await ctx.send('Nothing :sunglasses:\nhttps://tenor.com/view/savage-squad-burn-gif-11523021')  
      

  @commands.command()
  async def memes(self,ctx):

   r = requests.get("https://memes.blademaker.tv/api?lang=en")
   res = r.json()
   title = res['title']
   ups = res['ups']
   downs = res['downs']
   sub = res['subreddit']
   m = discord.Embed(title = f'{title}\nSubreddit: {sub}')
   m.set_image(url= res['image'])
   m.set_footer(text=f'👍:{ups} 👎:{downs}') 
   await ctx.send(embed = m)

  @commands.command()
  async def shitpost(self,ctx):
   q = requests.get("https://memes.blademaker.tv/api/shitposting")
   qes = q.json()
   qtitle = qes['title']
   qups = qes['ups']
   qdowns = qes['downs']
   qsub = qes['subreddit']
   w = discord.Embed(title = f'{qtitle}\nSubreddit: {qsub}')
   w.set_image(url= qes['image'])
   w.set_footer(text=f'👍:{qups} 👎:{qdowns}')
   await ctx.send(embed = w)
   
  @commands.command()
  async def retardmemes(self,ctx):
   s = requests.get("https://memes.blademaker.tv/api/okbuddyretard")
   ses = s.json()
   stitle = ses['title']
   sups = ses['ups']
   sdowns = ses['downs']
   ssub = ses['subreddit']
   f = discord.Embed(title = f'{stitle}\n Subreddit: {ssub}')
   f.set_image(url= ses['image'])
   f.set_footer(text=f'👍:{sups} 👎:{sdowns}')
   await ctx.send(embed=f)
  @self.client.group(invoke_without_command=True )
  async def help(self,ctx):
    hm= discord.Embed(title='Help', description = 'For details of specific feature type help<command>')
    hm.add_field(name='Basic',value='Hello','roast')
    hm.add_field(name='memes',value='memes','shitpost','retardmemes')
    hm.add_field(name='music',value = 'con','play','disconnect','equilizer','volume','pause','resume')
    await ctx.send(embed=hm)
  @help.command()
  async def Hello(self,ctx):
    hm= discord.Embed(title='Hello')
    hm.add_field(name='**Syntax**', value = '-hello')
  @help.command()
  async def roast(self,ctx):
    hm= discord.Embed(title='roast', description='Roasts A person Savagly')
    hm.add_field(name='**Syntax**', value = '-hello @<username>')
  @help.command()
  async def con(self,ctx):
    hm= discord.Embed(title='connect', description='Connects to a Voice channel')
    hm.add_field(name='**Syntax**', value = '-con Make sure you are in a voice channel')
  @help.command()
  async def play(self,ctx):
    hm= discord.Embed(title='play',description='Plays a song')
    hm.add_field(name='**Syntax**', value = '-play <song name>')
  @help.command()
  async def disconnect(self,ctx):
    hm= discord.Embed(title='disconnect',description='Disconnects the bot from a voice channel')
    hm.add_field(name='**Syntax**', value = '-disconnect')
  @help.command()
  async def equilizer(self,ctx):
    hm= discord.Embed(title='equilizers',description='Control the Bass and other things of music')
    hm.add_field(name='**Syntax**', value = '-eq')
  @help.command()
  async def volume(self,ctx):
    hm= discord.Embed(title='volume',description='Controls the volume of the song')
    hm.add_field(name='**Syntax**', value = '-volume <value>')
  @help.command()
  async def pause(self,ctx):
    hm= discord.Embed(title='pause',description='Pause the song currently playing')
    hm.add_field(name='**Syntax**', value = '-pause')
  @help.command()
  async def resume(self,ctx):
    hm= discord.Embed(title='resume',description='Resumes the song that was paused')
    hm.add_field(name='**Syntax**', value = '-disconnect')
  @help.command()
  async def memes(self,ctx):
    hm= discord.Embed(title='memes',description='Shows Random memes from r/memes')
    hm.add_field(name='**Syntax**', value = '-memes')
  @help.command()
  async def shitpost(self,ctx):
    hm= discord.Embed(title='shitpost',description='Shows Random memes from r/shitpost')
    hm.add_field(name='**Syntax**', value = '-sitpost')  
  @help.command()
  async def retardmemes(self,ctx):
    hm= discord.Embed(title='reatradmemes',description='Shows Random memes from r/reatrdmemes')
    hm.add_field(name='**Syntax**', value = '-retardmemes')
  

def setup(client):
  client.add_cog(Basic_(client))
