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
async def репер(ctx):
    message = (
        "Здесь вы можете посоветовать похожую игру или поделиться своими любимыми. Если у вас есть информация о том, где можно скачать эту игру через торрент, пожалуйста, поделитесь ею с другими участниками!\n\n" 
        "**Кроме того**, наши игроки всегда готовы помочь вам с решением проблем и непониманий в игре, а также **поделиться** полезными советами и стратегиями. Вместе мы строим удивительные игровые миры и совершенствуем свои навыки."
    )
    embed = discord.Embed(
        description=message,
        color=0xC80147
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1195867893594869857/1212823747371999332/a51e15177a546b6a.png")  #Устанавливаем изображение в интеграцию
    embed.set_footer(text="Вперед к новым игровым приключениям и сражениям!")
    embed.set_author(name="ДОБРО ПОЖАЛОВАТЬ В НАШИ РЕПЕРТУАРЫ", icon_url="https://cdn.discordapp.com/attachments/1195867893594869857/1211392929814544444/icon-torrent.png")  #Добавляем имя и иконку
    await ctx.send(embed=embed)

bot.run('MTEwMjE5OTc0MjE0ODEyMDYyNg.GwBoK3.x7h6joThCacZsA5LCGrUylgGZ7OEE17ihiKbcU')
