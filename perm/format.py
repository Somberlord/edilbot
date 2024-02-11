import discord
from config.i18n import I18nPermanenceStandard as I18n
from perm.model.event import Event


class PermFormat:

    @staticmethod
    def get_pt_title(permdate, permtitle) -> str:
        return f"[{permdate}] {permtitle}"

    @staticmethod
    def get_pt_embed(event: Event, user: discord.User) -> discord.Embed:
        embed = discord.Embed(
            title=PermFormat.get_pt_title(event.datestr, event.title),
            description=f"{I18n.PCT_THREAD_DESC} <@{user.id}>",
            color=I18n.PCT_EMBED_COLOR,
        )

        embed.add_field(name=I18n.PCM_PERM_DATE, value=event.startstr, inline=True)
        embed.add_field(name=I18n.PCT_PERM_START, value=event.startstr, inline=True)
        embed.add_field(name=I18n.PCT_PERM_END, value=event.endstr, inline=True)
        embed.add_field(name=I18n.PCM_PERM_DESC, value=event.description)
        embed.set_footer(text="React down there")
        embed.set_author(name=f"{user.name}")
        return embed
