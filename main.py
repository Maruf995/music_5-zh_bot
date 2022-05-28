from config import settings
import discord
from discord.ext import commands

PREFIX = '?'
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Ехало')


bot.lavalink_nodes = [
    {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
]

bot.load_extension('dismusic')
bot.run(settings['token'])
