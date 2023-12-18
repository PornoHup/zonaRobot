# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "21236884"))
   API_HASH = os.getenv("API_HASH", "2e526fe32b1177ba7ce3d552640ab854")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6798589879:AAHAZQYVg0lV1rLndsGj_smVEFvWLS0uMqA")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "ZonaTaggerbot")
   BOT_NAME = os.environ.get("BOT_NAME", "ZonaTagger")
   OWNER_ID = int(os.environ.get("OWNER_ID","6881891677"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "mirizyv") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://qenberismayilzade005:natiq.3169@cluster0.wna0quv.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001721854326"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "ZonaMusicPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002011627494"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001721854326"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "c7c2f4ed-e8c3-46e8-ae9a-bfd0ed6b1a69")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Miri")
   CHANNEL = os.environ.get("CHANNEL", "ZonaSupportKanal")
   SUPPORT = os.environ.get("SUPPORT", "ZonaSupportKanal")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg")
