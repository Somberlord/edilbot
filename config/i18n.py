import discord
from dataclasses import dataclass


@dataclass
class I18nPermanenceStandard:
    PCM_SLASHCMD_DESC: str = "Création de permanence"
    PCM_MODAL_TITLE: str = "Création de permanence"
    PCM_PERM_TITLE: str = "Intitulé"
    PCM_PERM_DATE: str = "Date"
    PCM_PERM_START_TIME: str = "Heure de début"
    PCM_PERM_END_TIME: str = "Heure de fin"
    PCM_PERM_DESC: str = "Description"
    PCT_THREAD_DESC: str = "Permanence créé par"
    PCT_PERM_START: str = "Début"
    PCT_PERM_END: str = "Fin"
    PCT_EMBED_COLOR = discord.Colour.blurple()
