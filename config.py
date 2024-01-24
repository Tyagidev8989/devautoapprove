from pyrogram.types import *

class Config:
    API_ID = int(27723431)
    API_HASH = "31e95a9870e7093fdf9586f2f6d6c88a"
    BOT_TOKEN = "5857092435:AAGsqf9cKtP_VdLwpuJVj0Kv4wYNaBesghk"
     
    

    ADMINS = [5606017879, 6012752629, 5558249587]
    DB_URL = "mongodb+srv://tyagidev8989:1212@dev@cluster0.h7y6ifi.mongodb.net/?retryWrites=true&w=majority"                    
    DB_NAME = "main"

    GIF = ['https://graph.org/file/2a8ff37310234bb666dee.jpg', 'https://graph.org/file/4d1c1981b6d8faa7238af.jpg',]
    img1 = "https://graph.org/file/37fae3f4db1073a9da1e3.jpg"
    img2 = "https://graph.org/file/5d2e3df6e4040e3f3d337.jpg"
  
    start_text = "**Hello {}!\nI'm an auto approve Admin Join Requests Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n💎Powerd By : @Tyagidev999**"               
    
    cap="**👇 YADAVJI THE BRAND 👇**"

        
    movie_btn = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✅ TOSS WINNER ✅", url="https://t.me/+pAPDRe1P0HkwNDhl"),
    	            ],[
                        InlineKeyboardButton("🕹 MATCH WINNER 🕹", url="https://t.me/+pAPDRe1P0HkwNDhl")
                    ],[
                        InlineKeyboardButton("🎥  FIX SESSION   🎥", url="https://t.me/+pAPDRe1P0HkwNDhl"),
		    ],[
                        InlineKeyboardButton("📊 FREE MARKET LOAD 📊", url="https://t.me/+pAPDRe1P0HkwNDhl")
                    ]    
                ]
    )

    bot_btn = InlineKeyboardMarkup([[
	    InlineKeyboardButton("DEV TYAGI", url="http://t.me/tyagidev999"),
            #InlineKeyboardButton("Movie Updates", url="https://t.me/mr_link_z")
    ]])


class temp:
    SETTINGS = {}
    broadcast_ids = {}
