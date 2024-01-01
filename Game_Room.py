from keep_alive import keep_alive
import disnake
from disnake.ext import commands, tasks
from disnake import PermissionOverwrite, Member, Guild, Activity, ActivityType
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
intents.voice_states = True #
intents.guilds = True #

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
      await welcome_channel.send(
          f"Здравия желаю {member.mention}! Обязательно ознакомьтесь с правилами сервера, чтобы не упустить важную информацию. А чтобы найти дополнительный увлекательный контент, не забудьте пройти по разделам навигации. И не упустите шанс познакомиться с другими участниками — ведь за каждым никнеймом скрывается своя уникальная история и интересы!",
          file=gif_file)

    os.remove("welcome.gif")  # Удаляем временный файл после отправки


message_threshold_1 = 60  # Измените на нужное вам значение
message_counter_1 = 0
message_threshold_2 = 40  # Измените на нужное вам значение
message_counter_2 = 0

users = {}

@bot.event
async def on_message(message):
    if message.channel.id == 421382342595182602:  # Замените YOUR_CHANNEL_ID на ID вашего канала
        emoji_ids = [1146196867982565497, 1146401819082379347, 1146223723746164757, 1146401807854223441, 1146196860176961653]  # Замените на ID ваших эмодзи
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
◈ Game Room: Игроновинки: https://www.youtube.com/@GameRoom_news
◈ Паблик ВКонтакте: https://vk.com/gameroom_news
◈ Game Room Live: https://www.youtube.com/@GameRoom_Live''')
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
             'приветствую', 'добрый день', 'ку', 'Hello', 'хаю хай', 'Hi',
             'доброе утро', 'добрый вечер', 'бонжур', 'Рад встрече')):
        response = 'Рады приветствовать вас. Мы очень рады видеть вас здесь и желаем, чтобы ваше время провождение было приятным и полным позитивной атмосферы. Если у вас возникнут вопросы или вам понадобится помощь, пожалуйста, не стесняйтесь обращаться к администраторам или модераторам через команду в боте. Мы также настоятельно просим вас соблюдать правила сервера.'

        channel_id = 420868571422392325  # Замените YOUR_CHANNEL_ID на фактический ID вашего канала
        if isinstance(message.channel, disnake.DMChannel):
            await message.author.send(response)
        elif message.channel.id == channel_id:
            await message.channel.send(response)

    # Отвечаем на сообщения пользователя в личных сообщениях
    if message.author != bot.user and isinstance(message.channel, disnake.DMChannel):
        response = "**Благодарю вас за сообщение! На данный момент бот не может общаться, так как занят работой круглосуточно на сервере:** https://discord.gg/pGkgzSKDxD"
        await message.author.send(response)

    await bot.process_commands(message)
  

@bot.slash_command(description="Отправить информацию о нарушении на сервере")
async def отчёт(ctx: disnake.ApplicationCommandInteraction,
                пользователь: disnake.Member,
                причина: str,
                доказательство: str = None):
    """Отправляет интеграцию в фиксированный канал жалоб"""
    канал = bot.get_channel(1175480769364373725)
    цвет = "#7d002c"

    пользователь_заявник = ctx.author

    отчет_msg = f"**{'### НАРУШЕНИЯ НА СЕРВЕРЕ'.upper()}**На пользователя {пользователь.mention} была подана жалоба от {пользователь_заявник.mention}\n\n**Причина нарушения:**\n```{причина}```"

    if доказательство:
        отчет_msg += f"\n\n**Доказательство нарушения:**\n```{доказательство}```"

    embed = disnake.Embed(description=отчет_msg, color=int(цвет[1:], 16))

    if канал:
        message = await канал.send(embed=embed)
        emojis = ['🟢', '🔴']
        for emoji in emojis:
            await message.add_reaction(emoji)

    await пользователь_заявник.send(
        "Ваша жалоба была успешно отправлена: **Команде Game Room: Игроновинки**")


@bot.slash_command(description="Отправить запрос на присоединение к команде")
async def присоединиться(ctx: disnake.ApplicationCommandInteraction, кем: str, возраст: int):
    """Отправляет запрос на присоединение к команде"""
    канал = bot.get_channel(1175482013348806666)
    цвет = "#7d002c"

    сообщение = f"### ЗАПРОС НА ПРИСОЕДИНЕНИЕ\n\nПользователь {ctx.author.mention} хочет присоединиться к команде\n\n**Роль:**\n```{кем}```\n**Возраст:**\n```{возраст} лет```"

    embed = disnake.Embed(description=сообщение, color=int(цвет[1:], 16))

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await ctx.author.send("Ваш запрос на присоединение успешно отправлен: **Команде Game Room: Игроновинки**")


@bot.slash_command(description="Задать вопрос о сервере")
async def помощ(ctx, вопрос: str, ссылка_на_ваш_скриншот: str = None):
    канал = bot.get_channel(1175481819731329054)
    пользователь = ctx.author

    вопрос_msg = f"### ВОПРОСЫ О СЕРВЕРЕ\n\nИнтересный вопрос о сообществе от: {пользователь.mention}\n\n**Вопрос:**\n```{вопрос}```"

    цвет = "#7d002c"

    embed = disnake.Embed(description=вопрос_msg, color=int(цвет[1:], 16))

    if ссылка_на_ваш_скриншот:
        embed.add_field(name="\n**Дополнительная информация:**", value=f"```{ссылка_на_ваш_скриншот}```", inline=False)

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await пользователь.send(
            "Ваш вопрос был успешно отправлен: **Команде Game Room: Игроновинки**")


