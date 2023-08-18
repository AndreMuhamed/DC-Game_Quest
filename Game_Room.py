from keep_alive import keep_alive
import disnake
from disnake.ext import commands, tasks
import typing
import discord
import os
import datetime
import random
import requests
import openai

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())

@bot.event
async def on_member_join(member):
    welcome_channel_id = 420868571422392325  # Замените это на ID канала, куда хотите отправлять приветственные сообщения
    welcome_channel = bot.get_channel(welcome_channel_id)
    
    if welcome_channel is not None:
        gif_url = "https://i.gifer.com/3OaZB.gif"  # Замените это на вашу ссылку на гифку
        gif_response = requests.get(gif_url)
        
        with open("welcome.gif", "wb") as f:
            f.write(gif_response.content)
        
        with open("welcome.gif", "rb") as f:
            gif_file = disnake.File(f, filename="welcome.gif")
            await welcome_channel.send(content=f"Здравия желаю {member.mention}! Обязательно ознакомьтесь с правилами сервера, чтобы не упустить важную информацию. А чтобы найти дополнительный увлекательный контент, не забудьте пройти по разделам навигации. И не упустите шанс познакомиться с другими участниками — ведь за каждым никнеймом скрывается своя уникальная история и интересы!", file=gif_file)

        os.remove("welcome.gif")  # Удаляем временный файл после отправки

@bot.slash_command(description="Сообщите о нарушении правил сервера")
async def отчёт(ctx: disnake.ApplicationCommandInteraction, пользователь: disnake.Member, причина: str, доказательство: typing.Optional[str] = None):
    """Сообщает о нарушении правил сервера"""
    модераторы = ctx.guild.get_role(421378470392627213)
    отчет_msg = f"{модераторы.mention}, пользователь {пользователь.mention} был зарепорчен по причине: {причина}"
    
    if доказательство:
        отчет_msg += f"\nДоказательства: {доказательство}"
    
    channel = bot.get_channel(922996283034177587)
    if channel:
        await channel.send(отчет_msg)
    
    await ctx.response.send_message("Ваше сообщение о нарушении было успешно отправлено модераторам")

@bot.slash_command(description="Отправить запрос на присоединение к команде")
async def присоединиться(ctx: disnake.ApplicationCommandInteraction, кем: str, возраст: int):
    """Отправляет запрос на присоединение к команде"""   
    admin_role = ctx.guild.get_role(421379945370222592)  # замените на фактический ID роли админа
    message = f'''{admin_role.mention}, пользователь {ctx.author.mention} хочет присоединиться к команде.
    
**Роль: {кем}.**
**Возраст: {возраст} лет.**
\nПожалуйста, предоставьте ему доступ, если это возможно. '''
    
    # Получение канала, в который будет отправлено сообщение
    канал = bot.get_channel(922996283034177587)  # замените на фактический ID канала, куда вы хотите отправить сообщение
    
    # Отправка сообщения в канал запросов на присоединение к команде и упоминание админа
    await канал.send(message)
    
    # Ответ на команду пользователю, который вызвал команду
    await ctx.response.send_message("Ваш запрос на присоединение к команде был успешно отправлен.")

# ID канала для отправки вопросов
QUESTION_CHANNEL_ID = 922996283034177587

@bot.slash_command(description="Спросить вопрос о сервер")
async def помощ(ctx, *, вопрос):
    # получение объекта канала для отправки вопроса
    вопрос_channel = bot.get_channel(QUESTION_CHANNEL_ID)
    
    # отправка вопроса в канал
    await вопрос_channel.send(f"Вопрос от {ctx.author.mention}: {вопрос}")
    
    # отправка подтверждения вопроса в канал, откуда была вызвана команда
    await ctx.send("Ваш вопрос был отправлен.")

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
    "Если геймер долго не спит, это не баг — это его способность настроения 'не засыпать до победы'!""Почему герой из RPG всегда говорит в повелительном наклонении? Потому что ему нельзя отказаться от квестов!",
]

@bot.slash_command(description="Отправляем анекдоты")
async def анекдот(ctx: disnake.ApplicationCommandInteraction):
    random_анекдот = random.choice(anecdotes)
    await ctx.response.send_message(random_анекдот)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(description="Отправляем твою крутую фотку")
async def фотка(context: disnake.ApplicationCommandInteraction):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    image_url = data[0]['url']
    await context.response.send_message(image_url)

PLASH_API_KEY = "JU_FnZ9tmvKZ4xLX2POVUdg0GpU3uGc8lW-1GLp9EbE"

@bot.slash_command(description="Отправляет фото твоего компьютера")
async def пк(context: disnake.ApplicationCommandInteraction):
    response = requests.get(f'https://api.unsplash.com/photos/random?query=computer&client_id={PLASH_API_KEY}')
    data = response.json()
    image_url = data['urls']['regular']
    await context.send(content=image_url)

message_threshold_1 = 60
message_counter_1 = 0
message_threshold_2 = 40
message_counter_2 = 0

