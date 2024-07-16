import datetime
import time
from DAXXMUSIC import app

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7473830088:AAFUvpAti-vlZMG7ADwK8toY199W1OZh4cc'

# Replace with your group chat IDs where you want to send messages
GROUP_CHAT_IDS = [
    -1002121827877,  # Example group chat ID
    -1002121827877   # Another example group chat ID
]

def send_message_to_groups(message):
    bot = Bot(token=TOKEN)

    for chat_id in GROUP_CHAT_IDS:
        bot.send_message(chat_id=chat_id, text=message)

def send_good_morning():
    send_message_to_groups('Good morning! ☀️')

def send_good_afternoon():
    send_message_to_groups('Good afternoon! 🌤️')

def send_good_night():
    send_message_to_groups('Good night! 🌙')

def set_up_timed_messages():
    while True:
        current_time = datetime.datetime.now().time()

        # Time for morning message (adjust as needed)
        morning_time = datetime.time(hour=7, minute=0, second=0)

        # Time for afternoon message (adjust as needed)
        afternoon_time = datetime.time(hour=14, minute=20, second=0)

        # Time for night message (adjust as needed)
        night_time = datetime.time(hour=24, minute=25, second=0)

        # Check current time and send appropriate message
        if current_time >= morning_time and current_time < datetime.time(hour=7, minute=1, second=0):
            send_good_morning()
            time.sleep(60)  # Sleep for 1 minute to avoid multiple sends

        elif current_time >= afternoon_time and current_time < datetime.time(hour=14, minute=21, second=0):
            send_good_afternoon()
            time.sleep(60)  # Sleep for 1 minute to avoid multiple sends

        elif current_time >= night_time and current_time < datetime.time(hour=24, minute=25, second=0):
            send_good_night()
            time.sleep(60)  # Sleep for 1 minute to avoid multiple sends

        # Check every minute
        time.sleep(60)
