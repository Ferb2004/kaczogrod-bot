import discord
from discord.ext import commands
from discord import app_commands

class Czesc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} jest online.")

    @app_commands.command(name="czesc", description="Pełna kulturka.")
    async def czesc(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} serwus!", ephemeral=True)



async def setup(bot):
    await bot.add_cog(Czesc(bot))