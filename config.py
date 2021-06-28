from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1602591136:AAHvluVntjW1aSCclIFWhyG51JKVzz0rRGk" #imp
    APP_ID = 5540967 #imp
    API_HASH = "eedf0196b0533f361b51b5b7082358e9" #imp
    AUTH_CHANNEL = [-100138716715, -1001563645757] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://torrentleech.torrentleech-gdrive.workers.dev
    GLEECH_COMMAND = "gleech@TorrentLeech_Gdrivebot"
    YTDL_COMMAND = 'ytdl@TorrentLeech_Gdrivebot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@TorrentLeech_Gdrivebot"
    CLONE_COMMAND_G = "gclone@groupname"
    PYTDL_COMMAND_G = "pytdl@groupname"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech@TorrentLeech_Gdrivebot"
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.-XX9fgU--","token_type":"Bearer","refresh_token":"1//0gLZEp8-VV2rZyourtCgYIARAAGBASNwF-","expiry":"2020-09-03T14:22:34.599776393Z"}\nteam_drive = """
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""
