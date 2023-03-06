# https://youtu.be/qoaLdCdZOfc
import time

import requests

BASE_URL = 'https://api.telegram.org/bot'
TOKEN = 'TOKEN'
admin_id = [5014092219]
user_id = 5014092219

res = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
update = res['result'][-1]
print(update)

# chat_id = update['message']['from']['id']
# print(chat_id)
# sendVideo
# file_id = update['message']['video']['file_id']
# print(file_id)
#
# res = requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={chat_id}&video={file_id}&caption=Это видео').json()
# print(res)

# sendVoice
# file_id = update['message']['voice']['file_id']
# print(file_id)
#
# res = requests.get(f'{BASE_URL}{TOKEN}/sendVoice?chat_id={chat_id}&voice={file_id}&caption=Это аудиосообщение').json()
# print(res)


# # sendContact
# res = requests.get(f'{BASE_URL}{TOKEN}/sendContact?chat_id={chat_id}&phone_number=89003444527&first_name=Иван').json()
# print(res)


# # sendLocation
# res = requests.get(f'{BASE_URL}{TOKEN}/sendLocation?chat_id={chat_id}&latitude=55.4507&longitude=37.3656').json()
# print(res)


# # # sendVenue
# res = requests.get(f'{BASE_URL}{TOKEN}/sendVenue?chat_id={chat_id}&latitude=55.4507&longitude=37.3656&title=Москва').json()
# print(res)


# # getUserProfilePhotos
# res = requests.get(f'{BASE_URL}{TOKEN}/getUserProfilePhotos?user_id={chat_id}').json()
# print(res)
#
# photo = res['result']['photos'][-1][0]
# file_id = photo['file_id']
# print(photo)
#
# res = requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={file_id}').json()
# print(res)

# # getFile
# # https://api.telegram.org/file/bot<token>/<file_path>
#
# res = requests.get(f'{BASE_URL}{TOKEN}/getFile?file_id=AgACAgUAAxkDAAP2ZAYKuAABRerS-5Jz2k7prgXttM_EAAJiszEbge_JVOS1oBrE8ao9AQADAgADYQADLgQ').json()
# file_path = res['result']['file_path']
# link = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
# print(link)
# ReplyKeyboardMarkup
# res = requests.get(
#     f'{BASE_URL}{TOKEN}/',
#     json={
#         'method': 'sendMessage',
#         'chat_id': chat_id,
#         'text': 'Сообщение с клавиатурой',
#         'reply_markup': {
#             'keyboard': [
#                 [
#                     {
#                         'text': 'Поделиться контактом',
#                         'request_contact': True
#                     },
#                     {
#                         'text': 'Гео',
#                         'request_location': True
#                     }
#                 ],
#                 [
#                     {
#                         'text': 'текст кнопки3'
#                     }
#                 ],
#             ],
#             'resize_keyboard': True,
#             'one_time_keyboard': True
#         }
#     }
# ).json()
# time.sleep(3)
#
# res = requests.get(
#     f'{BASE_URL}{TOKEN}/',
#     json={
#         'method': 'sendMessage',
#         'chat_id': chat_id,
#         'text': 'Сообщение с клавиатурой',
#         'reply_markup': {
#             'keyboard': [
#                 [
#                     {
#                         'text': 'Поделиться контактом',
#                         'request_contact': True
#                     },
#                     {
#                         'text': 'Гео',
#                         'request_location': True
#                     }
#                 ],
#                 [
#                     {
#                         'text': 'текст кнопки3'
#                     }
#                 ],
#                 [
#                     {
#                         'text': 'текст кнопки4'
#                     }
#                 ],
#             ],
#             'resize_keyboard': True,
#             'one_time_keyboard': True
#         }
#     }
# ).json()
# # print(res)
# time.sleep(3)
# ReplyKeyboardRemove
# r = requests.get(f'{BASE_URL}{TOKEN}/',
#                  json={
#                      'method': 'sendMessage',
#                      'chat_id': user_id,
#                      'text': 'удаление клавиатуры',
#                      'reply_markup': {
#                          'remove_keyboard': True
#                      }
#                  }
#                  ).json()
# print(r)

# @bot_name

# r = requests.get(f'{BASE_URL}{TOKEN}/',
#                  json={
#                      'method': 'sendMessage',
#                      'chat_id': user_id,
#                      # 'text': '<b>Инлайн клавиатура</b>',
#                      'text': '<code>Инлайн клавиатура</code>',
#                      'reply_markup': {
#                          'inline_keyboard': [
#                              [
#                                  {
#                                      'text': 'Ссылка на видео',
#                                      'url': 'https://youtu.be/qoaLdCdZOfc'
#                                  },
#                                  {
#                                      'text': 'Кнопка с callback_data',
#                                      'callback_data': 'some_data1'
#                                  }
#                              ],
#                              [
#                                  {
#                                      'text': 'Кнопка с switch_inline_query',
#                                      'switch_inline_query': 'some text'
#                                  },
#                                  {
#                                      'text': 'Кнопка с switch_inline_query_current_chat',
#                                      'switch_inline_query_current_chat': 'some text'
#                                  },
#
#                              ]
#                          ]
#                      },
#                      'parse_mode': 'HTML'
#                  }
#                  ).json()
# print(r)
