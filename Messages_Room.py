import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Бот готов!")

@bot.command(name='халява')
async def send_combined_embed(ctx):
    embed_data = [
        "[RACE 07: Andy Priaulx Crowne Plaza Raceway](https://store.steampowered.com/app/8650/RACE_07_Andy_Priaulx_Crowne_Plaza_Raceway_Free_DLC/)",
        "[The Descendant](https://store.steampowered.com/app/351940/The_Descendant/)",
        "[The Archotek Project](https://store.steampowered.com/app/608990/The_Archotek_Project/)",
        "[AX:EL - Air XenoDawn](https://store.steampowered.com/app/319830/AXEL__Air_XenoDawn/)",
        "[The Awesome Adventures of Captain Spirit](https://store.steampowered.com/app/845070/The_Awesome_Adventures_of_Captain_Spirit/)",
        "[Defiance 2050 - Beta](https://store.steampowered.com/app/825430/Defiance_2050__Beta/)",
        "[Serena](https://store.steampowered.com/app/272060/Serena/)",
        "[POSTAL](https://store.steampowered.com/app/232770/POSTAL/)",
        "[LIFE IS STRANGE 2 - EPISODE 1](https://store.steampowered.com/app/532210/Life_is_Strange_2/)",
        "[Capcom Arcade Stadium](https://store.steampowered.com/app/1515950/Capcom_Arcade_Stadium/)",
        "[Artifact Foundry](https://store.steampowered.com/app/1269260/Artifact_Foundry/)",
        "[Penumbra: Necrologue](https://store.steampowered.com/app/346290/Penumbra_Necrologue/)",
        "[Romance of the Three Kingdoms Maker](https://store.steampowered.com/app/397720/Romance_of_the_Three_Kingdoms_Maker/)",
        "[Capcom Arcade 2nd Stadium](https://store.steampowered.com/app/1755910/Capcom_Arcade_2nd_Stadium/)",
        "[Odysseus Kosmos and his Robot Quest: Episode 1](https://store.steampowered.com/app/769920/Odysseus_Kosmos_and_his_Robot_Quest_Episode_1/)"
    ]

    description = "\n".join(embed_data)
    description += "\n\n**Остальные игры, можно забрать через расширение [SteamDB](https://chromewebstore.google.com/detail/steamdb/kdbmhfkmnlmbkgbabkdealhhbfhlmmon), нажав на кнопку \"Add free license\".**"

    additional_games = [
        "[Tom Clancy's Ghost Recon Wildlands Open Beta](https://steamdb.info/sub/150442/info/)",
        "[Paladins - Public Test](https://steamdb.info/sub/157010/info/)",
        "[The Archotek Project (Demo)](https://steamdb.info/sub/222994/info/)",
        "[Defiance 2050 - Beta](https://steamdb.info/sub/253461/apps/)",
        "[Huawei VR2 Driver](https://steamdb.info/sub/292303/apps/)",
        "[SOS: Test Server](https://steamdb.info/sub/299795/apps/)"
    ]

    additional_description = "\n".join(additional_games)
    description += f"\n\n{additional_description}"

    embed = discord.Embed(
        title='БЕСПЛАТНЫЕ ИГРЫ В STEAM',
        description=description,
        color=8192044,
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/990304018188369980/1149433881448165508/Picsart_22-06-18_20-38-42-648_copy.png?ex=65a048b8&is=658dd3b8&hm=0b30538b18cd7c5d375377dc6e172be39f6354b64cec22d23c2da4218d895e08&')
    embed.set_footer(text="Дают +1 к значку коллекционера. Подпишись на социальные сети!!!")


    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
