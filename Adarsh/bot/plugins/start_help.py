import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
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
            f"#NEW_USER: \n\nπ½π΄π πππ΄π [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nStarted {Var.BOT_UN}!!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("π’ πΉπΎπΈπ½ ππΏπ³π°ππ΄ π²π·π°π½π½π΄π» π’", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(   
            text=f"π**π·π΄π»π»πΎ  {m.from_user.mention}**\n\n**πΈπ°πΌ π° ππΈπΌπΏπ»π΄ ππ΄π»π΄πΆππ°πΌ π΅πΈπ»π΄/ππΈπ³π΄πΎ ππΎ πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ πΆπ΄π½π΄ππ°ππΎπ π±πΎπ.**\n\n**πΈ π²π°π½ πΆπ΄π½π΄ππ°ππ΄ π³πΈππ΄π²π π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ π΅πΎπ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄π π΅πΎπ π³πΎππ½π»πΎπ°π³πΈπ½πΆ πΎπ½π»πΈπ½π΄ & π΅πΎπ ππππ΄π°πΌπΈπ½πΆ..\n\nππ΄π½π³ πΌπ΄ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄ ππΎ ππ΄π΄ πΌπ πΏπΎππ΄ππ.\nNB:π Dont forward Porn Files to me, You will Get Permanent B A N**",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("β‘ ππΏπ³π°ππ΄π", url="https://t.me/Cinema_Kottaka7"), 
                InlineKeyboardButton("π₯ πΆππΎππΏ", url="https://t.me/Cinema_Kottaka07")              
                ],[ 
                InlineKeyboardButton('π? πππ°πππ', callback_data='stats'),                 
                InlineKeyboardButton('π π°π±πΎππ', callback_data='about')
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
                        text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("π’ πΉπΎπΈπ½ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» π’", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
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

        msg_text = "**ππΎππ π»πΈπ½πΊ πΈπ πΆπ΄π½π΄ππ°ππ΄π³...β‘\n\nποΈ π΅πΈπ»π΄ π½π°πΌπ΄ :-\n{}\n {}\n\nπ π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ :- {}\n\nβ»οΈ ππ·πΈπ π»πΈπ½πΊ πΈπ πΏπ΄ππΌπ°π½π΄π½π π°π½π³ ππΈπ»π» π½πΎπ π΄ππΏπΈππ΄ β»οΈ\n\n@mkn_bots_updates**"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("π π³πΎππ½π»πΎπ°π³ π½πΎπ π", url=stream_link)]])
        )

