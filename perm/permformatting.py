import discord
from config.i18n import I18nPermanenceStandard as I18n


class PermFormat:

    @staticmethod
    def get_pt_title(permdate, permtitle) -> str:
        return f"[{permdate}] {permtitle}"

    @staticmethod
    def get_pt_embed(permdate, permtitle, permuser, permstart, permend, permdesc) -> discord.Embed:
        embed = discord.Embed(
            title=PermFormat.get_pt_title(permdate, permtitle),
            description=f"{I18n.PCT_THREAD_DESC} <@{permuser.id}>",
            color=I18n.PCT_EMBED_COLOR,
        )

        embed.add_field(name=I18n.PCM_PERM_DATE, value=permdate, inline=True)
        embed.add_field(name=I18n.PCT_PERM_START, value=permstart, inline=True)
        embed.add_field(name=I18n.PCT_PERM_END, value=permend, inline=True)
        embed.add_field(name=I18n.PCM_PERM_DESC, value=permdesc)
        embed.set_footer(text="React down there")
        embed.set_author(name=f"{permuser.name}")
        return embed
