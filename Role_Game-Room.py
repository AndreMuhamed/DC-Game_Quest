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

@bot.command(name='роль')
async def роль(ctx):
    # Данные для встроенного сообщения (embed)
    embed_data = {
        "description": "Выбирая эмодзи, вы не только определяете небольшую иконку, но и выбираете свою основную игру, "
                       "в которую обычно играете. Выбирая эмодзи, вы назначаете себе роль в мире игры:\n\n"
                       "⬜ **\"GTA V\"** - выбор элегантности и экшена.\n"
                       "🟨 **\"Dota 2\"** - преданность стратегии и принятию вызовов.\n"
                       "🟧 **\"CS:GO 2\"** - участие в конкурентной борьбе и в команде.\n"
                       "🟥 **\"Rust\"** - переживания в условиях выживания и адреналин.\n"
                       "🟩 **\"Minecraft\"** - выражение творчества и ощущение свободы.\n"
                       "🟫 **\"Call of Duty\"** - скорость и участие в войне.\n"
                       "🟦 **\"Battlefield\"** - стратегическая война на большой зоне.\n"
                       "🟪 **\"Другие игры\"** - ваш уникальный мир в игре.",
        "color": 0xC80147,  # Здесь новый цвет (C80147)
        "author": {
            "name": "ДОБРО ПОЖАЛОВАТЬ В НАШИ РОЛЕВЫЕ ВЫДАЧИ",
            "icon_url": "https://cdn.discordapp.com/attachments/1195867893594869857/1211392939327094854/icon-game.png"
        },
        "image": {
            "url": "https://cdn.discordapp.com/attachments/1195867893594869857/1204876749624844328/a87567b8a682e9df.png"
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
bot.run("ТВОЙ ТОКЕН БОТА")

