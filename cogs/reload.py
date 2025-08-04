import discord
from discord.ext import commands
from discord import app_commands

from typing import Literal


class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.coglist = ["github", "ping", "reload", "czesc"]

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} jest online.")


    @app_commands.command(name="reload", description="Odświeża coga.")
    async def reload(self, interaction: discord.Interaction, cog: Literal["github", "ping", "reload", "czesc"]):
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            await interaction.response.send_message(f"Przeładowano {cog}.py", ephemeral=True)
        except commands.ExtensionNotFound:
            await interaction.response.send_message(f"Nie znaleziono coga {cog}.py", ephemeral=True)
        except commands.ExtensionNotLoaded:
            await interaction.response.send_message(f"Cog {cog}.py nie jest załadowany", ephemeral=True)
        except commands.NoEntryPointError:
            await interaction.response.send_message(f"Cog {cog}.py nie ma funkcji setup()", ephemeral=True)
        except commands.ExtensionFailed:
            await interaction.response.send_message(f"Wystąpił błąd podczas przeładowywania {cog}.py", ephemeral=True)



async def setup(bot):
    await bot.add_cog(Reload(bot))