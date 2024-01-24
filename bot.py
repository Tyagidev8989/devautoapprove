import os, time, string, random, re, asyncio, aiofiles, datetime, aiofiles.os

from traceback import format_exc
from pyrogram.types import *
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant, FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from config import Config, temp



from database import add_user, add_group, all_users, all_groups, users, remove_user
   
 
 
 
Bot = Client(name="approver", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

 
@Bot.on_message(filters.command("start"))
async def _if_start(c, m):
    user = m.from_user
    await m.reply_text(text=Config.start_text.format(user.mention), reply_markup=Config.bot_btn)     
  
   
@Bot.on_chat_join_request(filters.group | filters.channel)
async def approve(c, m):


    chat_id = m.chat.id
    user = m.from_user
    user_id = user.id
    add_user(user_id)
   
    
    await c.approve_chat_join_request(chat_id, user_id)
    await c.send_photo(user_id, photo="https://mallucampaign.in/images/img_1706091703.jpg", caption=Config.cap.format(user.mention, m.chat.title), reply_markup=Config.movie_btn)

    
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Bot.on_message(filters.command("users") & filters.user(Config.ADMINS))
async def dbtool(_, m : Message):
    xx = all_users()


    await m.reply_text(text=f"""
🍀 Stats 🍀
🙋‍♂️ Users : `{xx}`""")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Bot.on_message(filters.command("bcast") & filters.user(Config.ADMINS))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")



 
 



    
print("I'm Alive Now!")
Bot.run()
