# regex/regexp

# https://pythex.org/
# https://regex101.com/
# http://www.pyregex.com/

import re

# sentence = 'hello world hello!'
# r = re.match('hello', sentence)
# print(r)
# print(r.span())
# print(r.start())
# print(r.end())
#
# print(r.group(0))


# sentence = '1357594719074829 3745982137489231 hello world!'
# r = re.match('\d+', sentence)
# print(r)
# print(r.group(0))
# a = '1\n1'
# b = r'1\n1'
# print(a)
# print(b)

# sentence = 'Hello world!'
# r = re.match(r'hello', sentence, re.I)
# if r:
#     print(r.group(0))
# else:
#     print('He найдено совпадений')

# sentence = 'Hello world!'
# r = re.search(r'hello', sentence, re.I)
# if r:
#     print(r)
#     print(r.group(0))
# else:
#     print('He найдено совпадений')


# sentence = 'Hello World!'
# r = re.search(r'(\w+)\s(\w+)', sentence, re.I)
# if r:
#     print(r.group(0))
#     print(r.group(1))
#     print(r.group(2))
# else:
#     print('He найдено совпадений')

# sentence = 'Python! Регулярные выражения в python'
# r = re.findall(r'python', sentence, re.I)
# print(r)


# sentence = 'Моя почта example@domain.ru'
# r = re.search(r'(\w+)@(\w+)\.(\w{2})', sentence)
# print(r.group(0))
# print(r.group(1))
# print(r.group(2))
# print(r.group(3))

# user_mail = input('Введите адрес электронной почты')
# if re.match(r'\w+@\w+\.\w{2,}', user_mail):
#     print('Почта верна')
# else:
#     print('Почта неверна')


user_mail = input('Введите адрес электронной почты:')
if re.match(r'[0-3a-zA-Zа-яёА-ЯЁ]{1,}@[a-z]+\.[a-z]{2,}', user_mail):
    print('Почта верна')
else:
    print('Почта неверна')