@bot.slash_command(description="Отправить идею для сервера или бота")
async def идея(ctx: disnake.ApplicationCommandInteraction, категория: str, описание_идеи: str, ссылка_на_ваш_скриншот: str = None):
    канал = bot.get_channel(1175482399191204004)  # Замените на ID вашего канала для идей

    пользователь = ctx.author

    идея_msg = f"### ИДЕИ ДЛЯ СЕРВЕРА\n\nПользователь {пользователь.mention} предложил модель для развития\n\n**Категория:** \n```{категория}```\n**Описание идеи:**\n```{описание_идеи}```"

    цвет = "#7d002c"

    embed = disnake.Embed(description=идея_msg, color=int(цвет[1:], 16))

    if ссылка_на_ваш_скриншот:
        embed.add_field(name="\n**Дополнительная информация:**", value=f"```{ссылка_на_ваш_скриншот}```", inline=False)

    if канал:
        sent_message = await канал.send(embed=embed)
        await sent_message.add_reaction('🟢')
        await sent_message.add_reaction('🔴')

        await пользователь.send(
            "Ваша идея была успешно отправлена: **Команде Game Room: Игроновинки**")


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


@bot.slash_command(description="Отправляем анекдоты")
async def анекдот(ctx: disnake.ApplicationCommandInteraction):
  random_анекдот = random.choice(anecdotes)
  await ctx.response.send_message(random_анекдот)


@bot.slash_command(description="Отправляем твою крутую фотку")
async def фотка(context: disnake.ApplicationCommandInteraction):
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  data = response.json()
  image_url = data[0]['url']
  await context.response.send_message(image_url)

PLASH_API_KEY = "JU_FnZ9tmvKZ4xLX2POVUdg0GpU3uGc8lW-1GLp9EbE"

@bot.slash_command(description="Отправляет фото твоего компьютера")
async def пк(context: disnake.ApplicationCommandInteraction):
  response = requests.get(
      f'https://api.unsplash.com/photos/random?query=computer&client_id={PLASH_API_KEY}'
  )
  data = response.json()
  image_url = data['urls']['regular']
  await context.send(content=image_url)

openai.api_key = os.environ["OPENAI_API_KEY"]

@bot.slash_command(description="Генерирует ответ в стиле GPT-3.5")
async def чат(ctx: disnake.ApplicationCommandInteraction, задача: str):
    """Генерирует ответ в стиле GPT-3.5"""
    response = await generate_chat_response(задача)
    await ctx.followup.send(response)

async def generate_chat_response(user_input):
    from openai import ChatCompletion
    completion = ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {
                "role": "system",
                "content": user_input
            }
        ],
        api_key=openai.api_key
    )
    result = completion["choices"][0]["message"]["content"] if completion["choices"] else "No response generated"
    return result


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
async def вопросдня(ctx: disnake.ApplicationCommandInteraction):
  today = datetime.date.today()
  random.seed(today.year * 1000 +
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


@bot.event
async def on_raw_reaction_add(payload):
  ваш_идентификатор_сообщения = 1173357569780224050
  реакции_и_роли = {
      '⬜': 1173012037459259392,  # GTA V
      '🟨': 1173012131843682385,  # Dota 2
      '🟧': 1173012240841068584,  # CS:GO
      '🟥': 1173012306096046151,  # Rust
      '🟩': 1173012366095564830,  # Minecraft
      '🟫': 1173012438824779806,  # Call of Duty
      '🟦': 1173012498526515370,  # Battlefield
      '🟪': 1173012546937176144,  # Другие игры
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
  ваш_идентификатор_сообщения = 1173357569780224050
  реакции_и_роли = {
      '⬜': 1173012037459259392,  # GTA V
      '🟨': 1173012131843682385,  # Dota 2
      '🟧': 1173012240841068584,  # CS:GO
      '🟥': 1173012306096046151,  # Rust
      '🟩': 1173012366095564830,  # Minecraft
      '🟫': 1173012438824779806,  # Call of Duty
      '🟦': 1173012498526515370,  # Battlefield
      '🟪': 1173012546937176144,  # Другие игры
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
    str = "<@&990306177617395713>, в команды Game Room: Игроновинки, имеются значимые обновления, которыми мы хотели бы поделиться",
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

@bot.event
async def on_ready():
    print(f"Бот запуснился як {bot.user}")

    activity = Activity(type=ActivityType.watching, name="Game Room: Игроновинки")
    await bot.change_presence(activity=activity)

    second_channel_id = 1172167660298063964  # Замените ID другого голосового канала
    second_channel = bot.get_channel(second_channel_id)

    if second_channel:
        try:
            await second_channel.connect()
            print(f"Успешное подключение к {second_channel.name}")
        except Exception as e:
            print(f"Ошибка при подключении к каналу {second_channel}: {e}")
    else:
        print(f"Канал с ID {second_channel_id} не найден")












special_channel_id = 1180547378030313592  # ID специального голосового канала
category_id = 1180115281104863292  # ID категории для создания канала
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
                guild.default_role: disnake.PermissionOverwrite(connect=False),
                member: disnake.PermissionOverwrite(connect=True)
            }

            # Получение объекта владельца сервера
            server_owner = guild.get_member(guild.owner_id)
            
            if member == server_owner:
                # Предоставляем владельцу специальные права доступа к категории и специальному каналу
                overwrites[server_owner] = discord.PermissionOverwrite(connect=True, manage_channels=True)
              
            new_channel = await category.create_voice_channel(f"Лейтенант {member.name}", overwrites=overwrites)
            bot_created_channels[member.id] = new_channel
            await member.move_to(new_channel)

    if before.channel and before.channel.id != special_channel_id and len(before.channel.members) == 0:
        if before.channel.id in [channel.id for channel in bot_created_channels.values()]:
            await before.channel.delete()
            bot_created_channels = {k: v for k, v in bot_created_channels.items() if v.id != before.channel.id}
































































keep_alive()
bot.run(os.environ["Token"])
