import discord
from config.i18n import I18nPermanenceStandard as I18n
from perm.format import PermFormat


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
        permtitle = self.children[0].value
        permdate = self.children[1].value
        permstart = self.children[2].value
        permend = self.children[3].value
        permdesc = self.children[4].value
        embed = PermFormat.get_pt_embed(permdate=permdate, permtitle=permtitle, permuser=interaction.user,
                                        permstart=permstart, permend=permend, permdesc=permdesc)
        await self.permcb(interaction=interaction, embed=embed, title=PermFormat.get_pt_title(permdate, permtitle),
                          desc=permdesc)
