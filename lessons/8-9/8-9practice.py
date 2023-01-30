# print('*' * 7)
# print('*' * 7)
# print('*' * 7)
# print('*' * 7)
# print('*' * 7)
# for i in range(3):
#     for _ in range(5):
#         print('*' * 7)
#     print()

# for _ in range(5):
#     print('*' * 7)
# new_param = 5
# new_param += 1
# print(new_param)
#
# for _ in range(5):
#     print('*' * 7)

# def название_функции():
#     блок кода

# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
#
#
# draw_box()
# print()
# new_param = 5
# new_param += 1
# draw_box()
# print()
# draw_box()

# def printMessage12():
#     print('Hello')
#     print('my name is john')
#
#
# printMessage12()

# def название_функции(параметры):
#     блок кода
#
# название_функции(параметры)

# def my_print(message):
#     print(message)
#
#
# my_print('rtrt')

# def draw_box(height, width):  # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
#
#
# # draw_box(5, 7)
# # print()
# # draw_box(2, 4)
# # print()
# # draw_box(3, 3)
# # draw_box(height=10, width=3)
# # draw_box(width=3, height=10)
# h = 10
# w = 3
# draw_box(h, w)
# /
# def myFunc(param1, param2, param3, param4=4):
#     print(param1, param2, param3, param4)


# myFunc(1, 2, 3, 44)


# myFunc(1, param3=3, param2=2, param4=44)


# Написать функцию, которая принимает стороны прямоугольника и выводит периметр и площадь прямоугольника
# def func1(side1, side2):
#     area = side1 * side2
#     perimetr = (side1 + side2) * 2
#     print(area, perimetr)
#
#
# side1 = int(input())
# side2 = int(input())
# func1(side1, side2)


# def func2():
#     side1 = int(input())
#     side2 = int(input())
#     area = side1 * side2
#     perimetr = (side1 + side2) * 2
#     print(area, perimetr)
#
#
# func2()


# x = 5
#
#
# def func():
#     print(x)
#
#
# func()


# x = 5
#
#
# def func():
#     global x
#     x += 1
#
#
# func()
# print(x)

# def func():
#     x = 5
#
#
# func()
# print(x)  # NameError: name 'x' is not defined

# value = len('1231')
# def func():
#     x = 5
#     x += 10
#     return x
#
#
# result = func()
# print(result)

# def func():
#     x = 5
#     y = 10
#     # return 5, 10
#     return x, y
#
#
# value = func()
# print(value)
# result1, result2 = func()
# print(result1, result2)

# def func():
#     for i in range(10):
#         print(i)
#         if i == 4:
#             return i
#
#
# value = func()
# print(f'{value=}')

# None
# def func():
#
#     for i in range(10):
#         print(i)
#         if i == 4:
#             return
#
#
# value = func()
# print(f'{value=}')

# def func():
#     x = 5
#
#
# value = func()
# print(f'{value=}')

# def func(a):
#     if a == 1:
#         return True
#     return False
#
#
# value = func(1)
# print(f'{value=}')

# result = lambda x: x + 5
# print(result(4))

# result = lambda x, y: x + y
# print(result(4, 5))

# my_list = [1, 3, 22, 1312, -1]
# my_list.sort(key=lambda x: x % 2 == 0)
# # my_list.sort(key=lambda x: x > 100)
#
# print(my_list)

# def func():
#     value = {2, 3}
#     return value

# Написать программу, которая принимает от пользователя год и возвращает високосный год или нет.
# Високосный год - год, который кратен 4, но не кратен 100 или кратен 400

def get_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    return False


value = get_year(2000)
if value:
    print('Високосный')
else:
    print('Обычный')
