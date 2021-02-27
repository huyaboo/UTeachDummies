import discord
from discord.ext import commands

#EXAMPLE FORMAT OF THE FILE TO PLACE YOUR COMMANDS
class Classname(commands.Cog):
	def __init__(self, client):
		self.client = client

	#PUT THIS FOR EVENTS
	@commands.Cog.listener()

	#PUT THIS ABOVE ANY COMMAND Y'ALL WANNA MAKE
	@commands.command()

#PUT THIS AT THE END OF YOUR PYTHON FILE
def setup(client):
	client.add_cog(Classname(client))