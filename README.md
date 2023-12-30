# This code is designed for a Discord bot that responds to reactions added or removed from a specific message. Here's what it does:

1. **on_raw_reaction_add**: This function is triggered when a user adds a reaction to a specific message. It checks if the reaction was added to a message with a specific ID and verifies if the reaction corresponds to one of the emojis in the `реакции_и_роли` dictionary. If the conditions are met:
   - It fetches the server and the user.
   - Finds the corresponding role on the server.
   - Assigns that role to the user on the server.
   - Sends a private message to the user about the successful addition of the role.

2. **on_raw_reaction_remove**: This function is triggered when a user removes a reaction from a specific message. It performs the opposite action compared to `on_raw_reaction_add`:
   - Removes the role from the user on the server.
   - Sends a private message to the user about the successful removal of the role.

These functions are useful for automating the process of assigning or removing roles to users on a Discord server based on reactions to a specific message.

![image](https://github.com/AndreMuhamed/Game_Room/assets/128980327/ead9b139-eeda-4b2d-a541-f6dc49bcc08d)


# I am not responsible for the functionality of the bot.
