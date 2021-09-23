import os
import pathlib
from discord.ext import commands
from dotenv import load_dotenv
import pymongo

from commands import QuoteCommands
from mongo import Quotes

envPath = pathlib.Path(__file__).parent.parent.resolve()
load_dotenv(envPath)
TOKEN = os.getenv('TOKEN')
MONGO_CONN_STR = os.getenv('MONGO_CONN_STR')

print('Connecting to mongo...')
quotes = Quotes(MONGO_CONN_STR)
print('Successful connection made to mongo')

bot = commands.Bot(command_prefix='q!')
bot.add_cog(QuoteCommands(bot, quotes))

try:
  bot.run(TOKEN)
except KeyboardInterrupt:
  print('Exiting...')
finally:
  pass
