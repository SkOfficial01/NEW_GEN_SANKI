from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from DAXXMUSIC import app
# Initialize your Pyrogram Client
app = Client("my_bot")

# Define the support chat link
SUPPORT_CHAT = "https://t.me/IndianLunaChatters"

# Define the button for inline keyboard
BUTTON = [[InlineKeyboardButton("Support", url=SUPPORT_CHAT)]]

# Function to handle /slap command
@app.on_message(filters.command("slap"))
async def slap(_, message):
    if not message.reply_to_message:
        await message.reply("Reply to someone to slap them!")
        return
    
    # Get the user info
    slapped_user = message.reply_to_message.from_user
    
    # Generate a random percentage for the slap
    slap_percent = random.randint(1, 100)
    
    # Construct the message without Markdown
    slap_message = f"💥 Slap! {slapped_user.first_name} got slapped by {message.from_user.first_name}!"
    slap_message += f"\n\nDamage: {slap_percent}%"
    
    # Send the message with the slap result
    await app.send_message(
        chat_id=message.chat.id,
        text=slap_message,
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )

# Help command text
help_text = """
Welcome to the slap game! Use the following commands:

• /slap : Reply to someone to slap them and see the damage percentage!

🔗 Support: [Join our chat](https://t.me/IndianLunaChatters)
"""

# Function to handle /start command
@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply(help_text, disable_web_page_preview=True)
