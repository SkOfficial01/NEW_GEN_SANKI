import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","24740695"))
API_HASH = getenv("API_HASH","a95990848f2b93b8131a4a7491d97092")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7005088837:AAGb6L60_BmGef5vmDWxd7ZH9PirHJA60Z0")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_SANKI_XD")
#Add HANDLER username Without @
HANDLER_USERNAME = getenv("HANDLER_USERNAME","Aadi29104")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "SANKI_MUSIC_XD_BOT")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "SANKI XD")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "II_SANKI_ll")
EVALOP = list(map(int, getenv("EVALOP", "6971100005").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")
# for fedban 
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002100433415"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6971100005))

# Get this value from on telegram by /id
HANDLER_ID = int(getenv("HANDLER_ID","6190297573"))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/skofficial001/New_sanki",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ToXiC_BoY_OFFICIAL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ToXiC_BoY_OFFICIAL")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION1","BQF5g1cAQqkEUIVMyIvytuaBvfuxqyihfT3q3sdVZQt47AOzZ3NQlgwZQoWvGu4B77DcDhihOVZHW8zn0PHm9V-VN-F7bgrU26BlOH8-ZUkr1jJd3wFqsujcrK_UIxmHXrwjaG-tVsgmbhj1EbKAiJa2_cig670C-a_CyeU46kyY_cLqwyWAQLlZLqdo5Ispe-0b7CGe24j3cnf9YJ7T_zVd9ZJLAvCBd1MVe-RmmZ9B29ozvLuU_7M_mSDOw2KRUnDJL-Z_jaO8qXJsi6D4DhvsZkt5TnISa5i3xxBZqoCxCH2q8aTXwYEqM2Gnxg2XWmDRO7JPy2hE4tkllfMYvZHJ74n1ogAAAAG7EjwaAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/b64a54ced71082fb41c39.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b64a54ced71082fb41c39.jpg"
)
VERSION_IMG_URL = getenv(
    "VERSION_IMG_URL", "https://telegra.ph/file/1c3d5586fdc654152ac75.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
