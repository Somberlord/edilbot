import discord
from discord.ext import commands

from perm.creation_modal import PermCreateModal
from perm.event_listener import EventListener
from perm.model.permanence import Permanence
from perm.format import PermFormat


class PermanenceCog(commands.Cog):

    def __init__(self, bot, config: dict):
        self.bot: discord.Bot = bot
        # Load Permanence Configuration
        self.channel = int(config['ForumChannel'])
        self.response_delay = int(config['ModalResponseDelay'])
        self.event_listeners = []

    def add_event_listener(self, event_listener: EventListener):
        self.event_listeners.append(event_listener)

    # Entry point. Command /perm
    # Creates a modal for the user to fill
    @commands.slash_command(description=PermFormat.pcm_slashcmd_desc())
    async def perm(self, ctx):
        modal = PermCreateModal(title=PermFormat.pcm_modal_title(), permcb=self.modal_callback)
        await ctx.send_modal(modal)

    # Called when the user finished filling the modal
    # Create a thread in a ForumChannel
    # Replies to the user with the thread id
    async def modal_callback(self, interaction: discord.Interaction, perm: Permanence):
        # Raises IDE warning, because ForumChannel is a subclass of GuildChannel
        permchannel: discord.ForumChannel = self.bot.get_channel(self.channel)
        thread_format = PermFormat.pcm_thread(perm, interaction.user)
        newthread = await permchannel.create_thread(name=thread_format['title'],
                                                    embed=thread_format['embed'],
                                                    content=perm.description)
        await interaction.response.send_message(PermFormat.pcm_response(newthread.id),
                                                ephemeral=True, delete_after=self.response_delay)
        for listener in self.event_listeners:
            await listener.create_permanence(perm)
