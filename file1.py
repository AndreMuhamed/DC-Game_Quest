import disnake
from disnake.ext import commands, tasks
from disnake import PermissionOverwrite, Member, Guild, Activity, ActivityType
from datetime import datetime, timedelta
import typing
import time
import discord
import asyncio
import random
import requests
import openai
import os


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.presences = True
intents.voice_states = True 
intents.guilds = True 

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"Бот запуснился как {bot.user} и готов выполнять команды")


@bot.event
async def on_member_join(member):
    # Ваш ID роли, которую нужно выдать при входе
    role_id = 1195867892521123853  # Замените это на ID вашей роли
    role = member.guild.get_role(role_id)

    if role is not None:
        await member.add_roles(role)

    welcome_channel_id = 1195867893745860762  # Замените это на ID канала, куда хотите отправлять приветственные сообщения
    welcome_channel = bot.get_channel(welcome_channel_id)

    if welcome_channel is not None:
        gif_url = "https://i.gifer.com/3OgpU.gif"  # Замените это на вашу ссылку на гифку
        gif_response = requests.get(gif_url)

        with open("welcome.gif", "wb") as f:
            f.write(gif_response.content)

        with open("welcome.gif", "rb") as f:
            gif_file = disnake.File(f, filename="welcome.gif")
            await welcome_channel.send(
                f"Здравия желаю {member.mention}! Обязательно ознакомьтесь с правилами сервера, чтобы не пропустить важную информацию. Исследуйте разделы навигации для поиска дополнительного увлекательного контента. Также, не упустите возможность познакомиться с другими участниками — за каждым никнеймом таится своя уникальная история и интересы!",
                file=gif_file)

        os.remove("welcome.gif")  # Удаляем временный файл после отправки

    

message_threshold_1 = 60  # Измените на нужное вам значение
message_counter_1 = 0
message_threshold_2 = 40  # Измените на нужное вам значение
message_counter_2 = 0

users = {}

@bot.event
async def on_message(message):
    if message.channel.id == 1195879709553209384:  # Замените YOUR_CHANNEL_ID на ID вашего канала
        emoji_ids = [11111111111111, 1111111111111, 11111111111111, 11111111111111, 1111111111111111]  # Замените на ID ваших эмодзи
        for emoji_id in emoji_ids:
            emoji = bot.get_emoji(emoji_id)
            if emoji:
                await message.add_reaction(emoji)
            else:
                print(f"Emoji with ID {emoji_id} not found!")

    global message_counter_1, message_counter_2

    # Проверяем, что сообщение не от бота и не в личных сообщениях
    if not message.author.bot and isinstance(message.channel, disnake.TextChannel):
        message_counter_1 += 1
        message_counter_2 += 1

        if message_counter_1 == message_threshold_1:
            channel = message.channel
            await channel.send(
                '''**Не забудьте подписать на другие наши социальные сети нашего Discord-сервера:**
◈ YouTube Game Quest: https://www.youtube.com/@GameQuest_news
◈ Telegram-группа: https://t.me/GameQuest_news''')
            message_counter_1 = 0

        if message_counter_2 == message_threshold_2:
            channel = message.channel
            await channel.send('''**Поддержите наш проект донатом:**  
ↈ https://www.patreon.com/andremuhamad
ↈ https://www.donationalerts.com/r/andremuhamad
''')
            message_counter_2 = 0

    # Отвечаем на приветственное сообщение пользователя в определенном канале
    if message.content.lower().startswith(
            ('привет', 'хай', 'салют', 'привіт', 'всем ку', 'всем привет', 'здарова',
             'приветствую', 'добрый день', 'здравствуйте', 'Hello', 'хаю хай', 'Hi',
             'доброе утро', 'добрый вечер', 'бонжур', 'Рад встрече')):
        response = 'Здравия желаю! Мы рады видеть вас здесь и надеемся, что ваше время пребывания будет приятным и наполненным позитивом. Если у вас возникнут вопросы или потребуется помощь, не стесняйтесь обращаться к администраторам или модераторам через бота. Также, пожалуйста, придерживайтесь правил сервера.'

        channel_id = 1195867893745860762  # Замените YOUR_CHANNEL_ID на фактический ID вашего канала
        if isinstance(message.channel, disnake.DMChannel):
            await message.author.send(response)
        elif message.channel.id == channel_id:
            await message.channel.send(response)

    # Отвечаем на сообщения пользователя в личных сообщениях
    if message.author != bot.user and isinstance(message.channel, disnake.DMChannel):
        response = "**Благодарю за ваше сообщение! В настоящее время бот занят и не может вести разговор, так как активно работает на сервере:** https://discord.gg/nQGvVAEw5r"
        await message.author.send(response)

    await bot.process_commands(message)
  

@bot.slash_command(description="Отправить информацию о нарушении на сервере")
async def отчёт(ctx: disnake.ApplicationCommandInteraction,
                пользователь: disnake.Member,
                причина: str,
                доказательство: str = None):
    """Отправляет интеграцию в фиксированный канал жалоб"""
    канал = bot.get_channel(1200967683110338560)
    цвет = "#C80147"

    пользователь_заявник = ctx.author

    отчет_msg = f"**{'### НАРУШЕНИЯ НА СЕРВЕРЕ'.upper()}**На пользователя {пользователь.mention} была подана жалоба от {пользователь_заявник.mention}\n\n**Причина нарушения:**\n```{причина}```"

    if доказательство:
        отчет_msg += f"\n**Доказательство нарушения:**\n```{доказательство}```"

    embed = disnake.Embed(description=отчет_msg, color=int(цвет[1:], 16))

    if канал:
        message = await канал.send(embed=embed)
        emojis = ['🟢', '🔴']
        for emoji in emojis:
            await message.add_reaction(emoji)

    await пользователь_заявник.send(
        "Ваша жалоба была успешно отправлена: **Команде Game Quest**")


