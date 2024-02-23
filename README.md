<h1 align="center">
🎯 An amazing bot from the Game Quest 🎯
</h1>

---

![image](https://github.com/AndreMuhamed/Game_Quest/assets/128980327/3ca9c1f9-0da9-4315-877e-28f1a450169f)


---

## <a id="menu"></a>🦾 » Menu
- [🎮・Discord](https://discord.gg/nQGvVAEw5r)
- [🛠・Features](#features)
- [🎉・Setting up](#setup)
- [🕵️・Responsibility](#responsibility)

## <a id="features"></a>🛠 » Features

### basis.py
This code snippet utilizes the `threading` and `subprocess` modules to concurrently execute multiple Python scripts in separate threads.

1. It defines a function `run_file(file_name)` that launches the specified Python file using `subprocess.Popen(['python', file_name])`. It then prints a message indicating that the file has been launched.

2. It creates a list of files `files` to be executed.

3. For each file in the `files` list, it creates a new thread where the `run_file` function is called with the corresponding file name as an argument.

4. The launched threads are appended to the `threads` list.

5. The main program continues execution without waiting for the threads to complete and prints a message indicating that the Discord bot and other files have been launched.

### file1.py

## <a id="responsibility"></a>🕵️ » Responsibility
The developers of this Discord bot code strive to create a product that operates as stably and reliably as possible. However, it should be noted that full functionality and reliability cannot be guaranteed due to the complexity of interactions with various components and services, as well as the influence of user settings and environments. Users should be prepared for possible failures and changes, so it makes sense to have alternative plans in place to ensure the uninterrupted operation of their projects.

<h1 align="center">
And remember, developers are not responsible for the performance of this Discord bot code
</h1>

---

