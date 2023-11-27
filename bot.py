import os

import discord
from dotenv import load_dotenv
import createImage
import keepAlive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/mergerequest'):
        imgtext = (message.content)[14:]
        createImage.createImage(imgtext)
        with open("output.jpg", "rb") as fh:
            f = discord.File(fh, filename="output.jpg")
            await message.channel.send(file=f)
            # await message.channel.send(message.content)
        # await message.channel.send('Hello!')

keepAlive.keep_alive()
client.run(TOKEN)