import discord
from discord.ext import commands

#EXAMPLE FORMAT OF THE FILE TO PLACE YOUR COMMANDS
class Classname(commands.Cog):
	#Creates class in which to place commands
	def __init__(self, client):
		self.client = client

	#PUT THIS FOR EVENTS (replaces @client.event())
	@commands.Cog.listener()

	#PUT THIS ABOVE ANY COMMAND Y'ALL WANNA MAKE (replaces @client.command())
	@commands.command()

#PUT THIS AT THE END OF YOUR PYTHON FILE
def setup(client):
	client.add_cog(Classname(client))
