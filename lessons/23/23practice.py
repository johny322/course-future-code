# class Decorator:
#     def __init__(self, func):
#         print('> Класс Decorator метод __init__')
#         self.func = func
#
#     def __call__(self):
#         print('> перед вызовом класса...', self.func.__name__)
#         self.func()
#         print('> после вызова класса')
#
#
# @Decorator
# def wrapped():
#     print('функция wrapped')
#
#
# print('>> старт')
# wrapped()
# print('>> конец')


# class A:
#     def __init__(self):
#         print('__init__')
#         self.name = 'A'
#
#     def __call__(self):
#         print('__call__')
#
#
# a = A()
# a()
# print(a.name)

# def decorator_with_args(func):
#     print('> декоратор с аргументами...')
#
#     def decorated(a, b):
#         print('до вызова функции', func.__name__)
#         ret = func(a, b)
#         print('после вызова функции', func.__name__)
#         return ret
#
#     return decorated
#
#
# @decorator_with_args
# def add(a, b):
#     print('функция 1')
#     return a + b
#
#
# @decorator_with_args
# def sub(a, b):
#     print('функция 2')
#     return a - b
#
#
# print('>> старт')
# r = add(10, 5)
# print('r:', r)
# g = sub(10, 5)
# print('g:', g)
# print('>> конец')

# class Decorator:
#     def __init__(self, func):
#         print('> Класс Decorator метод __init__')
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('> до вызова из класса...', self.func.__name__)
#         res = self.func(*args, **kwargs)
#         print('> после вызова из класса')
#         return res
#
#
# @Decorator
# def wrapped(a, b):
#     print('функция wrapped:', a, b)
#     print(a + b)
#     return a, b
#
#
# print('>> старт')
# print(wrapped(10, 20))
# print('>> конец')

# # *args и **kwargs
# def func(*args, **kwargs):
#     print(f'{args=}')
#     print(f'{kwargs=}')
#
#
# func(1, 2, 3, a=5, b=1)

# import sys
# import time
#
#
# def get_size(func):
#     def wrapper(*args):
#         result = sys.getsizeof(func(*args))
#         print(f'>> функция {func.__name__} занимает в памяти: {result} байт')
#
#     return wrapper
#
#
# @get_size
# def add_with_delay(a, b, delay=0):
#     print('умножение', a, b, delay)
#     time.sleep(delay)
#     return a * b
#
#
# @get_size
# def loop():
#     res = 0
#     for i in range(10000000):
#         res *= i
#     return res
#
#
# print('старт программы')
# add_with_delay(100000000000000, 2000000000000000, 0)
# # add_with_delay(10, 20, 1)
# loop()
# print('конец программы')


# Написать функцию, которая возвращает сумму двух чисел 4 и 5, также написать декоратор get_type,
# который выводит тип данных возвращаемый декорируемой функцией.
# def f():
#     return 're'
#
#
# print(type(f()))
# def get_sum(a, b):
#     return a + b
#
#
# def get_type(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print('Тип:', type(result))
#         return result
#
#     return wrapper
#
#
# @get_type
# def main():
#     return get_sum(4, 6)


# if __name__ == '__main__':
#     print(main())

# def get_type(func):
#     def wrapper():
#         result = func()
#         print(f"Return type: {type(result)}")
#         return result
#
#     return wrapper
#
#
# @get_type
# def add_numbers():
#     return ['4 + 5']
#
#
# result = add_numbers()
# print(f"Result: {result}")

