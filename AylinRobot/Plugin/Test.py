import os
from pyrogram import idle, filters
import requests
import wget
from AylinRobot import AylinRobot as app
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
import yt_dlp
from AylinRobot.config import Config
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.types import Message
from pyrogram import *
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import asyncio
import math
import io
import re
import time
import aiofiles
import aiohttp
import wget
import os
from asyncio import get_running_loop
from functools import partial
from io import BytesIO
from urllib.parse import urlparse
import ffmpeg
import lyricsgenius
from youtubesearchpython import VideosSearch



@app.on_message(filters.command('yt') & ~filters.forwarded & filters.text)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("🔎 Searching...")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        
        performer = f"Unknown Artist"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ Cannot find song use another keywords"
        )
        print(str(e))
        return
    m.edit("Ssss")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        caption_for_logchannel = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 👤 İstəyən: {isteyen}**
**├───────────────**
**├▷ 🌀 Bot: @{Config.BOT_USERNAME}**
**╰───────────────**
'''
        caption_for_private = f'''
**╭───────────────**
**├▷ 🎧 Başlıq: [{title}]({link})**
**├───────────────**
**├▷ 👁‍🗨 Baxış: {views}**
**├───────────────**
**├▷ 🌀 Bot: @{Config.BOT_USERNAME}**
**╰───────────────**
'''
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        m.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=caption_for_private, quote=False, title=title, duration=dur, thumb=thumb_name, performer = f"{Config.PLAYLIST_NAME}", reply_markup=buttons['markup_for_private'])
        m.delete()
        app.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=caption_for_logchannel, performer = f"{Config.BOT_USERNAME}", title=title, duration=dur, thumb=thumb_name, reply_markup=buttons['add_to_group'])
    except Exception as e:
        m.edit(f'**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı {Config.OWNER_NAME} sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)