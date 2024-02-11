import discord
from discord.ext import commands

from perm.creation_modal import PermCreateModal
from config.i18n import I18nPermanenceStandard as I18n
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
    @commands.slash_command(description=I18n.PCM_SLASHCMD_DESC)
    async def perm(self, ctx):
        modal = PermCreateModal(title=I18n.PCM_MODAL_TITLE, permcb=self.modal_callback)
        await ctx.send_modal(modal)

    # Called when the user finished filling the modal
    # Create a thread in a ForumChannel
    # Replies to the user with the thread id
    async def modal_callback(self, interaction: discord.Interaction, embed: discord.Embed, perm: Permanence):
        # Raises IDE warning, because ForumChannel is a subclass of GuildChannel
        permchannel: discord.ForumChannel = self.bot.get_channel(self.channel)
        title_formatted = PermFormat.get_pt_title(perm.datestr, perm.title)
        newthread = await permchannel.create_thread(name=title_formatted, embed=embed, content=perm.description)
        await interaction.response.send_message(f"{I18n.PMR_THREAD_CREATED} : <#{newthread.id}>",
                                                ephemeral=True, delete_after=self.response_delay)
        for listener in self.event_listeners:
            await listener.create_permanence(perm)
