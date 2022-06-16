import discord
from discord.ext import commands
from discord_slash import SlashCommand

import sys
import json

from time import sleep


# Prepare Launching

print('[MESSAGE] Welcome! Please wait until the bot is ready.')
sleep(1)
print('[BOT] Preparing launching...\n')
print('----------------------------------')
print('>> Debug Logs << \n')


# Load Config

print('[DEBUG] Loading Configuration...')

with open('config.json', 'r') as f:
    data = json.load(f)
    token = data["Token"]
    prefix = data["Prefix"]

print('[DEBUG] Loaded Configuration!')


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.remove_command('help')

# Variables

botname = 'PandaBot'
botversion = 'V1.0'

# Slash Commands

slash = SlashCommand(bot, sync_commands=True)

# Ready event

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print('[DEBUG] All functions ready!\n')
    print('>> End of Debug Logs <<')
    print('----------------------------------\n')
    print(f'[INFO] Username: {bot.user.name}')
    print(f'[INFO] Bot ID: {bot.user.id}')
    sleep(1)
    print('[BOT] Bot is now online!')

    channel = bot.get_channel(966300786051133445)
    msg = await channel.send('Online')


# Activity changer

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name='🔧 Under Development!'), status=discord.Status.online)
        sleep(7)
        await bot.change_presence(activity=discord.Game(name=f'mit {len(bot.users)} Usern!'), status=discord.Status.online)
        sleep(7)


# Test Command

@slash.slash(name='Test', description='This is just a test')
async def test(ctx):
    await ctx.send('Test')

# Rickroll Command

@slash.slash(name='Rickroll', description='Rickroll a member on this server')
async def rickroll(ctx, member:discord.Member):
    await ctx.send(f'{member.mention}, you got rickrolled!')
    await ctx.send('https://cdn.discordapp.com/attachments/966300786051133444/986992057539231835/rickroll-roll.gif')

# Shutdown Command

@slash.slash(name='Shutdown', description='Shuttting down the bot [DEV ONLY]')
async def shutdown(ctx):
    await ctx.send('🛑 **Shutting down the bot...**')
    sleep(1)
    sys.exit()



bot.run(token, bot=True)




