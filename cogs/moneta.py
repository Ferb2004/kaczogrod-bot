import discord
from discord.ext import commands
from discord import app_commands

import random

class Moneta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} jest online.")


    @app_commands.command(name="moneta", description="Rzut monetą.")
    async def moneta(self, interaction: discord.Interaction):
        opcje = ['Orzeł', 'Reszka']
        rzut = random.choice(opcje)
        await interaction.response.send_message(f"{rzut}")



async def setup(bot):
    await bot.add_cog(Moneta(bot))