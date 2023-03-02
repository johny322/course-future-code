# Bot API
# https://core.telegram.org/bots/api
# https://tlgrm.ru/docs/bots/api

# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
#
from pprint import pprint

import requests

BASE_URL = 'https://api.telegram.org/bot'
token = '6140305778:AAH7b3GscfEle_aHkJRJoSPHZTW1WE_Z034'
admin_id = [5014092219]

# response = requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={admin_id}&text=hi')
# print(response.json())

# response = requests.get(f'{BASE_URL}{token}/getUpdates')
# print(response.json())


# def polling():
#     len_count = 0
#     while True:
#         res = requests.get(f'{BASE_URL}{token}/getUpdates').json()
#         print(res)
#         if len_count != len(res['result']):
#             print(len_count)
#             len_count = len(res['result'])
#
#             message = res['result'][-1]['message']
#             from_id = message['from']['id']
#             if from_id in admin_id:
#                 requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={from_id}&text=Привет')
#
#
# polling()
# def pulling():
#     count_message = 0
#     while True:
#         response = requests.get(f'{BASE_URL}{token}/getUpdates').json()
#         print(response)
#         print(response['result'])
#         if count_message != len(response['result']):
#             count_message = len(response['result'])
#             message = response['result'][-1]
#             print(count_message)
#
#
# pulling()

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

