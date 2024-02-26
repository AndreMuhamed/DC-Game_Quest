import discord
from discord.ext import commands

intents = discord.Intents.default()  # Включить стандартные интенты
intents.voice_states = True  # Включить интенты для голосовых состояний
intents.guild_messages = True  # Включить привилегированный интент для сообщений сервера
intents.message_content = True  # Намерение для обработки сообщений

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} готов')

@bot.command()
async def чат(ctx):
    message = (
        "Если вам кажется, что в нашем сообществе не хватает определенных каналов для общения или развлечений, не переживайте!\n\n" 
        "**Вы всегда можете** настроить сервер согласно вашим предпочтениям. Просто зайдите в настройки сервера и включите опцию: **показать все каналы**, чтобы получить доступ ко всем имеющимся возможностям и ресурсам."
    )
    embed = discord.Embed(
        description=message,
        color=0xC80147
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1195867893594869857/1211632429891199017/2024-02-26-13-12-07.gif")  #Устанавливаем изображение в интеграцию
    embed.set_footer(text="Наша главная цель - обеспечить ваш комфортный опыт на сервере!")
    embed.set_author(name="ДОБРО ПОЖАЛОВАТЬ В НАШИ ЧАТЫ", icon_url="https://cdn.discordapp.com/attachments/1195867893594869857/1211392935623397376/icon-chat.png")  #Добавляем имя и иконку
    await ctx.send(embed=embed)

bot.run('ТВОЙ ТОКЕН БОТА')
