import time
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = "8381590872:AAHLt_qgvo6QpUcrsrD4RXGbeUipgSG5JWQ"
CHANNEL_USERNAME = "@kawaiitube"  # Replace with your actual channel username

videos = [
    {
        "title": "🌸 Hindi Dubbed Anime – Episode 1",
        "desc": "Watch now on ToonStream 💖",
        "thumb": "https://i.imgur.com/8TUazAq.jpg",
        "link": "https://toonstream.love/?trembed=0&trid=36321&trtype=2"
    },
    {
        "title": "🔥 Epic New Anime Drop – Episode 2",
        "desc": "Stream latest anime in Hindi now ✨",
        "thumb": "https://i.imgur.com/8TUazAq.jpg",
        "link": "https://toonstream.love/?trembed=0&trid=36561&trtype=2"
    }
]

bot = Bot(token=BOT_TOKEN)

while True:
    for video in videos:
        try:
            caption = f"*{video['title']}*\n{video['desc']}\n[▶️ Watch Here]({video['link']})"

{video['desc']}
[▶️ Watch Here]({video['link']})"
            bot.send_photo(
                chat_id=CHANNEL_USERNAME,
                photo=video['thumb'],
                caption=caption,
                parse_mode="Markdown"
            )
            print(f"✅ Posted: {video['title']}")
        except TelegramError as e:
            print("❌ Error posting video:", e)
        time.sleep(600)  # Wait 10 minutes before posting next
