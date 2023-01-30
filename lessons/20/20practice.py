# class MyClass:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#
#
# obj = MyClass(5)
# for n in obj.__iter__():
#     print(n)
#
# print(next(obj.__iter__()))
# print(next(obj.__iter__()))
# print(next(obj.__iter__()))

# def it():
#     yield 1
#
#
# print(it())

# def gen1(stop):
#     n = 1
#     while n <= stop:
#         yield n
#         n += 1
#
#
# def gen2(start):
#     n = start
#     while n > 0:
#         yield n
#         n -= 1
#
#
# def func(n):
#     yield from gen1(n)
#     yield from gen2(n)
#
#
# # def func(n):
# #     for x in gen1(n):
# #         yield x
# #     for x in gen2(n):
# #         yield x
#
#
# for n in func(5):
#     print(n)

# numbers = [1, 2, [3, [4, 5], 6, 7], 8]
#
#
# # for i in numbers:
# #     print(i)
#
# def func(n):
#     for i in n:
#         if isinstance(i, list):
#             yield from func(i)
#             # for el in func(i):
#             #     yield el
#         else:
#             yield i
#
#
# for i in func(numbers):
#     print(i, end=' ')


# def func():
#     print('Hello')
#     while True:
#         n = yield
#         print(f'Hi {n}')


# r = func()
# r.send(None)
# r.send(1)
# r.send(2)
# r.send(6)

# r = func()
# r.send(None)
# r.send(1)
# r.close()
# r.send(2)

# r = func()
# r.throw(RuntimeError, "Ошибка")

# def func():
#     data = bytearray()
#     line = None
#     linecount = 0
#     while True:
#         part = yield line
#         linecount += part.count(b'\n')
#         data.extend(part)
#         if linecount > 0:
#             index = data.index(b'\n')
#             line = bytes(data[:index + 1])
#             data = data[index + 1:]
#             linecount -= 1
#         else:
#             line = None
#
#
# r = func()
# print(r.send(None))
# print(r.send(b'hello'))
# print(r.send(b'world\nit '))
# print(r.send(b'works!'))
# print(r.send(b'\n'))
#
#
# class MyClass:
#     def __init__(self):
#         self.data = bytearray()
#         self.linecount = 0
#
#     def send(self, part):
#         self.linecount += part.count(b'\n')
#         self.data.extend(part)
#         if self.linecount > 0:
#             index = self.data.index(b'\n')
#             line = bytes(self.data[:index + 1])
#             self.data = self.data[index + 1:]
#             self.linecount -= 1
#             return line
#         else:
#             return None


# # tuple
# # Написать генератор кортежа чисел от 5 до 25 включительно.
# # Вывести весь кортеж, первое число, последнее число и последние 5 чисел
# my_list = tuple([i for i in range(5, 26)])
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(my_list[-1:-6:-1])
# print(my_list[-6:-1])
# print(my_list[-5:])

def f(a: int) -> int:
    pass


# Написать программу, которая считываем числа с консоли через запятую и выводит только
# числа кратные 3 или 5 через запятую в одну строку

s = [int(i) for i in input().split(',') if int(i) % 3 == 0 or int(i) % 5 == 0]
print(s)
# print(list(map(int, s)))
# s = []
# # inp = input()
# # inp = inp.split(',')
# for i in input().split(','):
#     # print(i)
#     if int(i) % 3 == 0 or int(i) % 5 == 0:
#         s.append(i)
# print(s)
