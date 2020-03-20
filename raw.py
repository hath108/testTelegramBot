'''
https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md

python - m venv .venv
pip install requests[socks]
pip install pyTelegramBotAPI
pip freeze > requirements.txt
git init

'''
import requests
BASE_URL = "https://api.telegram.org/bot1036931187:AAEgRa7nOS3nAsodpE-RGOKBZLRC-3_rasI/"
r = requests.get(f'{BASE_URL}getme')
r = requests.get(f'{BASE_URL}getUpdates')
r.json()

# export BOT_TOKEN = 1036931187: AAEgRa7nOS3nAsodpE-RGOKBZLRC-3_rasI
