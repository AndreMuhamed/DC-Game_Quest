from keep_alive import keep_alive
import disnake
import typing
import discord
import random
import requests
import openai

bot = disnake.Client()

from discord.ext import commands
from disnake.ext import commands
from disnake.embeds import Colour

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())

@bot.slash_command(description="Сообщите о нарушении правил сервера")
async def отчёт(ctx: disnake.ApplicationCommandInteraction, пользователь: disnake.Member, причина: str, доказательство: typing.Optional[str] = None):
    """Сообщает о нарушении правил сервера"""
    # Тут можно добавить логику для проверки прав пользователя, который выполняет команду
    # Создание сообщения о жалобе
    модераторы = ctx.guild.get_role(421378470392627213)
    отчет_msg = f"{модераторы.mention}, пользователь {пользователь.mention} был зарепорчен по причине: {причина}"
    # Добавление доказательств, если они были предоставлены
    if доказательство:
        отчет_msg += f"\nДоказательства: {доказательство}"
    # Получение канала, в который будет отправлено сообщение
    channel = bot.get_channel(922996283034177587)
    # Отправка сообщения в канал жалоб на нарушения
    await channel.send(отчет_msg)
    # Ответ на команду пользователю, который вызвал команду
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
    
Заказать рекламу: https://t.me/Andremuhamed''')   

anecdotes = [
    "Как игроки выигрывают в казино? Заходят с двумя деньгами и выходят с одним.",
    "Как называют игрока, который играет в казино, но не может выиграть? Кредитор.",
    "Почему игроки в интернет-казино всегда пишут 'бесплатный бонус $100', но на самом деле получают только $10? Это их способ подготовить игрока к тому, что ему придется зарабатывать на жизнь как работник этого же казино.",
    "Два игрока подходят к казино. Один говорит: 'Я собираюсь выиграть большую сумму денег и потом уходить'. Другой отвечает: 'Это какой-то план выходного дня?'",
    "Почему игроки в казино называют игровые автоматы 'однорукими бандитами'? Потому что они забирают ваши деньги, а вам приходится смотреть на них, как на настоящих бандитов.",
    "Как говорят, программисты любят три вещи: кофе, клавиатуру и ошибки. Из них только первые две полезны.",
    "Два игрока играют в покер. Первый игрок повышает ставку. Второй игрок говорит: 'Ты знаешь, что я не могу играть на деньги'. Первый игрок отвечает: 'Я знаю, но это мой единственный шанс выиграть'.",
    "Один программист спрашивает другого: 'Почему ты так долго работаешь над этой программой?' - 'Я хочу, чтобы она была готова к завтрашнему дню' - отвечает другой. - 'Но завтра же выходной!' - удивляется первый. - 'Ну и что? Моя программа работает по будням и по выходным!'"
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
            await channel.send('''**Не забудьте подписаться на наш канал нашего сервера:**
Game Room: Игроновинки: https://www.youtube.com/@GameRoom_news/featured

А также присоединяйтесь к нашей группе в ВК: https://vk.com/gameroom_news''')
            message_counter_1 = 0

        if message_counter_2 == message_threshold_2:
            channel = message.channel
            await channel.send('''**Поддержите наш проект донатом:**  
ↈ https://donatello.to/andremuhamad
ↈ https://www.donationalerts.com/r/andremuhamad
''')
            message_counter_2 = 0

    # Отвечаем на приветственное сообщение пользователя в определенном канале
    if message.content.lower().startswith(('привет', 'хай', 'салют', 'привіт', 'всем привет', 'здарова', 'приветствую', 'добрый день', 'доброе утро', 'добрый вечер', 'Рад встрече')):
        response = 'Рады приветствовать вас на нашем сервере! Мы очень рады видеть вас здесь и желаем, чтобы ваше времяпровождение было приятным и полным позитивной атмосферы. Если у вас возникнут вопросы или вам понадобится помощь, пожалуйста, не стесняйтесь обращаться к администраторам или модераторам через команду в боте. Мы также настоятельно просим вас соблюдать правила сервера.'

        channel_id = 420868571422392325  # Замените YOUR_CHANNEL_ID на фактический ID вашего канала
        if isinstance(message.channel, disnake.DMChannel):
            await message.author.send(response)
        elif message.channel.id == channel_id:
            await message.channel.send(response)

    # Отвечаем на сообщения пользователя в личных сообщениях
    if message.author != bot.user and isinstance(message.channel, disnake.DMChannel):
        response = "Благодарю вас за сообщение! На данный момент я не могу общаться, так как занят работой круглосуточно на сервере: https://discord.gg/pGkgzSKDxD"
        await message.author.send(response)

    await bot.process_commands(message)


openai.api_key = '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'  # Підставте свій API ключ OpenAI

@bot.slash_command(description="Генерирует ответ в стиле GPT-3.5")
async def чат(ctx: disnake.ApplicationCommandInteraction, вопрос: str):
    """Генерирует ответ в стиле GPT-3.5"""
    response = generate_chat_response(вопрос)
    await ctx.response.send_message(response)

def generate_chat_response(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Використовуйте текстовий модуль для мови, яку ви хочете
        prompt=user_input,
        max_tokens=50,  # Максимальна кількість токенів відповіді
        temperature=0.7,  # Контролює різноманітність відповідей (чим вище, тим різноманітніше)
        n=1,  # Кількість відповідей, які будуть згенеровані
        stop=None,  # Рядок зупинки, який можна використовувати для зупинки генерації відповіді
    )
  
@bot.slash_command(description="Отправить сообщение в канал")
async def cообщение_канал(ctx: disnake.ApplicationCommandInteraction, канал: disnake.TextChannel, *, сообщение: str):
    """Отправляет сообщение в канал"""
    await канал.send(сообщение, allowed_mentions=disnake.AllowedMentions.none())
    response_msg = f"Сообщение успешно отправлено в канал {канал.mention}"
    await ctx.response.send_message(response_msg, ephemeral=True)

@bot.slash_command(name="интеграцию_канал", description="Отправить интеграцию в канал")
async def uнтеграцию_канал(ctx: disnake.ApplicationCommandInteraction, канал: disnake.TextChannel, цвет: str, ссылка_на_фотографию: str, сообщение: str, верхнее_сообщение: str = "<@&990306177617395713>, у нас, команды Game Room: Игроновинки, имеются значимые обновления, которыми мы хотели бы поделиться"):
    """Отправить интеграцию в канал"""
    # Проверка на правильный формат шестнадцатеричного кода цвета
    if len(цвет) != 7 or not цвет.startswith("#"):
        response_msg = "Неправильный формат цвета. Используйте шестнадцатеричный код цвета в формате #RRGGBB."
        await ctx.response.send_message(response_msg, ephemeral=True)
        return

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
bot.run('FDGGsbnfdndndGSHHjtrjYyNg.GLKaMs.Tph5k40lODeHbavPCWKYrqSkBylAOxoP7-DKbo')
