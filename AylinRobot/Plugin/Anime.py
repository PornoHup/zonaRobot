# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
import time
from time import time
import random
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram.errors import FloodWait
from AylinRobot.config import Config

photolist = ["https://telegra.ph/file/ebe8512750e0006a19d13.jpg","https://telegra.ph/file/37464958eb8e8c1a086ca.jpg","https://telegra.ph/file/390f1d70ffb2930c12f68.jpg","https://telegra.ph/file/68653583766f4cc47d494.jpg","https://telegra.ph/file/27b1fe3f721a6a4ae6298.jpg","https://telegra.ph/file/9f61304bc19be3b5546a1.jpg","https://telegra.ph/file/2d84ef1cfca743889a8d9.jpg","https://telegra.ph/file/91bbfd4b63abbc2040009.jpg","https://telegra.ph/file/6af7f483dbfb9357c39d7.jpg","https://telegra.ph/file/2107a11862491c4666e83.jpg","https://telegra.ph/file/301e1d06ecf3d8c0d74c4.jpg","https://telegra.ph/file/40fccc4c8bdc3efb05532.jpg","https://telegra.ph/file/409ff7a27c9169e71428e.jpg","https://telegra.ph/file/b0048f18dde35d001bf2e.jpg","https://telegra.ph/file/7da5f792c7e123248bdf8.jpg","https://telegra.ph/file/fde73b2234c70a323ee29.jpg","https://telegra.ph/file/cf9ddebeba9da8aa87b07.jpg","https://telegra.ph/file/5c7dc14f4c56a954be316.jpg","https://telegra.ph/file/e9c416b8510690922526d.jpg","https://telegra.ph/file/8793a6d5ee7c42bd847a7.jpg","https://telegra.ph/file/5cd432b7ea27a6885fb4b.jpg","https://telegra.ph/file/efcb6f4144cff7992797b.jpg","https://telegra.ph/file/71bd278bf0b9d613b1437.jpg","https://telegra.ph/file/32f0f08c1907267f2137a.jpg","https://telegra.ph/file/906cf35e69c4df15717c6.jpg","https://telegra.ph/file/f672081ef93f3531679bf.jpg","https://telegra.ph/file/f1df74dbedb0b75fa0d33.jpg","https://telegra.ph/file/24e606488ea428e8b374f.jpg","https://telegra.ph/file/beb0f47365c2c30cac3e7.jpg","https://telegra.ph/file/b21165bb3633e80cf09d9.jpg","https://telegra.ph/file/33ee73e197a8854f1006e.jpg","https://telegra.ph/file/a27b2ea208f3ece99834f.jpg","https://telegra.ph/file/68a68f3bb1372d1ac5856.jpg","https://telegra.ph/file/6c528549b0319dcc1ce72.jpg","https://telegra.ph/file/e77151ac2c99508c9ab1d.jpg","https://telegra.ph/file/0782ae449c747112f9350.jpg","https://telegra.ph/file/9b99a68abf480d1b813f7.jpg","https://telegra.ph/file/63d14e86b5a1f41bbb3f4.jpg","https://telegra.ph/file/cb6169e13dcb5df7ea50b.jpg","https://telegra.ph/file/3a19b0f9b60d3cf5bf2f9.jpg","https://telegra.ph/file/f5bf486d0dac91f7ffdf2.jpg","https://telegra.ph/file/656e7e011941e8eb05c16.jpg","https://telegra.ph/file/b1a11cd58831329d1bb86.jpg","https://telegra.ph/file/9c920919d0d77fed64d81.jpg","https://telegra.ph/file/520880188fce9eac11380.jpg","https://telegra.ph/file/6ff0ee02a1c629e4e1dc5.jpg","https://telegra.ph/file/b496f6c4065c613f8ec7e.jpg","https://telegra.ph/file/2838408640f4e1764e3c4.jpg","https://telegra.ph/file/389bea612cb8b281b5085.jpg","https://telegra.ph/file/e515f5657ee5148dbd64f.jpg","https://telegra.ph/file/5ba8d4ca6af53ae835b6e.jpg","https://telegra.ph/file/a5e849bc3449ff2e9ba9f.jpg","https://telegra.ph/file/ea4eeb1b85941a828b539.jpg","https://telegra.ph/file/c19e83ce4eb260748d361.jpg","https://telegra.ph/file/edc520bb0ee0365dbc782.jpg","https://telegra.ph/file/ee383d6766ff36f9ccc3f.jpg","https://telegra.ph/file/8f4499e310b129649f544.jpg","https://telegra.ph/file/9445e83ad8336d383be7a.jpg","https://telegra.ph/file/7b89380503d53346468dc.jpg","https://telegra.ph/file/77b7c2ae60936fb16f95a.jpg","https://telegra.ph/file/f482746cebd3b29a5c609.jpg","https://telegra.ph/file/407ec1c756e46786ea7c6.jpg","https://telegra.ph/file/071f32b84f9ab7b98120f.jpg","https://telegra.ph/file/159d1662c74caf48073a8.jpg","https://telegra.ph/file/29c9113c874286ba886a6.jpg","https://telegra.ph/file/2b2317ca6c9125afe4a6b.jpg","https://telegra.ph/file/dcfb0227c17d3c0369f61.jpg","https://telegra.ph/file/6b3987e67bb5ecbc7b183.jpg","https://telegra.ph/file/35b45c0014c85f4c2ccd0.jpg","https://telegra.ph/file/10d9636bfe46150e0ff35.jpg","https://telegra.ph/file/ad57804974b91733da42a.jpg","https://telegra.ph/file/8fab37b1d93146ee6135b.jpg","https://telegra.ph/file/775cfa7e8aafb4bc594d7.jpg","https://telegra.ph/file/d4f16cfcff57ffaf895d3.jpg","https://telegra.ph/file/b4bc1c989c849f0d933bb.jpg","https://telegra.ph/file/725ba7b4f3385a671d9a1.jpg","https://telegra.ph/file/8ec206da36a03ee4bf4d6.jpg","https://telegra.ph/file/37ab9d5274b23a2d8915e.jpg","https://telegra.ph/file/920a060d2c8182874f33.jpg","https://telegra.ph/file/b92e2101d776b637691fb.jpg","https://telegra.ph/file/6c86d031c40b3e0c0fb2c.jpg","https://telegra.ph/file/f72ad2ecb2b2fadf43e91.jpg","https://telegra.ph/file/03cf7c1d5904eed033b7f.jpg","https://telegra.ph/file/94970660aaea999b0c4d6.jpg","https://telegra.ph/file/8eb6b022b7aebe747a651.jpg","https://telegra.ph/file/c7566e128913f034db64e.jpg","https://telegra.ph/file/c269cc7ef854a0890d3a3.jpg","https://telegra.ph/file/7fd8fa52717b2e6272389.jpg","https://telegra.ph/file/7b75a545cd6e75a68a02b.jpg","https://telegra.ph/file/60c70a214857f07051bcf.jpg","https://telegra.ph/file/63aded140647c9015ebc0.jpg","https://telegra.ph/file/7d08ec3973bb4e1afd67b.jpg","https://telegra.ph/file/5b91e5a69d2cf2b339a67.jpg","https://telegra.ph/file/d31045a50ed91dd77f8ea.jpg","https://telegra.ph/file/8adcc39f5745f47162a2a.jpg","https://telegra.ph/file/dbfb9fe68c10f3a621fce.jpg","https://telegra.ph/file/6c91bc0a7eed2d9d4c822.jpg","https://telegra.ph/file/81a4eb04eb9330962bc35.jpg","https://telegra.ph/file/59c567609edcf889ff40d.jpg","https://telegra.ph/file/dbc10b1bd7f963dc000b0.jpg","https://telegra.ph/file/45cff5c51bd6ec5587226.jpg","https://telegra.ph/file/e8aff891728ec0b12c673.jpg","https://telegra.ph/file/590964b86df38f8880807.jpg","https://telegra.ph/file/2100fb9bf0499aee5ad3b.jpg","https://telegra.ph/file/396a5673658d26a2775b0.jpg","https://telegra.ph/file/c1816ec3cd32fd0c43c0b.jpg","https://telegra.ph/file/23f6315d106dc352fb07f.jpg","https://telegra.ph/file/39993d3e4a2f3721b9ae4.jpg","https://telegra.ph/file/2d3cafa79f22eebf5def6.jpg","https://telegra.ph/file/1b249d53f3440cf336310.jpg","https://telegra.ph/file/33980d92c1c5d26a5e7a5.jpg","https://telegra.ph/file/00559a2adad45c3c297d5.jpg","https://telegra.ph/file/cf4eaa233fd52c14b72da.jpg","https://telegra.ph/file/323d2077a9ee34fb17472.jpg"] 

@app.on_message(filters.command("anime"))
async def anime(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Bir Anime Şəkili Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ **{Config.BOT_USERNAME} Sizin Üçün Rondom Bir Anime Şəkili Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()