import asyncio
from discord.ext.commands import Bot
import random
import requests
import time
import base64



BOT_PREFIX = ("!", "?", ">")
PECKY  = base64.b64decode(b'TlRVMU5qUXpOVEE1TXpFeE5EQTJNVEF4LkQyd2lLQS5Wb1JJU3VuZHc5bWU5YThickFISE8zVWRiZ2M=').decode("utf-8") # pecky
VERIFY = base64.b64decode(b'TlRVeE5UZzJORFV6T0RNd09Ea3pOVGM1LkQxektyQS5XRGw2WGF0WkRuV3dxRkhFaVlSWk9uUF9ESlU=').decode("utf-8")  # verifybot
client = Bot(command_prefix=BOT_PREFIX)

#Ready
@client.event
async def on_ready():
    print(client.user.name + " is breathing and healthy")

# Shows prefix
@client.command(description="You can use '!' or '?' or '>' as prefix", brief='! or ? or >')
async  def prefix():
    await client.say("Prefix = '!' , '?' , '>'")

# Function to reply random message on giveme
@client.command(description="test your luck to get random things from Pecky",brief='tells you what do you get from pecky', pass_context=True)
async def giveme(context):
    possible_responses = ['you will get a diamond pickaxe', 'you are so dump so you will get nothing', 'you will get a cake','beat me if you need to get emerald','you are lucky, you will get a mclaren']
    await client.say(context.message.author.mention + " " + random.choice(possible_responses))

# Function to reply square of number
@client.command()
async def square(number):
    sqaure_value = int(number) * int(number)
    await client.say(str(number) + " Squared is " + str(sqaure_value))

# get current bitcoin value
@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json() ['bpi'] ['USD'] ['rate']
    await client.say('Bitcoin price is: $' + value)

# get current bot running servers
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        servers = []
        for server in client.servers:
            servers.append(server.name)
        print('Current servers: ' + str(servers))
        await asyncio.sleep(60*10)

client.loop.create_task(list_servers())
client.run(PECKY)
