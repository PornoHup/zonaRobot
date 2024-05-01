# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "12349641"))
   API_HASH = os.getenv("API_HASH", "0f9159afc920f9c592df555e4b1cb73b")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6935426940:AAFPjtMdrDFNmKo1cI5N2MKfWI_H0UyghsY")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "ayanrobot")
   BOT_NAME = os.environ.get("BOT_NAME", "ayanrobot")
   OWNER_ID = int(os.environ.get("OWNER_ID", "6881891677"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "thagiyev") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002115471818"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "nezrinlogo")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002140637128"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002115471818"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "56ae7152-5102-4d4b-8ab7-218810c69336")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "riyad")
   CHANNEL = os.environ.get("CHANNEL", "nezrinlogo")
   SUPPORT = os.environ.get("SUPPORT", "nezrinlogo")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg")
