# def func():
#     print('dd')
#
#
# value_func = func
# value_func()


# def func1():
#     def func2():
#         print('func2')
#
#     print('func1')
#     func2()
#
#
# func1()

# def decorator(func):
#     def wrapper():
#         print('функция-оболочка')
#         func()
#
#     return wrapper
#
#
# def basic():
#     print('основная функция')
#
#
# wrapped = decorator(basic)
# print('старт программы')
# basic()
# print('до wrapped()')
# wrapped()
# print('конец программы')

# def decorator(func):
#     print('декоратор')
#
#     def wrapper():
#         print('-- до функции', func.__name__)
#         func()
#         print('-- после функции', func.__name__)
#
#     return wrapper
#
#
# @decorator
# def wrapped():
#     print('--- обернутая функция')
#
#
# print('- старт программы...')
# wrapped()
# print('- конец программы')

# def decorator_1(func):
#     print('декоратор 1')
#
#     def wrapper():
#         print('перед функцией c decorator_1')
#         func()
#
#     return wrapper
#
#
# def decorator_2(func):
#     print('декоратор 2')
#
#     def wrapper():
#         print('перед функцией c decorator_2')
#         func()
#
#     return wrapper
#
#
# @decorator_1
# @decorator_2
# def basic_1():
#     print('basic_1')
#
#
# @decorator_1
# def basic_2():
#     print('basic_2')
#
#
# print('>> старт')
# basic_1()
# basic_2()
# print('>> конец')


# @decorator_1
# @decorator_2
# def wrapped():
#     pass
#
#
# a = decorator_1(decorator_2(wrapped))

# def decorator_1(func_func):
#     print('декоратор 1')
#
#     def wrapper_func():
#         print('перед функцией c decorator_1')
#         return func_func()
#
#     return wrapper_func
#
#
# @decorator_1
# def func1():
#     return 1
#
#
# print(func1())

# import time
#
#
# def decorator(func):
#     def wrapper():
#         print('перед функцией c decorator_1')
#         start = time.time()
#         func_res = func()
#         stop = time.time()
#         result = stop - start
#         # print(result)
#         return func_res, result
#
#     return wrapper
#
#
# @decorator
# def func():
#     time.sleep(1)
#     print('sleep 3')
#     return 3
#
#
# @decorator
# def func2():
#     sum_res = 0
#     for i in range(1000000):
#         sum_res += 1
#
#
# print(func())
# print(func2())


# Написать простой декоратор добавляющий текст начало функции и конец функции к функции,
# которая выводит Привет мир!
def decorator(func):
    def hi():
        print('Начало функции')
        func()
        print('Конец функции')

    return hi


@decorator
def func():
    print('Привет мир!')


func()
# print()
