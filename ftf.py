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
async def гейм(ctx):
    message = (
        "В нашей командной игре каждый игрок - незаменимое звено. Помогите участнику собрать необходимую компоновку, чтобы вместе достигать победы!\n\n" 
        "**После отправки** сообщения автором будет создана специальная ветка, где каждый участник сможет выразить свои идеи и предложения для улучшения техники. **Давайте** объединим усилия и создадим мощную команду, способную одерживать победы на любом поле битвы."
    )
    embed = discord.Embed(
        description=message,
        color=0xC80147
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1195867893594869857/1212817198452572180/e30edec7d5e1b0e1.png")  #Устанавливаем изображение в интеграцию
    embed.set_footer(text="Единая команда, совершенная техника и удачный бой!")
    embed.set_author(name="ДОБРО ПОЖАЛОВАТЬ В НАШИ ГЕЙМТЕКИ", icon_url="https://cdn.discordapp.com/attachments/1195867893594869857/1211392927637704764/icon-technician.png")  #Добавляем имя и иконку
    await ctx.send(embed=embed)

bot.run('ТВОЙ ТОКЕН БОТА')
