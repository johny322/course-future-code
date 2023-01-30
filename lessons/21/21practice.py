# def func(n):
#     print(n)
#     if n < 10:
#         func(n + 1)
#
#
# func(4)

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

# __next__

# a = 'hello'
# iterator = iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# tuple1 = ("яблоко", "банан", "вишня")
# # for i in tuple1:
# #     print(i)
# myit = iter(tuple1)
# print(next(myit))
# print(next(myit))
# print(next(myit))
#
# for i in iter(tuple1):
#     print(i)

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# for i in myclass:
#     print(i)
# myiter = iter(myclass)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
#
# for i in myiter:
#     print(i)


# class MyClass:
#     def __init__(self, start=None, stop=None, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         x = self.start
#         while x < self.stop:
#             yield x
#             x += self.step
#
#
# nums = MyClass(0, 10, 1)
# for x in nums:
#     print(x)


# # Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран
# my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
#
# result = 1
# # for i in my_dictionary.values():
# #     result *= i
# for key in my_dictionary:
#     result = result * my_dictionary[key]
#
# print(result)

# # Создайте словарь из строки 'python.py' следующим образом: в качестве ключей возьмите буквы строки,
# # а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
# word = "python.py"
# result = {char: word.count(char) for char in word}
# # result = {}
# # for char in word:
# #     result[char] = word.count(char)
# print(result)

g = (i for i in range(10))
print(g)
