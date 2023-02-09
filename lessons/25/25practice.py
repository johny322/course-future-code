import time

# from functools import wraps


# def decor(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @decor
# def func(a, b):
#     """Функция возвращает сложение двух чисел"""
#     return a + b
#
#
# print(func(1, 5))
# print(func.__name__)
# print(func.__doc__)
# from functools import cache
#
#
# @cache
# def func(n):
#     result = 0
#     for i in range(n):
#         result += i
#     return result
#
#
# start1 = time.time()
# print(func(100000000))
# end1 = time.time()
# print(end1 - start1)
#
# start2 = time.time()
# print(func(100000000))
# end2 = time.time()
# print(end2 - start2)
#
# start3 = time.time()
# print(func(100000001))
# end3 = time.time()
# print(end3 - start3)

# print(int('qwerty'))
# BaseException

# import time
# time.sleep(10)
# print('hi')

# try:
#     k = int('1 / 0')
#
#     print('blabla')
# except ValueError:
#     print('ValueError')
#     k = 1
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#     k = 0
#
# print(k)

# try:
#     k = '1 / 0'
#     k[0] = 'dsa'
#
#     print('blabla')
# except (ValueError, ZeroDivisionError):
#     print('ValueError or ZeroDivisionError')
#     k = 1
# except Exception as ex_text:
#     print(f'Exception: {ex_text}')
#     k = None
# else:
#     print('нет ошибок')
# finally:
#     print('finally block')
#
# print(k)

# def func():
#     time.sleep(4)
#
#
# try:
#     func()
# except Exception:
#     print('except')
# # KeyboardInterrupt
# print('after try block')

# class MyException(Exception):
#     pass
#
#
# try:
#     while True:
#         k = input()
#         print(f'{k=}')
#         if k == 'q':
#             raise MyException('передан аргумент "q"')
# except MyException as ex:
#     print(f'MyException: {ex}')

# Написать функцию check_date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в
# нашем календаре, и False иначе. При написании использовать исключения

# from datetime import date
#
#
# def check_date(y, m, d):
#     try:
#         date(y, m, d)
#         return True
#     except Exception:
#         return False
#
#
# print(check_date(2006, 4, 24))
# print(check_date(2006, -4, 24))


# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с
# первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер
# столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES»,
# если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.

# 1,3 - 1,4 = YES
# 1,3 - 2,3 = YES
# 1,3 - 2,4 = NO

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())

# if (a1 == a3) or (a2 == a4):
#     print('YES')
# else:
#     print('NO')
print('YES') if (a1 == a3) or (a2 == a4) else print('NO')


