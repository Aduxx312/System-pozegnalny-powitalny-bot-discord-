import discord
from discord.ext import commands
from welcome import send_welcome_message
from goodbye import send_goodbye_message

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1344736081689444562 #Zmien na swoj kanal id (kanal na ktorym maja byc wysylane wiadomosci powitalne)
GOODBYE_CHANNEL_ID = 1344736081689444562 #Zmien na swoj kanal id (kanal na ktorym maja byc wysylane wiadomosci pozegnalne)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await send_welcome_message(channel, member)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(GOODBYE_CHANNEL_ID)
    if channel:
        await send_goodbye_message(channel, member)

bot.run("Wklej tutaj token swojego bota")
