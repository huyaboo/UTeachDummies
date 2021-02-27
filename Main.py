import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

#Bot initialization
client = Bot.commands(command_prefix = "UTD")
client.remove_command("help")

#Help command: Update as needed
@client.command()
async def help(ctx):
	help = discord.embed(
		colour = discord.colour(4359413),
		title = "Help",
		description = "THE place for managing your UTD courses. Below is a list of commands.")
	await ctx.send(embed = help)

#Loads commands from other python files
@client.command()
async def load_extension(ctx, file):
	client.load_extension(f"cogs.{file}")

#Removes commands from other python files
@client.command()
async def unload_extension(ctx, file):
	client.unload_extension(f"cogs.{file}")	

#Reads and creates commands from files listed in the cogs folder
for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		client.load_extension(f"cogs.{file[:-3]}")

#Load environment variable (Token)
load_dotenv()
TOKEN = os.getenv("CLIENT_TOKEN")

#Run bot
client.run(TOKEN)
