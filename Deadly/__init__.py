import time
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls, idle

_boot_ = time.time()

""" config area """

if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}




#REQUIRED
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")
DB_URL = getenv("DB_URL", None) 
LOG_ID = int(getenv("LOG_ID")) 
STRING1 = getenv("SESSION_NAME", None) 
STRING2 = getenv("SESSION_NAME2", None) 
STRING3 = getenv("SESSION_NAME3", None) 
STRING4 = getenv("SESSION_NAME4", None) 
STRING5 = getenv("SESSION_NAME5", None) 
STRING6 = getenv("SESSION_NAME6", None) 
STRING7 = getenv("SESSION_NAME7", None) 



#SUPPPORT LIST
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


#EXTRA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Elric-xD/DeadlyVC")


#IMAGES
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
PING_URL = getenv(" PING_URL", "https://te.legra.ph/file/abfcbebb3d9d8efbb7762.jpg") 






""" client area """

bot = Client(
    "Freya",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Deadly.modules"),
    )


if not STRING1:
   ASSISTANT_1 = None
else:   
   ASSISTANT_1 = Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING1)     
   user = PyTgCalls(ASSISTANT_1, cache_duration=100, overload_quiet_mode=True)   

if not STRING2:
   ASSISTANT_2 = None
else:   
   ASSISTANT_2 = Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING2)     
   user2 = PyTgCalls(ASSISTANT_2, cache_duration=100, overload_quiet_mode=True)   

if not STRING3:
   ASSISTANT_3 = None
else:
   ASSISTANT_3 =  Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING3) 
   user3 = PyTgCalls(ASSISTANT_3, cache_duration=100, overload_quiet_mode=True)   

if not STRING4:
   ASSISTANT_4 = None
else: 
   ASSISTANT_4 =  Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING4) 
   user4 = PyTgCalls(ASSISTANT_4, cache_duration=100, overload_quiet_mode=True,)   

if not STRING5:
   ASSISTANT_5 = None
else:   
   ASSISTANT_5 =  Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING5) 
   user5 = PyTgCalls(ASSISTANT_5, cache_duration=100, overload_quiet_mode=True,)   

if not STRING6:
   ASSISTANT_6 = None
else:   
   ASSISTANT_6 =  Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING6) 
   user6 = PyTgCalls(ASSISTANT_6, cache_duration=100, overload_quiet_mode=True,)   
   
if not STRING7:
   ASSISTANT_7 = None
else:   
   ASSISTANT_7 =  Client(api_id=API_ID, api_hash=API_HASH, session_name=STRING7) 
   user7 = PyTgCalls(ASSISTANT7, cache_duration=100, overload_quiet_mode=True,)   






call_py = PyTgCalls(ASSISTANT_1, overload_quiet_mode=True)
call_py2 = PyTgCalls(ASSISTANT_2, overload_quiet_mode=True)
call_py3 = PyTgCalls(ASSISTANT_3, overload_quiet_mode=True)
call_py4 = PyTgCalls(ASSISTANT_4, overload_quiet_mode=True)
call_py5 = PyTgCalls(ASSISTANT_5, overload_quiet_mode=True)
call_py6 = PyTgCalls(ASSISTANT_6, overload_quiet_mode=True)
call_py7 = PyTgCalls(ASSISTANT_7, overload_quiet_mode=True)


ASS_IDS = []
ASS_ID1 = 0
ASS_NAME1 = ""
ASS_USERNAME1 = ""
ASS_MENTION1 = ""
ASS_ID2 = 0
ASS_NAME2 = ""
ASS_USERNAME2 = ""
ASS_MENTION2 = ""
ASS_ID3 = 0
ASS_NAME3 = ""
ASS_USERNAME3 = ""
ASS_MENTION3 = ""
ASS_ID4 = 0
ASS_NAME4 = ""
ASS_USERNAME4 = ""
ASS_MENTION4 = ""
ASS_ID5 = 0
ASS_NAME5 = ""
ASS_USERNAME5 = ""
ASS_MENTION5 = ""
ASS_ID6 = 0
ASS_NAME6 = ""
ASS_USERNAME6 = ""
ASS_MENTION6 = ""
ASS_ID7 = 0
ASS_NAME7 = ""
ASS_USERNAME7 = ""
ASS_MENTION7 = ""
MULTI_ASSISTANT = []







with Client("Freya", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    Freya = Freya.get_me()
    BOT_NAME = Freya.first_name
    BOT_USERNAME = Freya.username
