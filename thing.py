import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    for glyph in message.content:
        if glyph.upper() == "E":
            try:
                await client.delete_message(message)
                await client.send_message(message.channel, "%s, You did a sin..." % (message.author.mention))
            except discord.errors.NotFound:
                return

client.run("NTEwMjczNTk2Njk0ODU1Njgx.DsaGdA.v6CuC7vmYO1blIBX6hO7OQ165JE")
