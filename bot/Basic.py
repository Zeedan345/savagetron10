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



    

  

def setup(client):
  client.add_cog(Basic_(client))
