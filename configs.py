# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 123456))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))

    ASK_FOR_BLOCKED_WORDS_LIST = os.environ.get("ASK_FOR_BLOCKED_WORDS_LIST",
                                                "Reply to this message with a list of Blocked Words. If those in Message I will not Forward them!\n\nExample:\nhello\nhacker\ncracker\njoin\nabuse heroku\njoin my channel\nchutiyappa")
    ASK_FOR_BLOCKED_EXT_LIST = os.environ.get("ASK_FOR_BLOCKED_EXT_LIST",
                                              "Reply to this message with a list of Blocked Extensions. If any file with that extension I will not forward that file!\n\nExample:\nzip\nmkv\ntorrent\ntxt\npy\ncap\nmp4\nmp3\nrar\n\nExtensions should be in lower case!")
    START_TEXT = """
Hi, This is for @TAMILROCKERSVPN ADMINS
EXPECT ADMINS OTHERS NOT ALLOWED.IF USE THIS 
YOUR TELEGRAM ACCOUNT LEADS TO BAN.WE ARE NOT 
RESPONSIBLE 
.

Check /settings !! 
"""
    ABOUT_CUSTOM_FILTERS_TEXT = """
SUBSCRIBE OUR CHANNEL @TAMILROCKERSVPN 
NEE ROMBA ARIVALI POLA SUTHA MOODITU CLOSE PANNU🤔
TELEGRAM ACCOUNT BAN ACHU NU NAANGA PORUPU ILLA PA
"""
