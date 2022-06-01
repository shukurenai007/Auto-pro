from telethon import custom, events, Button
import os,re
import asyncio

import telethn as bot
import telethn as tgbot
import telethn as aasf
from events import register

edit_time = 5
Alice1 = "https://telegra.ph//file/440b699a8f78adc90ef98.jpg"
Alice2 = "https://telegra.ph//file/b63f6d69eb2c65472a348.jpg"
Alice3 = "https://telegra.ph//file/82c65b1ea70e0ce3e5188.jpg"
Alice4 = "https://telegra.ph//file/1e270d1e7c1d624c3ef31.jpg"
Alice5 = "https://telegra.ph//file/212a6c06521d489367c89.jpg"

@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  on = await aasf.send_message(event.chat, f"**❦ Hᴇʏ {(event.sender.first_name)}**\n\n**❦ I Aᴍ [Rose](https://t.me/Rose01RoBot)**\n**❦ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [HollywoodNight](t.me/HollywoodNights)**", file=Alice1, buttons=button)

  await asyncio.sleep(edit_time)
  ok = await aasf.edit_message(event.chat_id, on, file=Alice2, buttons=button) 

  await asyncio.sleep(edit_time)
  ok2 = await aasf.edit_message(event.chat_id, ok, file=Alice3, buttons=button)

  await asyncio.sleep(edit_time)
  ok3 = await aasf.edit_message(event.chat_id, ok2, file=Alice4, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok4 = await aasf.edit_message(event.chat_id, ok3, file=Alice1, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok5 = await aasf.edit_message(event.chat_id, ok4, file=Alice2, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok6 = await aasf.edit_message(event.chat_id, ok5, file=Alice3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok7 = await aasf.edit_message(event.chat_id, ok6, file=Alice5, buttons=button)

  await asyncio.sleep(edit_time)
  ok8 = await aasf.edit_message(event.chat_id, ok7, file=Alice4, buttons=button)
 
  await asyncio.sleep(edit_time)
  ok9 = await aasf.edit_message(event.chat_id, ok8, file=Alice1, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    ALICE = "YOUR DETAILS BY NAGI SANZENIN \n"
    ALICE += f"FIRST NAME : {PRO.first_name} \n"
    ALICE += f"LAST NAME : {PRO.last_name}\n"
    ALICE += f"YOU BOT : {PRO.bot} \n"
    ALICE += f"RESTRICTED : {PRO.restricted} \n"
    ALICE += f"USER ID : {boy}\n"
    ALICE += f"USERNAME : {PRO.username}\n"
    await event.answer(ALICE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
