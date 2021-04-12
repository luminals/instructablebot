import discord
import os
from discord.ext.commands import Bot

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('%bot'):
        a = message.author.id
        await message.channel.send('<@!'+a+'>, hey! I am Instructable Bot. Your ID is '+a)


client.run('token')
