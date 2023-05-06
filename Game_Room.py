from keep_alive import keep_alive
import disnake
import typing
import discord
import random
import requests

bot = disnake.Client()

from discord.ext import commands
from disnake.ext import commands

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

@bot.slash_command(description="Спросить вопрос про сервер")
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
    response = requests.get('https://example.com/api/cat')
    data = response.json()
    await context.response.send_message(data['image_url'])

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

А также присоединяйтесь к нашей группе в ВК: https://vk.com/gameroom_new''')
            message_counter_1 = 0

        if message_counter_2 == message_threshold_2:
            channel = message.channel
            await channel.send('''**Поддержите наш проект донатом:**  
ↈ https://donatello.to/andremuhamad
ↈ https://www.donationalerts.com/r/andremuhamad
''')
            message_counter_2 = 0

        # Отвечаем на приветственное сообщение пользователя
        if message.content.lower() == 'привет':
            response = 'Привет, я бот! Не нарушайте правила сервера.'
            if isinstance(message.channel, disnake.DMChannel):
                await message.author.send(response)
            else:
                await message.channel.send(response)

    # Отвечаем на сообщения пользователя в личных сообщениях
    if message.author != bot.user and isinstance(message.channel, disnake.DMChannel):
        response = "Благодарю вас за сообщение! На данный момент я не могу общаться, так как занят работой круглосуточно на сервере: https://discord.gg/pGkgzSKDxD"
        await message.author.send(response)

    await bot.process_commands(message)

keep_alive()
bot.run('MTEdggsjE0ODEdggyMDYyNg.GLKaMs.Tphfdgfdfвп40lODeHbavPCWdfgdfgylAOxoP7-DKbo')
