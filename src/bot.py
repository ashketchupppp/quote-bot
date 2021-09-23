import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='q!')
# bot.add_cog(Categories(bot))

try:
  bot.run(TOKEN)
except KeyboardInterrupt:
  print('Exiting...')
finally:
  pass    
  # config.store()