@StreamBot.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
          await query.message.edit_text(                  
              text=f"π**π·π΄π»π»πΎ  {query.from_user.mention}**\n\n**πΈπ°πΌ π° ππΈπΌπΏπ»π΄ ππ΄π»π΄πΆππ°πΌ π΅πΈπ»π΄/ππΈπ³π΄πΎ ππΎ πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ πΆπ΄π½π΄ππ°ππΎπ π±πΎπ.**\n\n**πΈ π²π°π½ πΆπ΄π½π΄ππ°ππ΄ π³πΈππ΄π²π π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ π΅πΎπ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄π π΅πΎπ π³πΎππ½π»πΎπ°π³πΈπ½πΆ πΎπ½π»πΈπ½π΄ & π΅πΎπ ππππ΄π°πΌπΈπ½πΆ..\n\nππ΄π½π³ πΌπ΄ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄ ππΎ ππ΄π΄ πΌπ πΏπΎππ΄ππ....**",
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β‘ ππΏπ³π°ππ΄π", url="https://t.me/Cinema_Kottaka7"), 
                  InlineKeyboardButton("π₯ πΆππΎππΏ", url="https://t.me/Cinema_Kottaka07")              
                  ],[ 
                  InlineKeyboardButton('π? πππ°πππ', callback_data='stats'),                 
                  InlineKeyboardButton('π π°π±πΎππ', callback_data='about')                  
                  ]]
                  )
              )
          return
    elif data == "about":
        await query.message.edit_text(
            text="""
β­βββββββγπ π΅πΈπ»π΄-ππΎ-π»πΈπ½πΊ π±πΎπ πγ
β£ππ²ππ΄π°ππ΄π : <a href='https://t.me/mr_MKN'>πΌπ.πΌπΊπ½ ππΆ</a>
β£π’πππΏπΏπΎππ : <a href='https://t.me/mkn_bots_updates'>Mα΄Ι΄ Bα΄α΄α΄’β’</a>
β£π‘ππ΄πππ΄π :  <a href='https://help.heroku.com'>π·π΄πππΊπΎ</a>
β£ππ»πΈπ±ππ°ππ : <a href='https://docs.pyrogram.org'>πΏππΎπΆππ°πΌ</a>
β£ποΈπ»π°π½πΆππ°πΆπ΄: <a href='https://www.python.org'>πΏπππ·πΎπ½ 3</a>
β£β£οΈππΎπππ²π΄-π²πΎπ³π΄ : <a href='https://youtu.be/W4wSOZw8GXk'>π΅πΈπ»π΄-ππΎ-π»πΈπ½πΊ</a>
β£π¨βπ»π³π΄ππΎπ»π΄πΏπ΄π : <a href='https://github.com/Aadhi000'>π°π°π³π·πΈ</a>
β°βββββββγπΏπ»π΄π°ππ΄ πππΏπΏπΎππγ""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
            InlineKeyboardButton("β©οΈ π±π°π²πΊ", callback_data = "start")
            ]]                           
        )
    )
    elif data == "stats":
       currentTime = readable_time((time.time() - StartTime))
       total, used, free = shutil.disk_usage('.')
       total = get_readable_file_size(total)
       used = get_readable_file_size(used)
       free = get_readable_file_size(free)
       sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
       recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
       cpuUsage = psutil.cpu_percent(interval=0.5)
       memory = psutil.virtual_memory().percent
       disk = psutil.disk_usage('/').percent
       botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
                 f'<b>Total disk space:</b> {total}\n' \
                 f'<b>Used:</b> {used}  ' \
                 f'<b>Free:</b> {free}\n\n' \
                 f'πData Usageπ\n<b>Upload:</b> {sent}\n' \
                 f'<b>Down:</b> {recv}\n\n' \
                 f'<b>CPU:</b> {cpuUsage}% ' \
                 f'<b>RAM:</b> {memory}% ' \
                 f'<b>Disk:</b> {disk}%'
       await query.message.edit_text(
           text=botstats,
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("β»οΈ ππ΄π΅ππ΄ππ·", callback_data = "rfrsh"),
               InlineKeyboardButton("β©οΈ π±π°π²πΊ", callback_data = "start")
               ]]                           
               )
           )
    elif data == "rfrsh":
       await query.answer("Fetching status in DataBase")
       currentTime = readable_time((time.time() - StartTime))
       total, used, free = shutil.disk_usage('.')
       total = get_readable_file_size(total)
       used = get_readable_file_size(used)
       free = get_readable_file_size(free)
       sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
       recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
       cpuUsage = psutil.cpu_percent(interval=0.5)
       memory = psutil.virtual_memory().percent
       disk = psutil.disk_usage('/').percent
       botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
                 f'<b>Total disk space:</b> {total}\n' \
                 f'<b>Used:</b> {used}  ' \
                 f'<b>Free:</b> {free}\n\n' \
                 f'πData Usageπ\n<b>Upload:</b> {sent}\n' \
                 f'<b>Down:</b> {recv}\n\n' \
                 f'<b>CPU:</b> {cpuUsage}% ' \
                 f'<b>RAM:</b> {memory}% ' \
                 f'<b>Disk:</b> {disk}%'
       await query.message.edit_text(
           text=botstats,
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("β»οΈ ππ΄π΅ππ΄ππ·", callback_data = "rfrsh"),
               InlineKeyboardButton("β©οΈ π±π°π²πΊ", callback_data = "start")
               ]]                           
               )
           )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
