# Bot API
# https://core.telegram.org/bots/api
# https://tlgrm.ru/docs/bots/api

# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
#
import time
from pprint import pprint

import requests

BASE_URL = 'https://api.telegram.org/bot'
token = '6140305778:AAH7b3GscfEle_aHkJRJoSPHZTW1WE_Z034'
admin_id = [5014092219]


# response = requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={admin_id}&text=hi')
# print(response.json())

# response = requests.get(f'{BASE_URL}{token}/getUpdates')
# print(response.json())

# рабочий код
# проверяем id последнего обновления, если оно новое, то обрабатываем
def pulling():
    update_id = 0
    while True:
        time.sleep(0.5)
        r = requests.get(f'{BASE_URL}{token}/getUpdates').json()
        update_id_new = r['result'][-1]['update_id']
        if update_id != update_id_new:
            last_message_data = r['result'][-1]
            user_id = last_message_data['message']['from']['id']
            user_name = last_message_data['message']['from']['first_name']
            requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={user_id}&text=hello, {user_name}')
            update_id = update_id_new


pulling()

# sendPhoto
# response = requests.get(f'{BASE_URL}{token}/getUpdates')
# pprint(response.json()['result'][-1])
# message = response.json()['result'][-1]['message']
# photo = message['photo'][-1]
# print(photo)
# file_id = photo['file_id']
#
# res = requests.get(f'{BASE_URL}{token}/sendPhoto?chat_id=5014092219&photo={file_id}')
# print(res.json())

# sendDocument
# response = requests.get(f'{BASE_URL}{token}/getUpdates')
# # pprint(response.json()['result'][-1])
# message = response.json()['result'][-1]['message']
# pprint(message)
# document = message['document']
# print(document)
# file_id = document['file_id']
#
# res = requests.get(f'{BASE_URL}{token}/sendDocument?chat_id=5014092219&document={file_id}&caption=это фото кота')
# print(res.json())

# sendSticker
# response = requests.get(f'{BASE_URL}{token}/getUpdates')
# # pprint(response.json()['result'][-1])
# message = response.json()['result'][-1]['message']
# pprint(message)
# sticker = message['sticker']
# print(sticker)
# emoji = sticker['emoji']
# res = requests.get(f'{BASE_URL}{token}/sendMessage?chat_id=5014092219&text={emoji}')
# print(res.json())
# file_id = sticker['file_id']
# #
# res = requests.get(f'{BASE_URL}{token}/sendSticker?chat_id=5014092219&sticker={file_id}&disable_notification=true')
# print(res.json())

# sendChatAction
# res = requests.get(f'{BASE_URL}{token}/sendChatAction?chat_id={admin_id[-1]}&action=upload_voice')
# print(res.json())
