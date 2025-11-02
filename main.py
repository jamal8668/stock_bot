import asyncio
from telethon import TelegramClient, events
import os
import nest_asyncio

# Применяем фикс для Render
nest_asyncio.apply()

# === НАСТРОЙКИ ===
api_id = 23682855
api_hash = "ee64f83e641de11b5ff496694fcc13e4"
bot_token = "8566820879:AAG2lim7a1rmq0RcYyjFXLV14uAOseHwxIU"

# Каналы
source_channel = "https://t.me/grow_a_garden_stock_info"
target_channel = "https://t.me/brbrbrbra11"

# === КЛИЕНТ ===
client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

print(f"✅ Бот запущен и слушает канал: {source_channel}")

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.raw_text

    # Если хочешь — здесь можно изменить текст поста перед пересылкой
    # Например:
    if "группа со стоками" in text:
        text = text.split("группа со стоками")[0].strip()

    try:
        await client.send_message(target_channel, text)
        print("📨 Сообщение переслано!")
    except Exception as e:
        print("⚠️ Ошибка при отправке:", e)

async def main():
    await client.run_until_disconnected()

# === ЗАПУСК ===
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
