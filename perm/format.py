import discord
from perm.model.permanence import Permanence


class PermFormat:

    @staticmethod
    def pcm_slashcmd_desc() -> str:  # Permanence Command - Slash Command - Description
        return "Création de permanence"

    @staticmethod
    def pcm_modal_title() -> str:  # Permanence Modal - Title
        return "Création de permanence"

    @staticmethod
    def pcm_modal() -> dict:  # Permanence Modal - Data
        return {
            'title': PermFormat.pcm_modal_title(),
            'date': "Date",
            'start': "Heure de début",
            'end': "Heure de fin",
            'description': "Description",
        }

    @staticmethod
    def pcm_thread(perm: Permanence, user: discord.User) -> dict:  # Permanence Modal - Created Thread
        title = f"[{perm.datestr}] {perm.title}"
        return {
            'title': title,
            'embed': PermFormat.pcm_thread_embed(perm, user, title)
        }

    @staticmethod
    # Permanence Modal - Thread Embed
    def pcm_thread_embed(perm: Permanence, user: discord.User, title) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=f"Permanence créée par <@{user.id}>",
            color=discord.Colour.blurple(),
        )
        embed.add_field(name="Date", value=perm.datestr, inline=True)
        embed.add_field(name="Début", value=perm.startstr, inline=True)
        embed.add_field(name="Fin", value=perm.endstr, inline=True)
        embed.add_field(name="Description", value=perm.description)
        embed.set_footer(text="React down there")
        embed.set_author(name=f"{user.name}")
        return embed

    @staticmethod
    def pcm_response(threadid: int) -> str:  # Permanence Modal - Command Response
        return f"Thread créé : <#{threadid}>"
