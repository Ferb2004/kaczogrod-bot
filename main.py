import discord
from discord.ext import commands
from dotenv import load_dotenv

import os
import asyncio

#Ładuje plik z kluczami i je definiuje
load_dotenv(".env")
TOKEN: str = os.getenv("TOKEN")


#Definiowanie bota, prefixu komend i uprawnień
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())


#Powiadomienie o gotowości bota i statusie komend
@bot.event
async def on_ready():
    print("Bot gotowy!")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Liczba zsynchronizowanych komend: {len(synced_commands)}")
    except Exception as e:
        print("Problem z synchoronizacją komend:", e)


#Funkcja ładująca pliki z komendami
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


#Funkcja załączająca funkcję ładującą pliki z komendami i włączająca bota
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)


#Załącza główną funkcje
asyncio.run(main())