import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='/')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("bot is now ready")

if __name__ == "__main__":
    with open("token.txt", "r") as f:
        token = f.read()
    bot.run(token)