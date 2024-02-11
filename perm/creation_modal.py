import discord
from config.i18n import I18nPermanenceStandard as I18n
from perm.format import PermFormat
from perm.model.event import Event


class PermCreateModal(discord.ui.Modal):
    def __init__(self, *args, permcb, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.permcb = permcb

        self.add_item(discord.ui.InputText(label=I18n.PCM_PERM_TITLE))
        self.add_item(discord.ui.InputText(label=I18n.PCM_PERM_DATE))
        self.add_item(discord.ui.InputText(label=I18n.PCM_PERM_START_TIME))
        self.add_item(discord.ui.InputText(label=I18n.PCM_PERM_END_TIME))
        self.add_item(discord.ui.InputText(label=I18n.PCM_PERM_DESC, style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        event = Event(title=self.children[0].value, datestr=self.children[1].value,
                      startstr=self.children[2].value, endstr=self.children[3].value,
                      description=self.children[4].value)
        embed = PermFormat.get_pt_embed(event=event, user=interaction.user)
        await self.permcb(interaction=interaction, embed=embed, event=event)
