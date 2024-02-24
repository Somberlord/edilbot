import discord
from perm.format import PermFormat
from perm.model.permanence import *


class PermCreateModal(discord.ui.Modal):
    def __init__(self, *args, permcb, context, perm=Permanence(), validation=VALID_TIMES, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.permcb = permcb
        self.context = context
        modal_format = PermFormat.pcm_modal()

        date_label = (modal_format['date'] +
                      (f" {PermFormat.pcm_get_input_error()}" if validation == INVALID_DATE else ""))
        start_label = (modal_format['start']
                       + (f" {PermFormat.pcm_get_input_error()}" if validation == INVALID_START_TIME else ""))
        end_label = (modal_format['end']
                     + (f" {PermFormat.pcm_get_input_error()}" if validation == INVALID_END_TIME else ""))

        self.add_item(discord.ui.InputText(label=modal_format['title'], value=perm.title))
        self.add_item(discord.ui.InputText(label=date_label, value=perm.datestr))
        self.add_item(discord.ui.InputText(label=start_label, value=perm.startstr))
        self.add_item(discord.ui.InputText(label=end_label, value=perm.endstr))
        self.add_item(discord.ui.InputText(label=modal_format['description'],
                                           style=discord.InputTextStyle.long, value=perm.description))

    async def create(self):
        await self.context.send_modal(self)

    async def callback(self, interaction: discord.Interaction):
        perm = Permanence(title=self.children[0].value, datestr=self.children[1].value,
                          startstr=self.children[2].value, endstr=self.children[3].value,
                          description=self.children[4].value)
        await self.permcb(interaction=interaction, perm=perm)
