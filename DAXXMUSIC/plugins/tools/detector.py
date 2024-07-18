import logging
from DAXXMUSIC import app

class ActiveMembersDetector:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dp = self.updater.dispatcher

        self.dp.add_handler(CommandHandler('start', self.start))
        self.dp.add_handler(CommandHandler('active', self.detect_active_members))
        self.dp.add_handler(CommandHandler('detect', self.detect_command))

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

    def detect_command(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Running active members detection...')
        self.detect_active_members(update, context)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

def main():
    token = '7473830088:AAFUvpAti-vlZMG7ADwK8toY199W1OZh4cc'
    detector = ActiveMembersDetector(token)
    detector.run()
