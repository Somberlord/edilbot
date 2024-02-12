import discord
from perm.format import PermFormat
from perm.model.permanence import Permanence


class PermCreateModal(discord.ui.Modal):
    def __init__(self, *args, permcb, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.permcb = permcb
        modal_format = PermFormat.pcm_modal()

        self.add_item(discord.ui.InputText(label=modal_format['title']))
        self.add_item(discord.ui.InputText(label=modal_format['date']))
        self.add_item(discord.ui.InputText(label=modal_format['start']))
        self.add_item(discord.ui.InputText(label=modal_format['end']))
        self.add_item(discord.ui.InputText(label=modal_format['description'],
                                           style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        perm = Permanence(title=self.children[0].value, datestr=self.children[1].value,
                          startstr=self.children[2].value, endstr=self.children[3].value,
                          description=self.children[4].value)
        await self.permcb(interaction=interaction, perm=perm)
