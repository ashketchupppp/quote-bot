from discord.ext import commands

class QuoteCommands(commands.Cog):
  def __init__(self, bot, quotes):
      self.bot = bot
      self.quotes = quotes

  @commands.command(name='create-quote')
  async def createQuote(self, ctx, user, quote):
    self.quotes.create_quote(user, quote, ctx.guild)
    await ctx.send(f'Created a new quote for {user}')

  @commands.command(name='get-quote')
  async def getQuote(self, ctx, user):
    quote = self.quotes.get_random_quote(user)
    if quote:
      await ctx.send(f'{quote["user"]}: `{quote["quote"]}`')
    else:
      await ctx.send(f'Unable to find a quote from {user}')

  @getQuote.error
  @createQuote.error
  async def standard_errors(self, ctx, error):
      await ctx.send(error)
      print(error)