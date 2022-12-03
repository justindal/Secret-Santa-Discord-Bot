import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

description = 'discord bot to handle our secret santa'

bot = commands.Bot(command_prefix='ss ', description=description, intents=intents)
bot.ssParticipants = dict()

@bot.event
async def on_ready():
    print(f'successfully logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('.ss hello'):
        await message.channel.send('santa time teehee')
    await bot.process_commands(message)
    

@bot.command()
async def printUsers(ctx):
    await ctx.send('current members:')
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send(member)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def join(ctx):
    # dict of message.author to message.author.id
    if ctx.author not in bot.ssParticipants:
        bot.ssParticipants[ctx.author] = ctx.author.id
        await ctx.send(f'added {ctx.author} to the list')
    else:
        await ctx.send(f'{ctx.author} is already in the list!!!!!\n shame on you')


@bot.command()
async def printParticipants(ctx):
    for i in bot.ssParticipants:
        user = bot.get_user(bot.ssParticipants[i])
        await ctx.send(user)

@bot.command() # test to see of the bot can dm a user
async def test(ctx):
    for i in bot.ssParticipants:
        user = bot.get_user(bot.ssParticipants[i])
        await user.send(user)

@bot.command()
async def start(ctx):
    await ctx.send('starting secret santa with following users:')
    printParticipants(ctx)

bot.run(TOKEN)