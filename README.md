# An amazing bot from Andrey Muhammed's team for the Discord server:

^_^ Game Room(https://discord.com/invite/pGkgzSKDxD) ^_^


![Untitled-1](https://github.com/AndreMuhamed/Game_Room/assets/128980327/edbb8560-4abd-44bf-a18c-ea55cc86f7ee)


The code you're looking at contains 20 Discord bot commands, each of which describes a specific action. Let's look at each of them:

1. Command `/отчёт`:
    - Description: Reports a violation of server rules.
    - Command arguments:
      - `ctx`: Object of command interaction (application command interaction) from the `disnake` library.
      - `user': Mention of the user associated with the violation (`disnake.Member' type object).
      - `reason`: The reason for the violation (term).
      - `proof` (optional): Proof of violation (time limit).
    - Actions of the team:
      - Creates a complaint message containing information about the user, violation and evidence (if provided).
      - Sends a message to the specified channel for complaining about violations.
      - Sends a reply message to the author of the command about the successful sending of the violation message to the moderators.

2. The `/join` command:
    - Description: Sends a request to join the team.
    - Command arguments:
      - `ctx`: Object of command interaction (application command interaction) from the `disnake` library.
      - `kem`: The role the user wants to join (string).
      - `age`: Age of the user (integer).
    - Actions of the team:
      - Creates a message with information about the request for the user to join the team, including the specified role and age.
      - Sends a message to the specified channel of requests to join the team.
      - Sends a reply message to the author of the command about the successful sending of the connection request.

3. Variable `QUESTION_CHANNEL_ID`:
    - Value: `922996283034177587`.
    - Description: ID of the channel in which questions will be sent.

4. `/help` command:
    - Description: Asks a question about the server.
    - Command arguments:
      - `ctx`: Object of command interaction (application command interaction) from the `disnake` library.
      - `question`: Question about the server (string).
    - Actions of the team:
      - Gets the channel object using the ID `QUESTION_CHANNEL_ID`.
      - Sends a question to the specified channel on behalf of the team author.
      - Sends a reply message to the author of the command about the successful submission of the question.

5. `/pupupu` command:
    - Description: Sends an advertising message.
    - Command arguments:
      - `interaction`: Application command interaction object from `disnake` library.
    - Actions of the team:
      - Sends an advertising message in response to the command. Contains text and a link to order advertising.

6. Variable `anecdotes`:
    - Meaning: List of sentences representing jokes.
    - Description: Contains several anecdotes.

7. `/joke` command:
    - Description: Sends a random joke.
    - Command arguments:
      - `ctx`: Object of command interaction (application command interaction) from the `disnake` library.
    - Actions of the team:
      - Selects a random anecdote from the `anecdotes' list.
      - Sends the selected joke in response to the command.

8. Function `on_ready()`:
    - Description: This event is triggered when the bot is successfully connected and ready for use.
    - Actions of the function: When called, the function simply outputs a message to the console with information about which user the bot logged into the system.

9. `/photo` command:
    - Description: Sends a random image of a cat.
    - Command arguments:
      - `context`: Object of command interaction (application command interaction) from the `disnake` library.
    - Actions of the team:
      - Makes a GET request to "The Cat API" to get a random cat image.
      - Gets the URL of the image from the received data.
      - Sends an image URL in response to a command.

10. Variable `PLASH_API_KEY`:
     - Meaning: `"JU_FnZ9tmvKZ4xLX2POVUdg0GpU3uGc8lW-1GLp9EbE"`.
     - Description: API key for accessing the Unsplash service.

11. `/pc` command:
     - Description: Sends a random image associated with the computer.
     - Command arguments:
       - `context`: Object of command interaction (application command interaction) from the `disnake` library.
     - Actions of the team:
       - Makes a GET request to the Unsplash API using `PLASH_API_KEY` to retrieve a random image associated with the request "computer".
       - Gets the URL of the image from the received data.
       - Sends an image URL in response to a command.

12. Variables `message_threshold_1`, `message_counter_1`, `message_threshold_2`, `message_counter_2`:
    - Description:
      - `message_threshold_1` and `message_threshold_2` - values of the threshold number of messages, after which a certain message will be sent.
      - `message_counter_1` and `message_counter_2` are variables for tracking the number of messages that have already been sent.
    - Usage:
      -`message_counter_1` and `message_counter_2` increase by 1 with each message, not from the bot or in personal messages.
      - When `message_counter_1` reaches `message_threshold_1`, a message with text and links to the channel and server group is sent.
      - When `message_counter_2` reaches `message_threshold_2`, a message with text and links to project donations is sent.
      - After sending messages, `message_counter_1` and `message_counter_2` are reset to 0.

13. Dictionary `users`:
    - Description: This is a dictionary for storing user information. In the provided code, the dictionary is not used and remains empty.

14. Function `on_message(message)`:
    - Description: This event is triggered when each message is received in any channel on which the bot is located.
    - Function arguments:
      - `message': A message object from the `disnake' library containing information about the message.
    - Actions of the function:
      - Checks that the message was not sent by a bot and is not in personal messages.
      - Increases `message_counter_1` and `message_counter_2` by 1.
      - If `message_counter_1` reaches `message_threshold_1`, send a message with text and links to the channel and server group.
      - If `message_counter_2` reaches `message_threshold_2`, send a message with text and links to project donations.
      - Responds to greeting messages from users in a certain channel.
      - Responds to user messages in personal messages.
      - Calls `bot.process_commands(message)` to process commands from the message.

15. Variable `openai.api_key`:
    - Description: This is the OpenAI API key, which is used to execute requests to the GPT-3.5 model.
    - Usage: Paste your own OpenAI API key instead of `'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''.

16. Function `chat(ctx: disnake.ApplicationCommandInteraction, vopros: str)`:
    - Description: This is a slash command that generates an answer in the GPT-3.5 style based on the entered question.
    - Function arguments:
      - `ctx`: Object of interaction with the command (interaction) from the `disnake` library, containing information about the command.
      - `question`: A string containing a question, on the basis of which the answer will be generated.
    - Actions of the function:
      - Calls the function `generate_chat_response(question)` to generate a response.
      - Sends the generated response to the chat.

17. Function `generate_chat_response(user_input)`:
    - Description: This is a function that uses the GPT-3.5 model to generate an answer based on a question entered by the user.
    - Function arguments:
      - `user_input`: A string containing the user's question.
    - Actions of the function:
      - Uses the OpenAI API key and calls the `openai.Completion.create()` method to create a request to the GPT-3.5 model.
      - Sets request parameters, such as engine (`engine`), input text (`prompt`), maximum number of tokens (`max_tokens`), temperature (`temperature`), number of generated responses (`n`), and stop period (`stop`).
      - Returns a generated response.

18. Function `communication_channel(ctx: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel, *, message: str)`:
    - Description: This is a slash command that sends a message to the specified channel.
    - Function arguments:
      - `ctx`: Object of interaction with the command (interaction) from the `disnake` library, containing information about the command.
      - `channel`: Text channel object (`disnake.TextChannel`) to which the message will be sent.
      - `message`: A string containing the text of the message.
    - Actions of the function:
      - Using the ``channel.send()`` method, sends a message to the specified channel.
      - Sends a reply message with confirmation of successful sending.

19. Function `untegratsiyu_kanal(ctx: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel, color: str, link_to_photo: str, message: str, upper_message: str = "<@&990306177617395713>, we have Game Room teams: Game news, available significant updates we'd like to share")`:
    - Description: This is a slash command that sends a message with integration (a message with a photo and description) to the specified channel.
    - Function arguments:
      - `ctx`: Object of interaction with the command (interaction) from the `disnake` library, containing information about the command.
      - `channel`: A text channel object (`disnake.TextChannel`) to which the integrated message will be sent.
      - `color`: A string representing the hexadecimal color code in #RRGGBB format.
      - `link_to_photo`: A string containing the URL of the photo that will be included in the integration.
      - `message`: A string containing a description of the message in the integration.
      - `верхнее_сообщение`: (Optional argument) A string containing the top message in the integration (by default "<@&990306177617395713>, we, the Game Room: Game News team, have significant updates that we would like to share").
    - Actions fuactions:
      - Checks the correctness of the hexadecimal color code format.
      - Creates a `disnake.Embed' object with the specified color and message description.
      - Sets the image (`url`) in the `embed` object.
      - Using the ``kanal.send()`` method, sends a message with integration (with the specified top message and attachment) to the specified channel.
      - Sends a reply message with confirmation of successful sending.

# I am not responsible for the functionality of the bot.пцупуцпцупЦПЦУ
