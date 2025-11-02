import os
import asyncio
from telethon import TelegramClient, events

# 🔧 ВСТАВЬ СВОИ ДАННЫЕ СЮДА:
api_id = int("23682855")  # пример: 23682855
api_hash = "ee64f83e641de11b5ff496694fcc13e4"   # пример: ee64f83e641de11b5ff496694fcc13e4
bot_token = "8566820879:AAG2lim7a1rmq0RcYyjFXLV14uAOseHwxIU"  # пример: 123456789:ABCdefGhijkLmnoPQRstuVWxyz

# 📢 Канал, откуда брать посты
source_channel = "https://t.me/grow_a_garden_stock_info"

# 🎯 Канал, куда публиковать
target_channel = "@brbrbrbra11"

# Инициализация клиента
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Функция очистки текста
def clean_text(text):
    if not text:
        return text
    lower = text.lower()
    marker = "группа со стоками"
    if marker in lower:
        idx = lower.index(marker)
        return text[:idx].strip()
    return text.strip()

# Обработка новых сообщений
@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = ""
    if event.message.message:
        text = event.message.message
    elif event.message.caption:
        text = event.message.caption

    text = clean_text(text)

    try:
        if event.message.media:
            await client.send_file(target_channel, event.message.media, caption=text or None)
        else:
            await client.send_message(target_channel, text or " ")
    except Exception as e:
        print("Ошибка при отправке:", e)

# Запуск
async def main():
    print("✅ Бот запущен и слушает канал:", source_channel)
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
