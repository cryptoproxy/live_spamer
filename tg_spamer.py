import time
from random import randint, choice
from pyrogram import Client
from config import API_ID, API_HASH


api_id = API_ID
api_hash = API_HASH

# Пишите юзернейм жертвы
tg = '@telegram_username'
user = '@AnonRuBot'
i = 0





def send(text: str, user: str):
    try:
        app.send_message(user, text)
    except:
        time.sleep(3)


# по рофлу добавил
hello = ['приветик', 'ку', 'йо', 'даров', 'охае', 'кукусь']
while True:
    try:
        with Client("my_account", api_id, api_hash) as app:
            send(text='/search', user=user)
            time.sleep(9)
            send(text=f'{choice(hello)}, поможешь мне?', user=user)
            time.sleep(7)
            send(text=f'поздравь мою подругу с др пж, вот её тг {tg}\nа я тебе сиськи скину', user=user)
            time.sleep(30)
            send(text='ну шо поздравишь?', user=user)
            time.sleep(2)
            send(text='/stop', user=user)


    except:
        send(text='/stop', user=user)
        send(text='/search', user=user)
        continue


