import discord
from discord.ext import commands

# Создаем объект intents
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

# Создаем объект бота с указанием префикса команд и передачей intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Событие при готовности бота
@bot.event
async def on_ready():
    print("Бот готов!")

# Команда !роль
@bot.command(name='роль')
async def роль(ctx):
    # Данные для встроенного сообщения (embed)
    embed_data = {
        "description": "Выбирая эмодзи, вы не только определяете небольшую иконку, но и выбираете свою основную игру, "
                       "в которую обычно играете. Выбирая эмодзи, вы назначаете себе роль в мире игры:\n\n"
                       "⬜ \"GTA V\" - выбор элегантности и экшена.\n"
                       "🟨 \"Dota 2\" - преданность стратегии и принятию вызовов.\n"
                       "🟧 \"CS:GO\" - участие в конкурентной борьбе и командной игре.\n"
                       "🟥 \"Rust\" - переживания в условиях выживания и адреналин.\n"
                       "🟩 \"Minecraft\" - выражение творчества и ощущение свободы.\n"
                       "🟫 \"Call of Duty\" - скорость и участие в войне.\n"
                       "🟦 \"Battlefield\" - стратегическая война на большой территории.\n"
                       "🟪 \"Другие игры\" - ваш уникальный мир в игре.",
        "color": 8192044,
        "author": {
            "name": "ВЫДАЧА РОЛИ НА СЕРВЕРИ",
            "icon_url": "https://cdn.discordapp.com/attachments/990304018188369980/1146016243149701180/icon-partner.png?ex=655c7acc&is=654a05cc&hm=98a901d8e07d1aaa5e897f309279175c3d871917191190ef5ff8454f86f2c106&"
        },
        "image": {
            "url": "https://cdn.discordapp.com/attachments/990304018188369980/1172988143566332005/Untitled-1.jpg?ex=65625156&is=654fdc56&hm=00b2b745e4d30aab48dbbe0e10b9d2272eba6ef9344a88453cc1d7d85e64085c&"
        }
    }

    # Создаем объект встроенного сообщения из данных
    embed = discord.Embed.from_dict(embed_data)
    
    # Отправляем встроенное сообщение
    сообщение = await ctx.send(embed=embed)

    # Эмодзи для реакций
    emojis = ['⬜', '🟨', '🟧', '🟥', '🟩', '🟫', '🟦', '🟪']
    
    # Добавляем реакции к сообщению
    for emoji in emojis:
        await сообщение.add_reaction(emoji)

# Запускаем бота с указанием токена
bot.run("ybbnj7UPZKsh4")

