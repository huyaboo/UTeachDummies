import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

client = Bot.commands(command_prefix = "UTD")
client.remove_command("help")

load_dotenv()
TOKEN = os.getenv("CLIENT_TOKEN")

client.run(TOKEN)