@bot.slash_command(description="Отправить запрос на присоединение к команде")
async def присоединиться(ctx: disnake.ApplicationCommandInteraction, кем: str, возраст: int):
    """Отправляет запрос на присоединение к команде"""
    канал = bot.get_channel(1200965072093184051)
    цвет = "#C80147"

    сообщение = f"### ЗАПРОС НА ПРИСОЕДИНЕНИЕ\n\nПользователь {ctx.author.mention} хочет присоединиться к команде\n\n**Роль:**\n```{кем}```\n**Возраст:**\n```{возраст} лет```"

    embed = disnake.Embed(description=сообщение, color=int(цвет[1:], 16))

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await ctx.author.send("Ваш запрос на присоединение успешно отправлен: **Команде Game Quest**")


@bot.slash_command(description="Задать вопрос о сервере")
async def помощ(ctx, вопрос: str, ссылка_на_ваш_скриншот: str = None):
    канал = bot.get_channel(1200962301143044096)
    пользователь = ctx.author

    вопрос_msg = f"### ВОПРОСЫ О СЕРВЕРЕ\n\nИнтересный вопрос о сообществе от: {пользователь.mention}\n\n**Вопрос:**\n```{вопрос}```"

    цвет = "#C80147"

    embed = disnake.Embed(description=вопрос_msg, color=int(цвет[1:], 16))

    if ссылка_на_ваш_скриншот:
        embed.add_field(name="\n\n**Дополнительная информация:**", value=f"```{ссылка_на_ваш_скриншот}```", inline=False)

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await пользователь.send(
            "Ваш вопрос был успешно отправлен: **Команде Game Quest**")


@bot.slash_command(description="Отправить идею для сервера или бота")
async def идея(ctx: disnake.ApplicationCommandInteraction, категория: str, описание_идеи: str, ссылка_на_ваш_скриншот: str = None):
    канал = bot.get_channel(1200960162706505930)  # Замените на ID вашего канала для идей

    пользователь = ctx.author

    идея_msg = f"### ИДЕИ ДЛЯ СЕРВЕРА\n\nПользователь {пользователь.mention} предложил модель для развития\n\n**Категория:** \n```{категория}```\n**Описание идеи:**\n```{описание_идеи}```"

    цвет = "#C80147"

    embed = disnake.Embed(description=идея_msg, color=int(цвет[1:], 16))

    if ссылка_на_ваш_скриншот:
        embed.add_field(name="\n\n**Дополнительная информация:**", value=f"```{ссылка_на_ваш_скриншот}```", inline=False)

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await пользователь.send(
            "Ваша идея была успешно отправлена: **Команде Game Quest**")


@bot.slash_command(description="Не нажимай братан, а то...")
async def пупупу(interaction: disnake.AppCmdInter):
  await interaction.send('''**Здесь могла бы быть ваша реклама.**

Заказать рекламу: https://t.me/admirall_times''')


anecdotes = [
    "Почему герой из RPG всегда говорит в повелительном наклонении? Потому что ему нельзя отказаться от квестов!",
    "Почему персонажи из платформеров всегда такие нервные? Потому что они сталкиваются с препятствиями на каждом шагу!",
    "Я думал создать свою игру про котиков, но решил, что мне будет тяжело договориться о молчании этих персонажей.",
    "Почему программисты часто играют в хорроры? Потому что им тяжело спать с открытыми багами!",
    "Как геймеры проводят лето? Сидя дома и охлаждая компьютер!"
    "Почему геймеры зимой всегда на улице? Потому что хотят использовать инвентарь без снега!",
    "Если геймер лишний раз спрашивает тебя: 'А у тебя есть время поиграть?', это значит, что его вместо обеда ждет босс!"
    "Почему герои из RPG всегда находят антисептики?",
    "Если звезда имеет 5 углов, это значит, что геймер играет в ужасную игру!",
    "Почему геймеры не боятся зомби? Потому что они привыкли к ним уже на работе!",
    "Почему геймерам всегда не хватает времени? Потому что они занимаются 'ресурсоемкой деятельностью'!",
    "Если ты играл всю ночь, ты не устал — ты просто в режиме 'батарея разряжена'!",
    "Почему геймеры хорошо разбираются в технике? Потому что они все время подключаются к разным мирам!",
    "Я знаю только одну строку из военной стратегии: 'Я говорю тебе, у нас есть план!'",
    "Я обычно не играю в игры — у меня уже нет места на жестком диске!",
    "Как называют мастера стрельбы с большого расстояния? Снайпера-геймера!",
    "Почему геймеры всегда знают, как пройти сложные уровни? Потому что они учились делать даже домашние задания в последний момент!",
    "Что геймеры говорят своим героям перед боем? 'Верь в себя, ведь если ты погибнешь, мы начнем все сначала!'",
    "Почему геймеры никогда не боятся боли? Потому что для них это всего лишь дополнительный звуковой эффект!",
    "Если выиграв уровень, геймер сразу же идет на форум и задает вопрос: 'Что дальше?'",
    "Почему геймеры думают о еде даже во время игры? Потому что еда — это бонус к мане!",
    "Почему геймеры не любят поражения в играх? Потому что тогда они чувствуют себя как... геймеры в реальной жизни!",
    "Что делать, если игра долго не грузится? Заняться... группой геймеров и отпраздновать загрузку игры!",
    "Если игра зависает на экране загрузки, это не баг — это... максимально веселая стартовая локация!",
    "Если геймер говорит, что 'ведет жизнь', это означает, что он действительно тяжело ведет свою кофе!",
    "Почему геймеры всегда хотят есть? Потому что еда — это дополнительный источник энергии и возможности для персонажа!",
    "Что делать, если геймер не может решить, что поесть? Загрузить быстрым доступом пиццу!",
    "Если геймер нашел еду в игре, это не удивительно — ведь он все время ищет баффы и бонусы!",
    "Почему геймеры любят игры на выживание? Потому что это единственная возможность, когда их инвентарь остается всегда полным!",
    "Если геймер долго не спит, это не баг — это его способность настроения 'не засыпать до победы'!"
    "Почему герой из RPG всегда говорит в повелительном наклонении? Потому что ему нельзя отказаться от квестов!",
]

