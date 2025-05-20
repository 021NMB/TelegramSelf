from .library import *

admin_user_id = 7607683883  #<--- آیدی ادمین
api_id = 27678952 #<--- آی پی آی آیدی
api_hash = '3b41840360dee828e05d2aa0a6dec56b' #<--- ای پی آی هش
helper_username = 'SinaSelfhelperbot' #<--- یوزر ربات هلپر بدون @
bot_token = '7632888509:AAHgLEk-gqDsifDlblmPkNtXF--CGMjH6Rk' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
