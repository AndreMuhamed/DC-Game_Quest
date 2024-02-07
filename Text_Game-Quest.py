import discord
from discord.ext import commands

TOKEN = 'ТВОЙ ТОКЕН БОТА'  # замените на ваш токен

intents = discord.Intents.default()
intents.message_content = True  # Намерение для обработки сообщений

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def хехе(ctx):
    role1_id = 1195867892550479983
    role2_id = 1195867892521123859  # Замените на ID второй роли
    role1 = ctx.guild.get_role(role1_id)
    role2 = ctx.guild.get_role(role2_id)
    if role1 and role2:
        message = f"<@&{role1_id}> и <@&{role2_id}> а здесь вы должны продвигать наш сервер в поисковой строке командами: `/up ; /like`"
        await ctx.send(message)
    else:
        await ctx.send("Одна из ролей не найдена!")


bot.run(TOKEN)
