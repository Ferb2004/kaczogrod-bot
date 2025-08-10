from sys import exception

import discord
from discord.ext import commands
from discord import app_commands
import os

from typing import Literal


class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.coglist = bot.coglist

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} działa.")


    @app_commands.command(name="reload", description="Odświeża coga.")
    @app_commands.checks.has_permissions(administrator=True)
    async def reload(self, interaction: discord.Interaction, cog: Literal["czesc","ping","moneta","github","nadawanieroli","statystyki","tickety","test"]):
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            await interaction.response.send_message(f"Przeładowano {cog}.py", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Błąd, nie można przeładować {cog}.py\n'''{e}'''", ephemeral=True)
        except commands.ExtensionNotFound:
            await interaction.response.send_message(f"Nie znaleziono coga {cog}.py", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Reload(bot))