import os
import discord
import random
import time
import requests
import json
from replit import db
from discord.ext import commands

client= discord.Client()




@client.event
async def on_ready():
  print("Savage. Savage. Savage {0.user}"
  .format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith("-hello"):
    await message.channel.send("No :sunglasses:\nhttps://tenor.com/view/savage-squad-burn-gif-11523021")
  if message.content.startswith('noob'):
    await message.content.send('Real Noob tend to call other pro people Noob')
  
  if message.content.startswith('-roast'):
    roast = message.content.split('-roast ', 1)[1]
    rs = roast.split('@',1)[1]
    await message.channel.send(roast) 
    time.sleep(2)
    await message.channel.send(roast)
    time.sleep(2)
    await message.channel.send(roast)
    def check(m):
        return len(m.content)>0

    msg = await client.wait_for('message', check=check)
    await message.channel.send('Nothing :sunglasses:\nhttps://tenor.com/view/savage-squad-burn-gif-11523021')

  r = requests.get("https://memes.blademaker.tv/api?lang=en")
  res = r.json()
  title = res['title']
  ups = res['ups']
  downs = res['downs']
  sub = res['subreddit']
  m = discord.Embed(title = f'{title}\nSubreddit: {sub}')
  m.set_image(url= res['image'])
  m.set_footer(text=f'👍:{ups} 👎:{downs}')
  if message.content.startswith("-meme"):
    await message.channel.send(embed = m)

    msg = await client.wait_for('message', check=check)
    await message.channel.send('Nothing :sunglasses:')

  s = requests.get("https://memes.blademaker.tv/api/okbuddyretard")
  ses = s.json()
  stitle = ses['title']
  sups = ses['ups']
  sdowns = ses['downs']
  ssub = ses['subreddit']
  f = discord.Embed(title = f'{stitle}\n Subreddit: {ssub}')
  f.set_image(url= ses['image'])
  f.set_footer(text=f'👍:{sups} 👎:{sdowns}')
  if message.content.startswith('-retardmemes'):
    await message.channel.send(embed = f)

  q = requests.get("https://memes.blademaker.tv/api/shitposting")
  qes = q.json()
  qtitle = qes['title']
  qups = qes['ups']
  qdowns = qes['downs']
  qsub = qes['subreddit']
  w = discord.Embed(title = f'{qtitle}\nSubreddit: {qsub}')
  w.set_image(url= qes['image'])
  w.set_footer(text=f'👍:{qups} 👎:{qdowns}')
  if message.content.startswith('-shitpost'):
    await message.channel.send(embed = w)

  if message.content.startswith('-help'):
    await message.channel.send('-hello :.... Say hello to savagae-tron \n-roast {Username} :.... for Savagely roasting people.\n-memes :.... For Popular memes from around the web \n-shitposting :.... If your humour is lower then an egg\n-retardmemes :.... For retard which have egg') 


client.run(os.getenv('Token'))