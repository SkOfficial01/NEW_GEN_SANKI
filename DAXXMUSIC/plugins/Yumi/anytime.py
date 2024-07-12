import datetime
from DAXXMUSIC import app

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

def send_good_morning(context):
    context.bot.send_message(context.job.context, text='Good morning! ☀️')

def send_good_afternoon(context):
    context.bot.send_message(context.job.context, text='Good afternoon! 🌤️')

def send_good_night(context):
    context.bot.send_message(context.job.context, text='Good night! 🌙')

def set_up_timed_messages():
    updater = Updater(token=TOKEN, use_context=True)
    job_queue = updater.job_queue

    # Time for morning message (adjust as needed)
    morning_time = datetime.time(hour=7, minute=0, second=0)

    # Time for afternoon message (adjust as needed)
    afternoon_time = datetime.time(hour=13, minute=0, second=0)

    # Time for night message (adjust as needed)
    night_time = datetime.time(hour=21, minute=0, second=0)

    # Schedule messages
    job_queue.run_daily(send_good_morning, morning_time, context=updater.bot)
    job_queue.run_daily(send_good_afternoon, afternoon_time, context=updater.bot)
    job_queue.run_daily(send_good_night, night_time, context=updater.bot)

    updater.start_polling()
    updater.idle()
