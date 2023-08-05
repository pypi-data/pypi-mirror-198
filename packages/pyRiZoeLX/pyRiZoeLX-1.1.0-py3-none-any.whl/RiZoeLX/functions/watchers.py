"""
   RiZoeLX 2022 © pyRiZoeLX
"""

from PhoenixScanner import Phoenix
import random

def random_token():
   Toks = ["RED7-yppfpzmakyopbjiwyccs", 
           "RED7-s7gforbm7iga1bj34qvlsa",
           "RED7-riw5wtg5mpjlcxi6jtjqhh",
           "RED7-cwnwhnzu305f24304nrs38",
           "RED7-gsgqo3eoab0vqsx1fw808",
          ]
   token = random.choice(Toks)
   return token


def update_scanlist():
   Red7 = Phoenix(random_token())
   newlist = Red7.scanlist()
   if newlist == {'message': 'Invalid Token'}:
      newlist = Red7.scanlist()
      if newlist == {'message': 'Invalid Token'}:
         raise 'Invalid Scanner Token'
   return newlist


# [Pyrogram]
async def Red7_Watch(RiZoeL, message):
   Red7_Client = Phoenix(random_token())
   user = message.from_user
   msg = f"""
** Alert ⚠️**
User {user.mention} is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
   """
   try:
      check = Red7_Client.check(user.id)
   except Exception as eor:
      print(str(eor))
   
   if check['is_gban']:
      try:
         await RiZoeL.ban_chat_member(message.chat.id, user.id)
         await RiZoeL.send_message(message.chat.id, msg, disable_web_page_preview=True)
      except Exception as eorr:
         print(str(eorr))


# [Telethon]
from telethon.tl import types, functions

RIGHTS = types.ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def Red7_Watch_telethon(RiZoeL, message):
   user = message.sender_id
   Red7_Client = Phoenix(random_token())
   msg = f"""
 Alert ⚠️
User [{user}](tg://user?id={user}) is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
   """
      try:
      check = Red7_Client.check(user.id)
   except Exception as eor:
      print(str(eor))
   
   if check['is_gban']:
      try:
         await RiZoeL(functions.channels.EditBannedRequest(message.chat_id, user, BANNED_RIGHTS))
         await RiZoeL.send_message(message.chat_id, msg, link_preview=False)
      except Exception as eorr:
         print(str(eorr))

