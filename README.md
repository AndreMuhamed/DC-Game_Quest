<h1 align="center">
🎯 An amazing bot from the Game Quest 🎯
</h1>

---

![image](https://github.com/AndreMuhamed/Game_Quest/assets/128980327/3ca9c1f9-0da9-4315-877e-28f1a450169f)


---

# <a id="menu"></a>🦾 » Menu
- [🎮・Discord](https://discord.gg/nQGvVAEw5r)
- [🛠・Features](#features)
- [🎉・Setting up](#setup)
- [🕵️・Responsibility](#responsibility)

---

# <a id="features"></a>🛠 » Features

## basis.py
This code snippet utilizes the `threading` and `subprocess` modules to concurrently execute multiple Python scripts in separate threads.

1. It defines a function `run_file(file_name)` that launches the specified Python file using `subprocess.Popen(['python', file_name])`. It then prints a message indicating that the file has been launched.

2. It creates a list of files `files` to be executed.

3. For each file in the `files` list, it creates a new thread where the `run_file` function is called with the corresponding file name as an argument.

4. The launched threads are appended to the `threads` list.

5. The main program continues execution without waiting for the threads to complete and prints a message indicating that the Discord bot and other files have been launched.

# file3.py
This Python script is a Discord bot programmed using the `discord.py` library. Here's a breakdown of what it does:

1. It imports necessary modules including `discord`, `commands` from `discord.ext`, `os`, `random`, and `asyncio`.

2. It defines intents for the bot to specify what events the bot should receive information about.

3. It sets up the bot using the defined intents and assigns it a command prefix `'!'`.

4. It defines an event handler `on_ready()` that executes when the bot is ready. In this handler:
   - It prints a message indicating that the bot is ready.
   - It retrieves the channel with the specified `CHANNEL_ID`.
   - It connects to the voice channel.
   - It sets the bot's presence activity.
   - It plays random music files from the specified `MUSIC_FOLDER_PATH` continuously.

5. It defines another event handler `on_message()` that executes when a message is sent. In this handler:
   - It processes commands.
   - It deletes messages that start with the command prefix `'!'`.

6. It defines several commands using the `@bot.command()` decorator. These commands include:
   - `иван`
   - `gamequest_news`
   - `украина`
   - `tedro`
   - `джокер`
   - `hezuko`
   - `эдвард`
   - `команда`
   - `сахарок`

7. It runs the bot using the specified `TOKEN`.

Overall, this script creates a Discord bot capable of playing music in a voice channel, responding to commands, and deleting messages that start with the specified command prefix. Additionally, it defines commands that provide information or perform specific actions when invoked by users in the Discord server.

---

# <a id="responsibility"></a>🕵️ » Responsibility
The developers of this Discord bot code strive to create a product that operates as stably and reliably as possible. However, it should be noted that full functionality and reliability cannot be guaranteed due to the complexity of interactions with various components and services, as well as the influence of user settings and environments. Users should be prepared for possible failures and changes, so it makes sense to have alternative plans in place to ensure the uninterrupted operation of their projects.

<h1 align="center">
And remember, developers are not responsible for the performance of this Discord bot code
</h1>

---

