import requests
import time
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
bot.remove_command("help")
token = input("Enter Bot Token: ")
@bot.command()
async def twentyonesix(ctx):
    await ctx.send("And he said unto me, It is done. I am Alpha and Omega, the beginning and the end. I will give unto him that is athirst of the fountain of the water of life freely.")
    print("sent")
bot.run()
