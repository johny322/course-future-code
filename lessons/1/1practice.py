# print('hello, world!')
# print('hello, world!')
# Здравствуй, мир!

# name = 'Иван'
# my_name = ''
# her_name = ''
# herName = ''
# nameJohn = 'John'
# print(nameJohn)

# name = input('введите ваше имя')
#
# print(name)
# name = 'Ana'
# print(name)

import random  # подключение модуля random

secret_number = random.randint(1, 10)  # Указываем случайное число
attempts = 3  # Количество попыток

print('Это программа угадай число. У Вас 3 попытки, чтобы постараться отгадать его.')
while attempts > 0:
    print('Попыток ' + str(attempts))  # выводим попытки
    attempts = attempts - 1  # уменьшаем попытки
    user_number = input('Введите ваше число: ')  # Ввод пользователя
    user_number = int(user_number)  # преобразование из строки в число
    if user_number > secret_number:  # условие сравнивает число с загаданным.
        print('Загаданное число меньше')
    if user_number < secret_number:
        print('Загаданное число больше')
    if user_number == secret_number:
        print('Вы угадали!')
        break
    if attempts == 0:
        print('Вы проиграли! Загаданное число ' + str(secret_number))
