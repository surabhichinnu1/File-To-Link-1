import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.extra import botstats
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\n𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nStarted {Var.BOT_UN}!!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📢 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",    
            caption=f"👋**𝙷𝙴𝙻𝙻𝙾  {m.from_user.mention}**\n\n**𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃.**\n\n**𝙸 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴𝚂 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙾𝙽𝙻𝙸𝙽𝙴 & 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶..\n\n𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴 𝚃𝙾 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉.\nNB:🔞 Dont forward Porn Files to me, You will Get Permanent B A N\n\nMADE BY @mkn_bots_updates**",
            reply_markup=InlineKeyboardMarkup( [[                
                InlineKeyboardButton("👨‍💻 𝙾𝚆𝙽𝙴𝚁", url="https://t.me/mr_MKN"),
                InlineKeyboardButton("📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂", url="https://t.me/mkn_bots_updates")
                ],[ 
                InlineKeyboardButton('🔮 𝚂𝚃𝙰𝚃𝚄𝚂', callback_data='stats'),                 
                InlineKeyboardButton('🔑 𝙰𝙱𝙾𝚄𝚃', callback_data='about')
                ]]
            ),
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("📢 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴𝙳...⚡\n\n🗂️ 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴 :-\n{}\n {}\n\n📎 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 :- {}\n\n♻️ 𝚃𝙷𝙸𝚂 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙰𝙽𝙳 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙴𝚇𝙿𝙸𝚁𝙴 ♻️\n\n@mkn_bots_updates**"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚀 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙽𝙾𝚆 🚀", url=stream_link)]])
        )

@StreamBot.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
          await query.message.edit_text(                  
              text=f"👋**𝙷𝙴𝙻𝙻𝙾  {query.from_user.mention}**\n\n**𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃.**\n\n**𝙸 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴𝚂 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙾𝙽𝙻𝙸𝙽𝙴 & 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶..\n\n𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴 𝚃𝙾 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉....**",
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 𝙾𝚆𝙽𝙴𝚁", url="https://t.me/mr_MKN"),
                  InlineKeyboardButton("📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂", url="https://t.me/mkn_bots_updates")
                  ],[ 
                  InlineKeyboardButton('🔮 𝚂𝚃𝙰𝚃𝚄𝚂', callback_data='stats'),                 
                  InlineKeyboardButton('🔑 𝙰𝙱𝙾𝚄𝚃', callback_data='about')                  
                  ]]
                  )
              )
          return
    elif data == "about":
        await query.message.edit_text(
            text="""
╭━━━━━━━〔🚀 𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺 𝙱𝙾𝚃 🚀〕
┣😎𝙲𝚁𝙴𝙰𝚃𝙴𝚁 : <a href='https://t.me/mr_MKN'>𝙼𝚛.𝙼𝙺𝙽 𝚃𝙶</a>
┣📢𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : <a href='https://t.me/mkn_bots_updates'>Mᴋɴ Bᴏᴛᴢ™</a>
┣📡𝚂𝙴𝚁𝚅𝙴𝚁 :  <a href='https://help.heroku.com'>𝙷𝙴𝚁𝚄𝙺𝙾</a>
┣📚𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : <a href='https://docs.pyrogram.org'>𝙿𝚁𝙾𝙶𝚁𝙰𝙼</a>
┣🗄️𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: <a href='https://www.python.org'>𝙿𝚈𝚃𝙷𝙾𝙽 3</a>
┣❣️𝚂𝙾𝚄𝚁𝙲𝙴-𝙲𝙾𝙳𝙴 : <a href='https://youtu.be/W4wSOZw8GXk'>𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺</a>
┣👨‍💻𝙳𝙴𝚅𝙾𝙻𝙴𝙿𝙴𝚁 : <a href='https://github.com/Aadhi000'>𝙰𝙰𝙳𝙷𝙸</a>
╰━━━━━━━〔𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚄𝙿𝙿𝙾𝚁𝚃〕""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
            InlineKeyboardButton("↩️ 𝙱𝙰𝙲𝙺", callback_data = "start")
            ]]                           
        )
    )
    elif data == "stats":
       await query.message.edit_text(
           text=botstats,
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("↩️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]                           
               )
           )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
