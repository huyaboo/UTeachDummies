import discord
from discord.ext import commands
from discord.ext.commands import guild_only
from asyncio import TimeoutError
from typing import Optional


class Roles(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.group()
	@guild_only()
	async def roles(self, ctx: commands.Context):
		if ctx.invoked_subcommand is None:
			# TODO roles help message
			await ctx.send('this should be a help message')

	@roles.command()
	async def setup(self, ctx: commands.Context, *, category_name: Optional[str]):
		def same_author_and_channel(message):
			return message.author == ctx.author and message.channel == ctx.channel

		if category_name is None:
			await ctx.send('What should the channel group be called?')
			try:
				msg = await ctx.bot.wait_for('message', check=same_author_and_channel, timeout=60.0)

				category_name = msg.content
			except TimeoutError:
				await ctx.send('One minute has passed without a reply, cancelling setup.')
				return

		names = []

		await ctx.send('Send the name of each role you want (type "done" to confirm, or "cancel" to cancel):')
		while True:
			try:
				msg = await ctx.bot.wait_for('message', check=same_author_and_channel, timeout=60.0)

				if msg.content == "cancel":
					return
				elif msg.content == "done":
					break

				names.append(msg.content)
				await msg.add_reaction('\u2705')  # green checkbox
			except TimeoutError:
				await ctx.send('One minute has passed without a reply, cancelling setup.')
				return

		await ctx.send('Do you want to allow anyone to @ these roles? (y/n)')
		try:
			msg = await ctx.bot.wait_for('message', check=same_author_and_channel, timeout=60.0)

			if msg.content == 'n':
				mentionable = False
			else:
				mentionable = True
		except TimeoutError:
			await ctx.send('One minute has passed without a reply, cancelling setup.')
			return

		reason = f'Role setup by {ctx.author.id}'

		category = await ctx.guild.create_category(
			name=category_name,
			reason=reason,
		)

		for name in names:
			role = await ctx.guild.create_role(
				name=name,
				mentionable=mentionable,
				reason=reason,
			)

			await ctx.guild.create_text_channel(
				name=name,
				category=category,
				overwrites={
					ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
					role: discord.PermissionOverwrite(read_messages=True),
				},
				reason=reason,
			)

		await ctx.send('Setup complete!')


def setup(client):
	client.add_cog(Roles(client))
