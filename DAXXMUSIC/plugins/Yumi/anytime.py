from pyrogram import Client, filters
from pyrogram.types import Message
import logging
from DAXXMUSIC import app 

class ActiveMembersDetector:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dp = self.updater.dispatcher

        self.dp.add_handler(CommandHandler('start', self.start))
        self.dp.add_handler(CommandHandler('active', self.detect_active_members))

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I\'m active member detector bot.')

    def detect_active_members(self, update, context):
        chat_id = update.effective_chat.id
        members = context.bot.get_chat_members_count(chat_id)
        active_members = 0

        for member in context.bot.get_chat_members(chat_id):
            if member.status in ['creator', 'administrator', 'member']:
                active_members += 1

        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Active members: {active_members}/{members}')

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

def create_active_members_detector(token):
    return ActiveMembersDetector(token)
