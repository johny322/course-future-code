# def decorator_with_args(name):
#     print('> decorator_with_args:', name)
#
#     def real_decorator(func):
#         print('>> сам декоратор', func.__name__)
#
#         def decorated(*args, **kwargs):
#             print('>>> перед функцие', func.__name__)
#             ret = func(*args, **kwargs)
#             print('>>> после функции', func.__name__)
#             return ret
#
#         return decorated
#
#     return real_decorator
#
#
# @decorator_with_args('test')
# def add(a, b):
#     print('>>>> функция add')
#     return a + b
#
#
# print('старт программы')
# r = add(10, 10)
# print(r)
# print('конец программы')


# class DecoratorArgs:
#     def __init__(self, name):
#         print('> Декоратор с аргументами __init__:', name)
#         self.name = name
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             print('>>> до обернутой функции')
#             if self.name == 'test':
#                 func(1, 1)
#             else:
#                 func(a, b)
#             print('>>> после обернутой функции')
#
#         return wrapper
#
#
# @DecoratorArgs("t")
# def add(a, b):
#     print('функция add:', a, b)
#
#
# print('>> старт')
# add(10, 20)
# print('>> конец')

# def fun():
#     '''
#     это тест функция
#
#     :return: None
#     '''
#     pass
#
#
# print(fun.__doc__)

# def decorator(func):
#     '''Декоратор'''
#
#     def decorated():
#         '''Функция Decorated'''
#         func()
#
#     return decorated
#
#
# @decorator
# def wrapped():
#     '''Оборачиваемая функция'''
#     print('функция wrapped')
#
#
# print('старт программы...')
# print(wrapped.__name__)
# print(wrapped.__doc__)
# print('конец программы')


# from functools import wraps
#
#
# def decorator(func):
#     '''Декоратор'''
#
#     @wraps(func)
#     def decorated():
#         '''Функция Decorated'''
#         func()
#
#     return decorated
#
#
# @decorator
# def wrapped():
#     '''Оборачиваемая функция'''
#     print('функция wrapped')
#
#
# print('старт программы...')
# print(wrapped.__name__)
# print(wrapped.__doc__)
# print('конец программы')

# # Singleton
# def singleton(cls):
#     '''Класс Singleton (один экземпляр)'''
#
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             print('no instance')
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         else:
#             print('yes instance')
#         return wrapper_singleton.instance
#
#     wrapper_singleton.instance = None
#     return wrapper_singleton
#
#
# @singleton
# class TheOne:
#     pass
#
#
# print('старт')
# print('до first_one')
# first_one = TheOne()
# print('до second_one')
# second_one = TheOne()
# print('после second_one')
# print(id(first_one))
# print(id(second_one))
# print('конец')

# user_permissions = ["user", "admin"]
#
#
# def check_permission(permission):
#     def wrapper_permission(func):
#         def wrapped_check():
#             if permission not in user_permissions:
#                 raise ValueError(f"Недостаточно прав: {permission}")
#             return func()
#
#         return wrapped_check
#
#     return wrapper_permission
#
#
# @check_permission("user")
# def check_value():
#     return "значение"
#
#
# @check_permission("admin")
# def do_something():
#     return "только админ"
#
#
# print('старт программы')
# print(check_value())
# print(do_something())
# print('конец программы')


# user_ids = [123456789]
#
#
# def check_permission(user_id):
#     def wrapper_permission(func):
#         def wrapped_check():
#             if user_id not in user_ids:
#                 return
#             return func()
#
#         return wrapped_check
#
#     return wrapper_permission
#
#
# @check_permission(123456789)
# def hi_id():
#     return f"привет, твой id 123456789"
#
#
# @check_permission(2222)
# def no_id():
#     return "я не знаю кто ты"
#
#
# print('старт программы')
# print(hi_id())
# print(no_id())
# print('конец программы')

# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
# Какое число является 10001-м простым числом?
def simple_number(num):
    simple = [3]
    number = 3
    count = 3
    while count <= num:
        number += 2
        simpleNuber = True
        for i in simple:
            if number < i ** 2:  # числа кратные i, начинают высчитывать с i(квадрат)
                break
            else:
                if number % i == 0:
                    simpleNuber = False
                    break
        if simpleNuber == True:
            simple.append(number)
            count += 1
    return simple[-1]


print(simple_number(10001))  # 104743
print(simple_number(100))  # 541

# try:
#     print('try')
#     print('до ValueError')
#     1/0
#     print('после ValueError')
# except ZeroDivisionError as e:
#     print(e)
#     print('на ноль делить нельзя')
# # finally:
# #     print('finally')
