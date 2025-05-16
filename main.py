import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

prefix_data = {"prefix": "z."}  # string prefix

def get_prefix(bot, message):
    return prefix_data["prefix"]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Reply when the bot is pinged
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        await message.channel.send(f"My current command prefix is `{prefix_data['prefix']}`")

    await bot.process_commands(message)

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
print(f"Running bot with token: {token}")
bot.run(token)
