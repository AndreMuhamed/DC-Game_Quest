import discord
import asyncio
from telethon import TelegramClient, events
from telethon.tl import types as telethon_types
import os

api_id = "АЙПИ телеграм"
api_hash = "КЕШ телеграм"
telegram_token = "ТОКЕН телеграм"
discord_token = "ТОКЕН бота"

telegram_channel_id = -1002010217021
discord_channel_id = 1195884297668792360

telegram_client = TelegramClient("telegram_session", api_id, api_hash)
discord_client = discord.Client(intents=discord.Intents.default())

async def handle_telegram_message(event):
    if event.text:
        await send_discord_message(discord_channel_id, text=event.text)
    
    if event.media:
        if isinstance(event.media, list):
            for i, media in enumerate(event.media, 1):
                await process_media(i, media)
        else:
            await process_media(1, event.media)

async def process_media(index, media):
    if isinstance(media, telethon_types.Photo):
        await process_photo(index, media)
    elif isinstance(media, telethon_types.Document):
        await process_document(index, media)
    elif isinstance(media, telethon_types.MessageMediaPhoto):
        await process_message_media_photo(index, media)
    elif isinstance(media, telethon_types.MessageMediaDocument):
        await process_message_media_document(index, media)

async def process_photo(index, photo):
    photo_file = await telegram_client.download_media(photo)
    await send_discord_message(discord_channel_id, file_path=photo_file)

async def process_document(index, document):
    document_file = await telegram_client.download_media(document)
    if 'video' in document.mime_type.lower():
        await process_video(index, document_file)
    else:
        await send_discord_message(discord_channel_id, file_path=document_file)

async def process_video(index, video_file):
    await send_discord_message(discord_channel_id, file_path=video_file)

async def process_message_media_photo(index, message_media_photo):
    photo = message_media_photo.photo
    await process_photo(index, photo)

async def process_message_media_document(index, message_media_document):
    document = message_media_document.document
    await process_document(index, document)

@discord_client.event
async def on_ready():
    print(f"Discord-клиент готов. Бот: {discord_client.user}")

    try:
        me = await telegram_client.get_me()
        print(f"Telegram-клиент готов. Пользователь: {me.id} ({me.username})")
    except Exception as e:
        print(f"Ошибка при получении информации о Telegram-пользователе: {e}")

async def send_discord_message(channel_id, text=None, file_path=None):
    channel = discord_client.get_channel(channel_id)

    if text:
        await channel.send(text)

    if file_path:
        file = discord.File(file_path)
        await channel.send(file=file)
        await delete_file(file_path)

async def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файл успешно удален: {file_path}")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

async def run_clients():
    try:
        await telegram_client.start(bot_token=telegram_token)
        await discord_client.start(discord_token)
        await telegram_client.run_until_disconnected()
    except Exception as e:
        print(f"Произошла ошибка при запуске клиентов: {e}")
    finally:
        await discord_client.close()

if __name__ == "__main__":
    telegram_client.add_event_handler(handle_telegram_message, events.NewMessage(chats=telegram_channel_id))
    asyncio.run(run_clients())