users = {}

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global message_counter_1, message_counter_2

    # Проверяем, что сообщение не от бота и не в личных сообщениях
    if not message.author.bot and isinstance(message.channel, disnake.TextChannel):
        message_counter_1 += 1
        message_counter_2 += 1

        if message_counter_1 == message_threshold_1:
            channel = message.channel
            await channel.send('''**Не забудьте подписать на другие наши социальные сети нашего Discord-сервера:**
◈ Game Room: Игроновинки: https://www.youtube.com/@GameRoom_news
◈ Паблик ВКонтакте: https://vk.com/gameroom_news
◈ Game Room Live: https://www.youtube.com/@GameRoomNews''')
            message_counter_1 = 0

        if message_counter_2 == message_threshold_2:
            channel = message.channel
            await channel.send('''**Поддержите наш проект донатом:**  
ↈ https://www.patreon.com/andremuhamad
ↈ https://www.donationalerts.com/r/andremuhamad
''')
            message_counter_2 = 0

    # Отвечаем на приветственное сообщение пользователя в определенном канале
    if message.content.lower().startswith(('привет', 'хай', 'салют', 'привіт', 'всем привет', 'здарова', 'приветствую', 'добрый день', 'доброе утро', 'добрый вечер', 'Рад встрече')):
        response = 'Рады приветствовать вас. Мы очень рады видеть вас здесь и желаем, чтобы ваше время провождение было приятным и полным позитивной атмосферы. Если у вас возникнут вопросы или вам понадобится помощь, пожалуйста, не стесняйтесь обращаться к администраторам или модераторам через команду в боте. Мы также настоятельно просим вас соблюдать правила сервера.'

        channel_id = 420868571422392325  # Замените YOUR_CHANNEL_ID на фактический ID вашего канала
        if isinstance(message.channel, disnake.DMChannel):
            await message.author.send(response)
        elif message.channel.id == channel_id:
            await message.channel.send(response)

    # Отвечаем на сообщения пользователя в личных сообщениях
    if message.author != bot.user and isinstance(message.channel, disnake.DMChannel):
        response = "***Благодарю вас за сообщение! На данный момент бот не может общаться, так как занят работой круглосуточно на сервере:*** https://discord.gg/pGkgzSKDxD"
        await message.author.send(response)

    await bot.process_commands(message)

openai.api_key = os.environ["openai.api"]  # Вставьте свой API-ключ OpenAI

@bot.slash_command(description="Генерирует ответ в стиле GPT-3.5")
async def чат(ctx: disnake.ApplicationCommandInteraction, вопрос: str):
    """Генерирует ответ в стиле GPT-3.5"""
    response = generate_chat_response(вопрос)
    await ctx.response.send_message(response)

def generate_chat_response(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Используйте текстовый движок для нужного языка
        prompt=user_input,
        max_tokens=50,  # Максимальное количество токенов в ответе
        temperature=0.7,  # Контролирует разнообразие ответов (чем выше, тем разнообразнее)
        n=1,  # Количество сгенерированных ответов
        stop=None,  # Строка остановки, которую можно использовать для прекращения генерации ответа
    )
    return response.choices[0].text.strip()  # Возвращаем текст ответа

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
async def вопрос_дня(ctx: disnake.ApplicationCommandInteraction):
    today = datetime.date.today()
    random.seed(today.year * 1000 + today.timetuple().tm_yday)  # Фиксируем вопрос на день

    question = random.choice(game_questions)
    await ctx.response.send_message(question)

# Список игр
games_list = [
    "**The Witcher 3: Wild Hunt**",
    "**Minecraft**",
    "**Grand Theft Auto V**",
    "**Call of Duty: Warzone**",
    "**Among Us**",
    "**Cyberpunk 2077**",
    "**Fortnite**",
    "**League of Legends**",
    "**Apex Legends**",
    "**Valorant**",
    "**Red Dead Redemption 2**",
    "**Stardew Valley**",
    "**Overwatch**",
    "**Doom Eternal**",
    "**Assassin's Creed Valhalla**",
    "**Rocket League**",
    "**Animal Crossing: New Horizons**",
    "**Rainbow Six Siege**",
    "**Destiny 2**",
    "**World of Warcraft**",
    "**Counter-Strike: Global Offensive**",
    "**Fall Guys**",
    "**The Elder Scrolls V: Skyrim**",
    "**Resident Evil Village**",
    "**Halo Infinite**",
    "**Far Cry 6**",
    "**Battlefield 2042**",
    "**Ghost of Tsushima**",
    "**Genshin Impact**",
    "**Dark Souls III**",

]

@bot.slash_command(description="Выбирает игру имено для тебя")
async def игра_дня(ctx: disnake.ApplicationCommandInteraction):
    """Выбирает случайную игру из списка"""
    random_game = random.choice(games_list)
    await ctx.response.send_message(f"Игра в которую сегодня ты должен поиграть: {random_game}")

@bot.slash_command(description="Отправить сообщение в канал")
async def cообщение_канал(ctx: disnake.ApplicationCommandInteraction, канал: disnake.TextChannel, *, сообщение: str):
    """Отправляет сообщение в канал"""
    await канал.send(сообщение, allowed_mentions=disnake.AllowedMentions.none())
    response_msg = f"Сообщение успешно отправлено в канал {канал.mention}"
    await ctx.response.send_message(response_msg, ephemeral=True)

@bot.slash_command(name="интеграцию_канал", description="Отправить интеграцию в канал")
async def uнтеграцию_канал(ctx: disnake.ApplicationCommandInteraction, канал: disnake.TextChannel, цвет: str, ссылка_на_фотографию: str, сообщение: str, верхнее_сообщение: str = "<@&990306177617395713>, у нас, команды Game Room: Игроновинки, имеются значимые обновления, которыми мы хотели бы поделиться", вторая_строка: str = None):
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

# Пример вызова команды: /uнтеграцию_канал <канал> <цвет> <ссылка_на_фотографию> <сообщение> <верхнее_сообщение>
# Значение в угловых скобках <> замените на соответствующие значения при вызове команды.
# Например: /uнтеграцию_канал #general #7d002c https://example.com/image.jpg "Привет, мир!" "Важное объявление"

    return response.choices[0].text.strip()

keep_alive()
bot.run(os.environ["Token"])
