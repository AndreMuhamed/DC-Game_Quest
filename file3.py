import discord
from discord.ext import commands
import os
import random
import asyncio

intents = discord.Intents.default()  # Включить стандартные интенты
intents.voice_states = True  # Включить интенты для голосовых состояний
intents.guild_messages = True  # Включить привилегированный интент для сообщений сервера
intents.message_content = True  # Намерение для обработки сообщений

TOKEN = 'ТОКЕН БОТА'
CHANNEL_ID = 1195867893594869851  # Замените на ID вашего голосового канала
MUSIC_FOLDER_PATH = '/путь_к_файлу/myzis'  # Замените на путь к вашей папке с музикой

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов для воспроизведения музыки')
    channel = bot.get_channel(CHANNEL_ID)

    # Подключение к голосовому каналу
    voice_channel = await channel.connect()

    # Установка статуса активности бота
    activity = discord.Activity(type=discord.ActivityType.watching, name="YouTube: Game Quest")
    await bot.change_presence(activity=activity)

    while True:
        # Выбор случайного файла из папки с музикой
        music_file = random.choice(os.listdir(MUSIC_FOLDER_PATH))

        # Формирование полного пути к выбранному файлу
        music_file_path = os.path.join(MUSIC_FOLDER_PATH, music_file)

        # Проигрывание музыки с кодеком Opus
        voice_channel.play(discord.FFmpegOpusAudio(music_file_path), after=lambda e: print('done', e))

        # Ожидание завершения воспроизведения перед переходом к следующему файлу
        while voice_channel.is_playing():
            await asyncio.sleep(1)
   




# Удаляем сообщение c !          
@bot.event
async def on_message(message):
    # Обрабатываем сообщения как команды
    await bot.process_commands(message)

    # После обработки проверяем, начинается ли сообщение с префикса "!"
    if message.content.startswith('!') and not message.author.bot:
        await message.delete()  # Удаляем сообщение с префиксом "!"

        
# Секретные команды                      
@bot.command(name='иван')
async def иван(ctx):
    embed = discord.Embed(
        title="Иван - настоящий герой!",
        description="В игре Иван всегда готов к вызовам и битвам. Но даже сильному воину нужно поддерживать силу, чтобы продолжать свое подвигание!",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)

@bot.command(name='gamequest_news')
async def gamequest_news(ctx):
    embed = discord.Embed(
        title="Краткая история создания проекта",
        description="Всё началось с идеи двух пылких геймеров, которые мечтали о создании пространства, где любители игр могли бы обмениваться идеями, делиться впечатлениями и получать последние новости из игрового мира. Они начали с небольшого форума, где быстро нашли своих поклонников.\n\n"
                    "С помощью распространения информации через форумы и собственный канал на YouTube, их проект набрал обороты. За год работы стала явно ощутима потребность в создании более организованного и развитого коммунального пространства для геймеров.\n\n"
                    "Это побудило их создать собственный сервер Discord, где геймеры могли обсуждать игры, делиться опытом и устраивать игровые вечера вместе. Поддержка активного сообщества и предоставление полезной информации были основными приоритетами команды.\n\n"
                    "Со временем команда Game Quest решила увеличить свое влияние, расширив свое присутствие на различных платформах, таких как Telegram и YouTube, где продолжает предоставлять полезную информацию и развивать свое сообщество.\n\n"
                    "Их упорный труд и страсть к играм сделали Game Quest любимым местом для всех, кто хочет погрузиться в мир известных и неизвестных игр. Их путь достижений продолжается, поскольку они постоянно расширяются и привлекают новых энтузиастов в свое сообщество.",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)
  
@bot.command(name='украина')
async def украина(ctx):
    embed = discord.Embed(
        title="Главный создатель проекта",
        description="Стал украинец, который сыграл ключевую роль в создании и развитии команды Game Quest. Его упорный труд и преданность игровому сообществу способствовали созданию этого пространства для обмена опытом, идеями и впечатлениями от игр. Его вклад стал важным элементом успеха и популярности проекта среди геймеров.",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)
    
@bot.command(name='tedro')
async def tedro(ctx):
    embed = discord.Embed(
        title="TeDro - модератор Game Quest",
        description="После того, как TeDro потерял 100 долларов в игре, он стал модератором на сервере Game Quest. Это неожиданное изменение открыло перед ним новые возможности и вызовы, помогая развиться как игроку и лидеру сообщества.",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)   
            
@bot.command(name='джокер')
async def джокер(ctx):
    embed = discord.Embed(
        title="Джокер - иконический диктор",
        description="Джокер Name1, первый диктор нашего проекта, стал настоящей иконой голоса, что отметило его уникальность и привлекло внимание зрителей. Его энергия и эмоциональность стали душой команды и укрепили их уверенность в успехе проекта.",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)            
            
@bot.command(name='hezuko')
async def hezuko(ctx):
    embed = discord.Embed(
        title="Hezuko - верный друг и опора",
        description="Nezuko - это не только красивая девушка, но и большая опора и верный друг. Ее вера в успех проекта всегда вдохновляла нас и помогала преодолевать любые трудности.",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)
     
@bot.command(name='эдвард')
async def эдвард(ctx):
    embed = discord.Embed(
        title="Сердечная благодарность Эдварду",
        description="Сердечная благодарность Эдварду за его неизменную поддержку и значительный вклад в разработку дискорд-бота. Его экспертиза и навыки были неоценимы в этом процессе, и мы бесконечно признательны за его преданность и профессионализм. Пусть он получит заслуженное уважение за свой вклад в наш проект!",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)
    
@bot.command(name='команда')
async def команда(ctx):
    embed = discord.Embed(
        title="Искренние слова благодарности всем участникам нашей команды",
        description="Хочу выразить искренние слова благодарности всем участникам нашей команды - прошлым и настоящим. Ваш труд, преданность и творческий подход являются истинным источником нашего успеха. Каждый из вас вносит незаменимый вклад в наш проект, делая его лучше и сильнее шаг за шагом. Пусть наша общая мечта продолжает сбываться, а неутомимый труд каждого из вас приносит нам еще больше достижений и побед. Спасибо вам за вашу преданность, энергию и талант - вместе мы непобедимы!",
        color=0xC80147  # Красный цвет
    )
    await ctx.send(embed=embed)
    
@bot.command(name='сахарок')
async def сахарок(ctx):
    embed = discord.Embed(
        title="Сладкий сахарок",
        description="Она настолько сладкая, что ты ее захочешь попробовать даже в игре, потому что сахар - это энергия!",
        color=0xC80147  # Цвет интеграции
    )
    await ctx.send(embed=embed)    
    
    
        
        
        
        

# Запуск бота
bot.run(TOKEN)