import discord
from discord.ext import commands
from perm.perm_creation_modal import PermCreateModal
from config.i18n import I18nPermanenceStandard as I18n
from config.botconfig import Config


class Permanence(commands.Cog):

    def __init__(self, bot: discord.Bot, config: Config):
        self.bot: discord.Bot = bot
        self.config: Config = config

    @commands.slash_command(description=I18n.PCM_SLASHCMD_DESC)
    async def perm(self, ctx):
        modal = PermCreateModal(title=I18n.PCM_MODAL_TITLE, permcb=self.modal_callback)
        await ctx.send_modal(modal)

    async def modal_callback(self, interaction: discord.Interaction, embed, title, desc):
        permchannel: discord.ForumChannel = self.bot.get_channel(self.config.perm_channel)
        newthread = await permchannel.create_thread(name=title, embed=embed, content=desc)
        await interaction.response.send_message(f"Thread <#{newthread.id}> créé", ephemeral=True, delete_after=30)
