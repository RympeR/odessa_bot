import sys
from pyrogram import Client
import time
import random

api_id = 1119766
api_hash = "2019edb7991735a90ec9a04cadad05ff"

CHOISES = (1, 2, 3, 3, 3, 3)

LOOP = True
CHAT_ID = 1234060895
DEFAULT_TEXT = '''Переходи в наш чат 💬  
🌇Там тебя ждут новые знакомства и много другое 🌇
Ждем тебя ❤️
t.me/+5KlQLvCh6vFkYjdi'''


app = Client("my_account", api_id, api_hash)


@app.on_message()
def log(client, message):
    global LOOP
    if message.text.startswith('Слишком много лайков за сегодня ') or message.text.startswith('1. Смотреть анкеты.'):
        LOOP = False
    print(message)

try:
    app.start()
    while LOOP:
        choice = random.choice(CHOISES)
        app.send_message(
            chat_id=CHAT_ID,
            text=random.choice(CHOISES)
        )
        time.sleep(0.3)
        if choice != 3:
            app.send_message(
                chat_id=CHAT_ID,
                text=DEFAULT_TEXT
            )
            time.sleep(0.5)
    app.stop()
except Exception as e:
    print(e, file=sys.stderr)
    app.stop()
