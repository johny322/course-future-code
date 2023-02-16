import re

# sentence = 'Regex? Я не понимаю Regex!'
#
# result = re.split(r'Regex', sentence)
# print(result)

# sentence = 'Что такое Regex? Я не понимаю Regex!'

# result = re.split(r'Regex', sentence, maxsplit=1)
# print(result)


# result = re.split(r'\?', sentence, maxsplit=1)
# print(result)

# result = re.split(r'[a-zA-Z]+', sentence)
# print(result)


# result = re.sub(r'не понимаю', 'понимаю', sentence)
# print(result)


# result = re.sub(r'Regex', 'regex', sentence, count=1)
# print(result)

# sentence = 'Что тNакое Regex? Я не понимаю Regex!'

# with open('file.txt', 'r', encoding='utf-8') as f:
#     sentence = f.read()
#
# result = re.sub(r'[a-zA-Z]+', '', sentence)
# print(result)

# sentence = 'Что такое Regex? Я не понимаю Regex!'
#
# pattern = re.compile(r'Regex')
# result = pattern.findall(sentence)
# print(result)
# result1 = pattern.sub('', sentence)
# print(result1)

# sentence = 'Что такое Regex? Я не понимаю Regex!'
# # result = re.findall(r'\w', sentence)
# # print(result)
# # print(f'{"".join(result)}')
#
# # result = re.findall(r'^\w+', sentence)
# # print(result)
#
# result = re.findall(r'\w+\W{0,1}$', sentence)
# print(result)

# Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python.
# Номер должен быть длиной 10 знаков и начинаться с 8 или 9.

import re

numbers = ['9999999999', '8999999999', '999999-999', '99999_9999']
for number in numbers:
    if re.match(r'[8-9]{1}[0-9]{9}', number) and len(number) == 10:
        print(f'{number} номер верный')
    else:
        print(f'{number} номер неверный')
