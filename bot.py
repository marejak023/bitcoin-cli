import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

RATELIMIT = 1 # Number of command limitation within PER_SECONDS time 
PER_SECONDS = 11

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Prefix used for commands
client = commands.Bot(command_prefix="btc-cli! ")

''''
Simple, plaintext Query Api commands for retrieving blockchain data https://www.blockchain.com/api/q
'''

# Current difficulty target as a decimal number
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def getdifficulty(ctx):
    request = requests.get("https://blockchain.info/q/getdifficulty")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Current block height in the longest chain
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def getblockcount(ctx):
    request = requests.get("https://blockchain.info/q/getblockcount")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Hash of the latest block
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def latesthash(ctx):
    request = requests.get("https://blockchain.info/q/latesthash")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Current block reward in BTC
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def btcperblock(ctx):
    request = requests.get("https://blockchain.info/q/bcperblock")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Total Bitcoins in circulation (delayed by up to 1 hour)
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def totalbtc(ctx):
    request = requests.get("https://blockchain.info/q/totalbc")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Probability of finding a valid block each hash attempt
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def probability(ctx):
    request = requests.get("https://blockchain.info/q/probability")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Average number of hash attempts needed to solve a block
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def hashestowin(ctx):
    request = requests.get("https://blockchain.info/q/hashestowin")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Block height of the next difficulty re-target
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def nextretarget(ctx):
    request = requests.get("https://blockchain.info/q/nextretarget")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Average transaction size for the past 1000 blocks. Change the number of blocks by passing an integer as the second argument e.g. avgtxsize/2000
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def avgtxsize(ctx):
    request = requests.get("https://blockchain.info/q/avgtxsize")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Average transaction value (1000 Default)
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def avgtxvalue(ctx):
    request = requests.get("https://blockchain.info/q/avgtxvalue")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Average time between blocks in seconds
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def interval(ctx):
    request = requests.get("https://blockchain.info/q/interval")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Estimated time until the next block (in seconds)
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def eta(ctx):
    request = requests.get("https://blockchain.info/q/eta")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Average number of transactions per block (100 Default)
@client.command()
@commands.cooldown(RATELIMIT, PER_SECONDS, commands.BucketType.default)
async def avgtxnumber(ctx):
    request = requests.get("https://blockchain.info/q/avgtxnumber")
    print(request)
    print(request.content)
    await ctx.send(request.content)

# Displaying time of commands cooldown
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds')

client.run(BOT_TOKEN)