@bot.slash_command(description="Отправляет анекдоты игровой тематики")
async def анекдот(ctx: disnake.ApplicationCommandInteraction):
  random_анекдот = random.choice(anecdotes)
  await ctx.response.send_message(random_анекдот)

PLASH_KEY = "ТОКЕН unsplash"  # Замените на свой ключ

@bot.slash_command(description="Отправляет фото реальной машины")
async def кибертрак(context: disnake.ApplicationCommandInteraction):
    try:
        # Отложенный ответ
        await context.response.defer()

        response = requests.get(
            f'https://api.unsplash.com/photos/random?query=car&client_id={PLASH_KEY}'
        )
        response.raise_for_status()  # Проверка наличия ошибок в ответе

        data = response.json()
        image_url = data['urls']['regular']

        # Отправка конечного ответа
        await context.edit_original_message(content=image_url)

    except requests.exceptions.HTTPError as errh:
        await context.edit_original_message(content=f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        await context.edit_original_message(content=f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        await context.edit_original_message(content=f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        await context.edit_original_message(content=f"Something went wrong: {err}")   
    
@bot.slash_command(description="Отправляет крутую фотку")
async def фотка(ctx: disnake.ApplicationCommandInteraction):
    try:
        # Отложенный ответ
        await ctx.response.defer()

        # Запрос к API для получения случайной фотографии кота
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        data = response.json()
        image_url = data[0]['url']

        # Отправьте изображение в текстовый канал
        await ctx.send(content=image_url)
    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        await ctx.send(f"Произошла ошибка: {e}")

    
PLASH_API_KEY = "ТОКЕН unsplash"  # Замените на свой ключ

@bot.slash_command(description="Отправляет фото компьютера")
async def пк(context: disnake.ApplicationCommandInteraction):
    try:
        # Отложенный ответ
        await context.response.defer()

        response = requests.get(
            f'https://api.unsplash.com/photos/random?query=computer&client_id={PLASH_API_KEY}'
        )
        response.raise_for_status()  # Проверка наличия ошибок в ответе

        data = response.json()
        image_url = data['urls']['regular']

        # Отправка конечного ответа
        await context.edit_original_message(content=image_url)

    except requests.exceptions.HTTPError as errh:
        await context.edit_original_message(content=f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        await context.edit_original_message(content=f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        await context.edit_original_message(content=f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        await context.edit_original_message(content=f"Something went wrong: {err}")
        

ASH_API_KEY = "ТОКЕН unsplash"  # Замените на свой ключ доступа Unsplash

@bot.slash_command(description="Отправляет случайное фото")
async def картина(ctx: disnake.ApplicationCommandInteraction):
    try:
        # Откладываем ответ, чтобы Discord знал, что бот обрабатывает команду
        await ctx.response.defer()

        # Делаем запрос к API Unsplash для получения случайного изображения
        headers = {
            "Authorization": f"Client-ID {ASH_API_KEY}"
        }
        response = requests.get('https://api.unsplash.com/photos/random', headers=headers)
        response.raise_for_status()  # Проверяем наличие ошибок в ответе

        data = response.json()
        image_url = data['urls']['regular']

        # Отправляем изображение в текстовый канал
        await ctx.send(content=image_url)
    except requests.exceptions.HTTPError as errh:
        await ctx.send(f"HTTP-ошибка: {errh}")
    except requests.exceptions.ConnectionError as errc:
        await ctx.send(f"Ошибка подключения: {errc}")
    except requests.exceptions.Timeout as errt:
        await ctx.send(f"Ошибка таймаута: {errt}")
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Что-то пошло не так: {err}")
    

UNSPLASH_ACCESS_KEY = "ТОКЕН unsplash"  # Замените на свой ключ доступа Unsplash

@bot.slash_command(description="Отправляет фото игровой тематики")
async def игромен(ctx: disnake.ApplicationCommandInteraction):
    try:
        # Отложите ответ, чтобы сообщить Discord, что бот работает над ним
        await ctx.response.defer()

        # Сделайте запрос к API Unsplash для получения случайного игрового обоя
        response = requests.get(
            f'https://api.unsplash.com/photos/random?query=gaming%20wallpaper&client_id={UNSPLASH_ACCESS_KEY}'
        )
        response.raise_for_status()  # Проверьте наличие ошибок в ответе

        data = response.json()
        image_url = data['urls']['regular']

        # Отправьте изображение в текстовый канал
        await ctx.send(content=image_url)
    except requests.exceptions.HTTPError as errh:
        await ctx.send(f"HTTP-ошибка: {errh}")
    except requests.exceptions.ConnectionError as errc:
        await ctx.send(f"Ошибка подключения: {errc}")
    except requests.exceptions.Timeout as errt:
        await ctx.send(f"Ошибка тайм-аута: {errt}")
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Что-то пошло не так: {err}")

@bot.slash_command(description="Отправляет сгенерированного персонажа")
async def нейроперс(ctx: disnake.ApplicationCommandInteraction):
    try:
        # Отложить ответ, чтобы показать, что бот работает над командой
        await ctx.response.defer()

        # Путь к папке с изображениями на вашем хостинге
        folder_path = "/путь_к_файлу/нейро_обои"

        # Получить список файлов в папке
        image_files = os.listdir(folder_path)

        if image_files:
            # Случайным образом выбрать одно изображение из списка
            image_filename = random.choice(image_files)
            
            # Путь к выбранному изображению
            image_path = os.path.join(folder_path, image_filename)

            # Отправить изображение в текстовый канал
            await ctx.send(file=disnake.File(image_path))
        else:
            await ctx.send("В папке нет изображений.")
    except Exception as e:
        await ctx.send(f"Произошла ошибка: {e}")

@bot.slash_command(description="Отправляет изображение для рабочего стола")
async def обои(ctx: disnake.ApplicationCommandInteraction):
    try:
        # Отложить ответ, чтобы показать, что бот работает над командой
        await ctx.response.defer()

        # Путь к папке с изображениями на рабочем столе
        folder_path = "/путь_к_файлу/пк_обои"

        # Получить список файлов в папке
        image_files = os.listdir(folder_path)

        if image_files:
            # Случайным образом выбрать одно изображение из списка
            image_filename = random.choice(image_files)
            
            # Путь к выбранному изображению
            image_path = os.path.join(folder_path, image_filename)

            # Отправить изображение в текстовый канал
            await ctx.send(file=disnake.File(image_path))
        else:
            await ctx.send("На рабочем столе нет изображений.")
    except Exception as e:
        await ctx.send(f"Произошла ошибка: {e}")
        
openai.api_key = "ТОКЕН openai"

@bot.slash_command(description="Генерирует ответ в стиле GPT-3.5")
async def чат(ctx: disnake.ApplicationCommandInteraction, задача: str):
    """Генерирует ответ в стиле GPT-3.5"""
    response = await generate_chat_response(задача)
    await ctx.followup.send(response)

async def generate_chat_response(задача):
    try:
        completion = await openai.Completion.create(
            engine="text-davinci-003",
            prompt=задача,
            api_key=openai.api_key
        )
        result = completion.choices[0].text if completion.choices else "No response generated"
        return result
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"


# Список игровых вопросов
game_questions = [
    "Какая ваша любимая игра из детства, которая оставила самое яркое впечатление?",
    "Какие жанры игр вы считаете наиболее увлекательными: открытый мир, головоломки или онлайн-сражения?",
    "Какое было ваше самое важное игровое достижение, на которое вы особенно гордитесь?",
    "Кажется ли вам, что играя в игры, мы можем изучить какие-то полезные навыки или умения?",
    "Какая игра вас поразила своей графикой или визуальным стилем?",
    "Кто ваши любимые герои или персонажи из игр? Что именно вас к ним тянет?",
    "Какие игры обычно выбираете для игры в компании с друзьями?",
    "Как бы вы выглядели в игровом мире, если бы могли стать персонажем игры?",
    "Отражают ли игры некоторые аспекты реальной жизни? Какие, по вашему мнению, наиболее точно?",
    "Какие игры вы бы хотели увидеть в будущем? Какие новые идеи или концепции вас заинтересовали бы?",
    "Какие игры вызывают у вас ностальгию за детством?",
    "Какие элементы игровой механики вам нравятся больше всего?",
    "Что для вас важнее: сюжет в игре или геймплей?",
    "Какая игра, на ваш взгляд, имеет самый интересный мир?",
    "Как вы относитесь к идеям образовательных игр? Могут ли они быть полезными?",
    "Какие игры вы предпочитаете – одиночные или многопользовательские?",
    "Считаете ли вы, что игры могут вдохновлять на творчество?",
    "Какую игру вы бы порекомендовали новичкам в мире гейминга?",
    "Есть ли у вас фаворит среди разработчиков игр?",
    "Какие игровые моменты вызывают у вас наибольшую эмоциональную отдачу?",
    "Как вы считаете, игры способствуют развитию мышления?",
    "Какой персонаж или герой вас разочаровал в итоге игры?",
    "Какие игры заставили вас задуматься о каких-то глубоких темах?",
    "Как вы относитесь к ремейкам и переизданиям старых игр?",
    "Как бы вы описали свой первый опыт в игровом мире?",
    "Какая игра, по вашему мнению, имеет самый захватывающий сюжет?",
    "Какие игры вы выбираете для релакса и отдыха?",
    "Какие игры вас удивили необычным геймплеем или механиками?",
    "Какие игры вам нравятся больше всего – классические или инновационные?",
    "Что важнее в многопользовательских играх: сотрудничество или соревнование?",
    "Какие игры помогли вам научиться решать проблемы в реальной жизни?",
    "Какие игры вы готовы проходить снова и снова?",
    "Какой персонаж игры, по вашему мнению, идеально подходит для вас?",
    "Какие игры вас вдохновляют на творчество и новые идеи?",
    "Что вы думаете о влиянии игр на общество и молодежь?",
    "Как вы относитесь к платным дополнениям и контенту в играх?",
    "Какие игры, по вашему мнению, имеют самую красивую и проработанную графику?",
    "Что вы думаете о возможности играть в режиме виртуальной реальности?",
    "Какие игры помогли вам научиться работать в команде?",
    "Как вы относитесь к тому, что некоторые игры могут быть настолько сложными?",
    "Какие игры вызывают у вас азарт и желание победить?",
    "Какие игры вас пугают или вызывают тревогу?",
    "Какая игра, на ваш взгляд, идеально сбалансирована по сложности?",
    "Какую игру вы бы хотели сыграть, если бы у вас было больше свободного времени?",
    "Как вы относитесь к сюжетам в играх, которые вызывают сильные эмоции?",
]


@bot.slash_command(description="Вопрос для размышления и обсуждения")
async def вопросник(ctx: disnake.ApplicationCommandInteraction):
  today = datetime.date.today()
  random.seed(today.year * 350 +
              today.timetuple().tm_yday)  # Фиксируем вопрос на день

  question = random.choice(game_questions)
  await ctx.response.send_message(question)


# Список игр
games_list = [
    "**Elden Ring**",
    "**The Witcher 3: Wild Hunt**",
    "**Grand Theft Auto V**",
    "**Red Dead Redemption 2**",
    "**Skyrim**",
    "**Fallout 4**",
    "**The Elder Scrolls Online**",
    "**World of Warcraft**",
    "**Final Fantasy XIV**",
    "**Call of Duty: Warzone**",
    "**Among Us**",
    "**Cyberpunk 2077**",
    "**Fortnite**",
    "**League of Legends**",
    "**Apex Legends**",
    "**Valorant**",
    "**Stardew Valley**",
    "**Overwatch**",
    "**Doom Eternal**",
    "**Assassin's Creed Valhalla**",
    "**Rocket League**",
    "**Animal Crossing: New Horizons**",
    "**Rainbow Six Siege**",
    "**Destiny 2**",
    "**Counter-Strike: Global Offensive**",
    "**Fall Guys**",
    "**Resident Evil Village**",
    "**Halo Infinite**",
    "**Far Cry 6**",
    "**Battlefield 2042**",
    "**Ghost of Tsushima**",
    "**Genshin Impact**",
    "**Dark Souls III**",
    "**Dota 2**",
    "**League of Legends**",
    "**StarCraft II**",
    "**Hearthstone**",
    "**Age of Empires IV**",
    "**Total War: Warhammer III**",
    "**Warcraft III: Reforged**",
    "**Age of Empires II: Definitive Edition**",
    "**StarCraft: Remastered**",
    "**Metro Exodus**",
    "**Horizon Forbidden West**",
    "**God of War (2018)**",
    "**The Last of Us Part II**",
    "**Uncharted 4: A Thief's End**",
    "**Spider-Man**",
    "**Ghost of Tsushima**",
    "**The Legend of Zelda: Breath of the Wild**",
    "**Super Mario Odyssey**",
    "**Stardew Valley**",
    "**Celeste**",
    "**Undertale**",
    "**Hollow Knight**",
    "**Cuphead**",
    "**Among Us**",
    "**Among Trees**",
    "**Slime Rancher**",
    "**Untitled Goose Game**",
    "**Minecraft**",
    "**Roblox**",
    "**Spider-Man 2**",
    "**Animal Crossing: New Horizons**",
    "**Mario Kart 8 Deluxe**",
    "**Super Smash Bros. Ultimate**",
    "**FIFA 23**",
    "**NBA 2K23**",
    "**WWE 2K23**",
]


@bot.slash_command(description="Выбирает игру которую ты должен поиграть")
async def вочтопоиграть(ctx: disnake.ApplicationCommandInteraction):
  """Выбирает случайную игру из списка"""
  random_game = random.choice(games_list)
  await ctx.response.send_message(
      f"Игра в которую ты должен поиграть: {random_game}")


@bot.slash_command(description="Рассылка сообщения всем участникам сервера")
async def рассылка(ctx: disnake.ApplicationCommandInteraction, *,
                   сообщение: str):
    try:
        # Отложить ответ, чтобы сообщить Discord, что бот работает над ним
        await ctx.response.defer()

        guild = ctx.guild
        участники = guild.members

        for участник in участники:
            try:
                if not участник.bot and участник.dm_channel is None:
                    await участник.create_dm()

                if not участник.bot:
                    if участник.dm_channel.permissions_for(
                            участник.guild.me).send_messages:
                        await участник.dm_channel.send(сообщение)
                    else:
                        текст = f"Не удалось отправить сообщение {участник.mention}: У вас отключены личные сообщения от ботов."
                        await ctx.response.send_message(текст, ephemeral=True)
            except disnake.errors.Forbidden:
                # Пропускаем участника, которому невозможно отправить сообщение
                pass
            except disnake.errors.HTTPException as e:
                текст = f"Не удалось отправить сообщение {участник.mention}: {e}"
                await ctx.response.send_message(текст, ephemeral=True)

        await ctx.response.send_message("Рассылка завершена!")
    except Exception as e:
        await ctx.send(f"Произошла ошибка при выполнении рассылки: {e}")

@bot.event
async def on_raw_reaction_add(payload):
  ваш_идентификатор_сообщения = 1195891792810356787
  реакции_и_роли = {
      '⬜': 1195867892504350831,  # GTA V
      '🟨': 1195867892063940678,  # Dota 2
      '🟧': 1195867892063940677,  # CS:GO 2
      '🟥': 1195867892063940676,  # Rust
      '🟩': 1195867892063940675,  # Minecraft
      '🟫': 1195867892063940674,  # Call of Duty
      '🟦': 1195867892063940673,  # Battlefield
      '🟪': 1195867892063940672,  # Другие игры
  }

  if payload.message_id == ваш_идентификатор_сообщения and payload.emoji.name in реакции_и_роли:
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member:
      role_id = реакции_и_роли[
          payload.emoji.name]  # Получаем идентификатор роли из словаря
      role = guild.get_role(role_id)

      if role:
        await member.add_roles(role)
        print(f'Добавлена роль {role.name} для {member.display_name}')

        try:
          # Отправляем уведомление в личные сообщения участнику
          await member.send(
              f'Роль **{role.name}** успешно добавлена ваш профиль!')
        except discord.errors.Forbidden:
          print(
              f'Не удалось отправить уведомление пользователю {member.display_name}: нет прав'
          )
      else:
        print(f'Роль с идентификатором {role_id} не найдена на сервере')


@bot.event
async def on_raw_reaction_remove(payload):
  ваш_идентификатор_сообщения = 1195891792810356787
  реакции_и_роли = {
      '⬜': 1195867892504350831,  # GTA V
      '🟨': 1195867892063940678,  # Dota 2
      '🟧': 1195867892063940677,  # CS:GO 2
      '🟥': 1195867892063940676,  # Rust
      '🟩': 1195867892063940675,  # Minecraft
      '🟫': 1195867892063940674,  # Call of Duty
      '🟦': 1195867892063940673,  # Battlefield
      '🟪': 1195867892063940672,  # Другие игры
  }

  if payload.message_id == ваш_идентификатор_сообщения and payload.emoji.name in реакции_и_роли:
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member:
      role_id = реакции_и_роли[
          payload.emoji.name]  # Получаем идентификатор роли из словаря
      role = guild.get_role(role_id)

      if role:
        await member.remove_roles(role)
        print(f'Удалена роль {role.name} для {member.display_name}')

        try:
          # Отправляем уведомление в личные сообщения участнику
          await member.send(
              f'Роль **{role.name}** успешно удалена с вашого профиля!')
        except discord.errors.Forbidden:
          print(
              f'Не удалось отправить уведомление пользователю {member.display_name}: нет прав'
          )
      else:
        print(f'Роль с идентификатором {role_id} не найдена на сервере')


@bot.slash_command(description="Отправить сообщение в канал")
async def cообщение_канал(ctx: disnake.ApplicationCommandInteraction,
                          канал: disnake.TextChannel, *, сообщение: str):
  """Отправляет сообщение в канал"""
  await канал.send(сообщение, allowed_mentions=disnake.AllowedMentions.none())
  response_msg = f"Сообщение успешно отправлено в канал {канал.mention}"
  await ctx.response.send_message(response_msg, ephemeral=True)


@bot.slash_command(name="интеграцию_канал",description="Отправить интеграцию в канал")
async def uнтеграцию_канал(
    ctx: disnake.ApplicationCommandInteraction,
    канал: disnake.TextChannel,
    цвет: str,
    ссылка_на_фотографию: str,
    сообщение: str,
    верхнее_сообщение:
    str = "<@&1195867892521123853>, в команды Game Quest, имеются значимые обновления, которыми мы хотели бы поделиться",
    вторая_строка: str = None):
  """Отправить интеграцию в канал"""
  # Проверка на правильный формат шестнадцатеричного кода цвета
  if len(цвет) != 7 or not цвет.startswith("#"):
    response_msg = "Неправильный формат цвета. Используйте шестнадцатеричный код цвета в формате #RRGGBB."
    await ctx.response.send_message(response_msg, ephemeral=True)
    return

  if вторая_строка is not None:
    сообщение = f"{сообщение}\n\n{вторая_строка}"

  try:
    embed = disnake.Embed(description=сообщение, color=int(цвет[1:], 16))
  except ValueError:
    response_msg = "Неправильный формат цвета. Используйте шестнадцатеричный код цвета в формате #RRGGBB."
    await ctx.response.send_message(response_msg, ephemeral=True)
    return

  embed.set_image(url=ссылка_на_фотографию)  # Добавить фотографию в сообщение
  await канал.send(content=верхнее_сообщение, embed=embed)
  response_msg = f"Сообщение с интеграцией успешно отправлено в канал {канал.mention}"
  await ctx.response.send_message(response_msg, ephemeral=True)

  return response.choices[0].text.strip()

# Чистка сообщений на сервере
@bot.event
async def on_member_update(before, after):
    if len(after.roles) > len(before.roles):
        role_ids = [role.id for role in after.roles]
        if 1205268581957501010 in role_ids:   # ID роли
            await delete_last_messages(after, 10)
            await asyncio.sleep(14400)  # 4 часа в секундах
            await after.remove_roles(after.guild.get_role(1205268581957501010))

async def delete_last_messages(member, count):
    for channel in member.guild.text_channels:  # Получаем все текстовые каналы на сервере
        async for message in channel.history(limit=count):
            if message.author == member:
                await message.delete()
                count -= 1
                if count == 0:
                    break  # Если удалили 10 сообщений, выходим из цикла
                                        
# ID роли для уведомлений о наказании
PUNISHMENT_ROLE_ID = 1205268581957501010

@bot.event
async def on_member_update(before, after):
    # Проверяем, если у участника изменилась роль
    if before.roles != after.roles:
        # Проверяем, если у участника добавлена роль наказания
        if disnake.utils.find(lambda r: r.id == PUNISHMENT_ROLE_ID, after.roles):
            # Создаем встроенное сообщение с указанным цветом
            embed = disnake.Embed(
                title="Уведомление о наказании",
                description="К сожалению, ваше сообщение было заблокировано автоматически из-за нарушения правил сервера. Чтобы снова иметь возможность отправлять сообщения, пожалуйста, повысьте свой позывной на сервере!",
                color=disnake.Color.from_rgb(200, 1, 71)  # Цвет #C80147
            )
            # Отправляем встроенное сообщение
            await after.send(embed=embed)
        # Проверяем, если у участника снята роль наказания
        elif disnake.utils.find(lambda r: r.id == PUNISHMENT_ROLE_ID, before.roles) and not disnake.utils.find(lambda r: r.id == PUNISHMENT_ROLE_ID, after.roles):
            # Создаем встроенное сообщение с указанным цветом
            embed = disnake.Embed(
                title="Уведомление о снятии наказания",
                description="Рады сообщить, что ограничения на вашем аккаунте были сняты! Надеемся, что вы будете продолжать соблюдать правила сервера и рекомендуем вам повысить свой позывной на сервере!",
                color=disnake.Color.from_rgb(200, 1, 71)  # Цвет #C80147
            )
            # Отправляем встроенное сообщение
            await after.send(embed=embed)
                        
@bot.slash_command(description="Забанить участника")
async def ban(ctx: disnake.ApplicationCommandInteraction, member: disnake.Member):
    try:
        # Создаем встроенное сообщение о бане с указанным цветом
        embed = disnake.Embed(
            title="Уведомление о бане",
            description="Вас забанили на сервере. Обратитесь к администратору для получения дополнительной информации.",
            color=0xC80147  # Цвет #C80147
        )
        # Отправляем встроенное сообщение в личные сообщения пользователя
        await member.send(embed=embed)
    except disnake.errors.Forbidden:
        await ctx.send(f"Невозможно отправить уведомление пользователю {member} о бане: доступ к личным сообщениям заблокирован.")
    finally:
        # Применяем бан
        await ctx.guild.ban(member)
                
@bot.slash_command(description="Выгнать участника")
async def kick(ctx: disnake.ApplicationCommandInteraction, member: disnake.Member):
    try:
        # Создаем встроенное сообщение о вигнании с указанным цветом
        embed = disnake.Embed(
            title="Уведомление о вигнании",
            description="Вас исключили из сервера. Если у вас возникли вопросы, обратитесь к администратору.",
            color=0xC80147  # Цвет #C80147
        )
        # Отправляем встроенное сообщение в личные сообщения пользователя
        await member.send(embed=embed)
    except disnake.errors.Forbidden:
        await ctx.send(f"Невозможно отправить уведомление пользователю {member} о вигнании: доступ к личным сообщениям заблокирован.")
    finally:
        # Применяем вигнание
        await member.kick()
               
@bot.slash_command(description="Выдать участнику тайм-аут")
async def timeout(ctx: disnake.ApplicationCommandInteraction, member: disnake.Member):
    try:
        # Создаем встроенное сообщение о тайм-ауте с указанным цветом
        embed = disnake.Embed(
            title="Уведомление о тайм-ауте",
            description="Вам был выдан тайм-аут на сервере. Пожалуйста, ожидайте окончания тайм-аута или обратитесь к администратору для получения дополнительной информации.",
            color=0xC80147  # Цвет #C80147
        )
        # Отправляем встроенное сообщение в личные сообщения пользователя
        await member.send(embed=embed)
    except disnake.errors.Forbidden:
        await ctx.send(f"Невозможно отправить уведомление пользователю {member} о тайм-ауте: доступ к личным сообщениям заблокирован.")
    finally:
        # Применяем тайм-аут
        # Замените значение 600 на желаемую продолжительность тайм-аута в секундах (в данном случае 10 минут)
        await member.timeout(600)     
        
@bot.slash_command(description="Приглашение к оценке сервера")
async def прокачка(ctx: disnake.ApplicationCommandInteraction):
    # Ваше сообщение с приглашением к оценке сервера
    message = "Дайте оценку нашему серверу, если не сложно:\n\n" \
              "※ DiscordServer.Info: https://discordserver.info/1195867892063940671\n" \
              "※ ServerDiscord: https://server-discord.com/1195867892063940671"

    # Отправляем сообщение в текстовый канал
    await ctx.send(content=message)

@bot.slash_command(description="Приглашение к социальным сетям")
async def соцсеть(ctx: disnake.ApplicationCommandInteraction):
    # Ваша ссылка на социальные сети
    social_media_link = "https://bit.ly/3Px7sCH"

    # Отправляем сообщение с ссылкой
    await ctx.send(content=f"Присоединяйтесь к нашим сообществам в социальных сетях:\n{social_media_link}")
    
@bot.slash_command(description="Поддержите наш проект донатом")
async def донат(ctx: disnake.ApplicationCommandInteraction):
    # Ваши ссылки на донат
    patreon_link = "https://www.patreon.com/andremuhamad"
    donationalerts_link = "https://www.donationalerts.com/r/andremuhamad"

    # Отправляем сообщение с ссылками на донат
    await ctx.send(content=f"**Поддержите наш проект донатом:**\nↈ {donationalerts_link}\nↈ {patreon_link}")
    
@bot.slash_command(description="Поднимает настроение участнику сервера")
async def грусно(ctx: disnake.ApplicationCommandInteraction):
    uplifting_messages = [
        "Забудь об облаках, давай вместе посмотрим на яркую сторону жизни!",
        "Сегодня может быть серым, но завтра обещает быть ярче и лучше!",
        "Помни, что ты уникален и способен на великие дела!",
        "Улыбнись, и весь мир вокруг тебя станет светлее!",
        "Время от времени даже самые темные облака пропускают солнечные лучи. Так что держись!",
        "Не грусти, всегда есть место для радости!",
        "Жизнь прекрасна, особенно с тобой в ней!",
        "Веселись! Завтра будет лучше!",
        "Улыбнись, и весь мир улыбнется в ответ!",
        "Не переживай, лучшие моменты еще впереди!",
        "Не позволяйте темным мыслям завладеть вашим светлым днем!",
        "Сегодня может быть тяжело, но завтра придет новый день полный возможностей!",
        "Ты умеешь преодолевать трудности. Верь в себя!",
        "Не забывай, что у тебя есть поддержка вокруг. Мы здесь для тебя!",
        "Даже самый трудный день заканчивается. Всегда есть шанс на лучший завтра!",
        "Ты сильнее, чем думаешь, и способен на большее, чем представляешь!",
        "Помни, что каждый шаг к лучшему находится в тебе!",
        "Улыбнись, и весь мир улыбнется в ответ!"
    ]

    uplifting_message = random.choice(uplifting_messages)
    await ctx.send(content=uplifting_message)    
    
@bot.slash_command(description="Показывает команду Game Quest")
async def создатели(ctx: disnake.ApplicationCommandInteraction):
    creators_info = {
        "Андрей Мухамед": "https://vk.com/addmirall_times",
        "Михаил Михайлов": "https://vk.com/mihatosno",
        "Елена Калинина": "https://vk.com/id6422484",
        # Добавьте нужное количество персонажей и их ссылок
    }

    creators_message = "\n".join([f"**{creator}:** ```{link}```" for creator, link in creators_info.items()])
    await ctx.send(content=creators_message)  
    
@bot.slash_command(description="Показывает задержкe бота")
async def пинг(ctx: disnake.ApplicationCommandInteraction):
    latency = round(bot.latency * 1000)  # Пинг в миллисекундах
    await ctx.send(f'Задержка бота: `{latency}` мс')    

         



















special_channel_id = 1195867893938794651  # ID специального голосового канала
category_id = 1195867893938794649  # ID категории для создания канала
allowed_role = [1195867892550479985, 1195867892550479984, 1195867892550479983, 1195867892521123859, 1201172180558417931, 1196983887608426660, 1195867892521123858, 1195867892521123857, 1195867892521123856]  # ID ролей, которым разрешен доступ к каналу
bot_created_channels = {}  # Словарь для хранения ссылок на созданные каналы

@bot.event
async def on_voice_state_update(member, before, after):
    global bot_created_channels

    guild = member.guild

    special_channel = guild.get_channel(special_channel_id)
    category = guild.get_channel(category_id)

    if after.channel and after.channel.id == special_channel_id:  # Проверяем, что пользователь зашел в специальный канал
        if category:
            overwrites = {
                guild.default_role: disnake.PermissionOverwrite(connect=False),  # Запрещаем доступ для всех ролей по умолчанию
                member: disnake.PermissionOverwrite(connect=True, manage_channels=True, move_members=True, mute_members=True, deafen_members=True, create_instant_invite=True)  # Добавляем разрешения для управления каналом и создания приглашений
            }

            # Получение объекта владельца сервера
            server_owner = guild.get_member(guild.owner_id)
            
            if member == server_owner:
                # Предоставляем владельцу специальные права доступа к категории и специальному каналу
                overwrites[server_owner] = discord.PermissionOverwrite(connect=True, manage_channels=True)
              
            for role_id in allowed_role:
                role = guild.get_role(role_id)
                if role:
                    overwrites[role] = disnake.PermissionOverwrite(connect=True)

            new_channel = await category.create_voice_channel(f"Лейтенант {member.name}", overwrites=overwrites)
            bot_created_channels[member.id] = new_channel
            await member.move_to(new_channel)

    if before.channel and before.channel.id != special_channel_id and len(before.channel.members) == 0:
        if before.channel.id in [channel.id for channel in bot_created_channels.values()]:
            await before.channel.delete()
            bot_created_channels = {k: v for k, v in bot_created_channels.items() if v.id != before.channel.id}

























bot.run("ТВОЙ ТОКЕН БОТА")
