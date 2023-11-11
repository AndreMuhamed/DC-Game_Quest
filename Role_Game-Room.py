import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='роль', help='Отправляет сообщение для выбора роли.')
async def выбор_роли(ctx):
    описание = (
        "Выбирая эмодзи, вы не только определяете небольшую иконку, но и выбираете свою основную игру, "
        "в которую обычно играете. Выбирая эмодзи, вы назначаете себе роль в мире игры:\n\n"
        "⬜ \"GTA V\" - выбор элегантности и экшена.\n"
        "🟨 \"Dota 2\" - преданность стратегии и принятию вызовов.\n"
        "🟧 \"CS:GO\" - участие в конкурентной борьбе и командной игре.\n"
        "🟥 \"Rust\" - переживания в условиях выживания и адреналин.\n"
        "🟩 \"Minecraft\" - выражение творчества и ощущение свободы.\n"
        "🟫 \"Call of Duty\" - скорость и участие в войне.\n"
        "🟦 \"Battlefield\" - стратегическая война на большой территории.\n"
        "🟪 \"Другие игры\" - ваш уникальный мир в игре."
    )

    embed = discord.Embed(
        description=описание,
        color=8192044,
        author={"name": "ВЫДАЧА РОЛЕЙ НА СЕРВЕРЕ", "icon_url": "https://cdn.discordapp.com/attachments/990304018188369980/1146016243149701180/icon-partner.png?ex=655c7acc&is=654a05cc&hm=98a901d8e07d1aaa5e897f309279175c3d871917191190ef5ff8454f86f2c106&"},
        image={"url": "https://cdn.discordapp.com/attachments/990304018188369980/1172988143566332005/Untitled-1.jpg?ex=65625156&is=654fdc56&hm=00b2b745e4d30aab48dbbe0e10b9d2272eba6ef9344a88453cc1d7d85e64085c&"}
    )

    сообщение = await ctx.send(embed=embed)

    # Добавляем реакции к сообщению
    emojis = ['⬜', '🟨', '🟧', '🟥', '🟩', '🟫', '🟦', '🟪']
    for emoji in emojis:
        await сообщение.add_reaction(emoji)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Ваш токен бота
token = 'YOUR_BOT_TOKEN'
bot.run(token)

