# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import secrets, string, aiohttp
from AylinRobot import AylinRobot as app
from Sehid import random_line
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@app.on_message(filters.command("game"))
async def _(client, message):
	user = message.from_user
	await message.reply_text(text="{} Doğruluq yoxsa cəsarət!".format(user.mention, await random_line('Sehid/sehid.txt')), reply_markup=button)
    
button = reply_markup=InlineKeyboardMarkup(
[[InlineKeyboardButton("🇦🇿 Şəhid", callback_data="deyis"),
InlineKeyboardButton("🔐 Bağla", callback_data="close")]])


@app.on_callback_query(filters.regex("deyis"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text((await random_line('Sehid/sehid.txt')), reply_markup=button)