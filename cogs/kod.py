import discord
from discord.ext import commands
from discord import app_commands

class Kod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} jest online.")

    @app_commands.command(name="kod", description="Link do kodu źródłowego.")
    async def czesc(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} kod źródłowy dostępny jest tutaj: https://github.com/Ferb2004/kaczogrod-bot", ephemeral=True)



async def setup(bot):
    await bot.add_cog(Kod(bot))