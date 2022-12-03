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
bot.ssParticipants = set()

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
    x = {}
    x[ctx.message.author] = ctx.message.author.id
    bot.ssParticipants.add(x)
    await ctx.send(f'{ctx.message.author} has joined the game!')


@bot.command()
async def printParticipants(ctx):
    for i in bot.ssParticipants:
        await ctx.send(i)

@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

bot.run(TOKEN)