import discord
from discord.ext import commands
from discord.utils import get
import asyncio

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('bot is ready')
    
    
@client.event
async def on_member_join(member):
    print(f'(member) joina w walla kahboun')
    
    
@client.event
async def on_member_remove(member):
        print(f'(member)khraj yaatih aasba')
        

@client.command()
async def aasba(ctx):
    await ctx.send('yaatek aasba!')
    
    

@client.command()
async def aasbaenh(ctx,target:discord.Member):
    await ctx.send('yaatek aasba ala sormek ya!' + target.mention)    
    
  
                
@client.command()
async def nhebnalaab(ctx):
    await ctx.send('@everyone ya malhet chkn yalaab')
                

client.run('NzY5MzAyOTY3ODAzMTgzMTI0.X5NDOA.BlB4R8IEEmCgQNOWcy9ml1EN5Dk')   