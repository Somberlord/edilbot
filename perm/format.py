import discord
from config.i18n import I18nPermanenceStandard as I18n
from perm.model.permanence import Permanence


class PermFormat:

    @staticmethod
    def get_pt_title(permdate, permtitle) -> str:
        return f"[{permdate}] {permtitle}"

    @staticmethod
    def get_pt_embed(perm: Permanence, user: discord.User) -> discord.Embed:
        embed = discord.Embed(
            title=PermFormat.get_pt_title(perm.datestr, perm.title),
            description=f"{I18n.PCT_THREAD_DESC} <@{user.id}>",
            color=I18n.PCT_EMBED_COLOR,
        )

        embed.add_field(name=I18n.PCM_PERM_DATE, value=perm.startstr, inline=True)
        embed.add_field(name=I18n.PCT_PERM_START, value=perm.startstr, inline=True)
        embed.add_field(name=I18n.PCT_PERM_END, value=perm.endstr, inline=True)
        embed.add_field(name=I18n.PCM_PERM_DESC, value=perm.description)
        embed.set_footer(text="React down there")
        embed.set_author(name=f"{user.name}")
        return embed
