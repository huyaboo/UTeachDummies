import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


def main():
	# Bot initialization
	client = commands.Bot('UTD')
	client.remove_command("help")

	# Help command: Update as needed
	@client.command()
	async def help(ctx):
		await ctx.send(embed=discord.Embed(
			color=4359413,
			title='Help',
			description='THE place for managing your UTD courses. Below is a list of commands.'
		))

	# Loads commands from other python files
	@client.command('load')
	async def load_extension(ctx, file):
		client.load_extension(f"cogs.{file}")

	# Removes commands from other python files
	@client.command('unload')
	async def unload_extension(ctx, file):
		client.unload_extension(f"cogs.{file}")

	# Reads and creates commands from files listed in the cogs folder
	for file in os.listdir("./cogs"):
		if file.endswith(".py"):
			try:
				client.load_extension(f"cogs.{file[:-3]}")
			except:
				print(f'failed to load cog {file}')

	# Load environment variable (Token)
	load_dotenv()
	TOKEN = os.getenv("CLIENT_TOKEN")

	# Run bot
	client.run(TOKEN)


if __name__ == "__main__":
	main()
