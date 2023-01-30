# import random
#
# print(random.randint(1, 10))

# import random as my_random
#
# print(my_random.randint(1, 10))

# from random import randint, choice
#
# print(randint(1, 10))
# # print(choice([1, 2, 'asd']))

# from random import randint as rint, choice as ch
#
#
# def randint():
#     pass
#
#
# print(rint(1, 10))

# from model1 import func as model1_func
# from model2 import func as model2_func

# from random import randint as rint
#
#
# def randint(a, b):
#     return (a, b)
#
#
# print(randint(1, 10))
# print(rint(1, 10))

# from math import pi
#
# print(pi)

# from module import *

# from test_one import *
#
# print(func())
# obj = MyClass()
# # print(number)  # ошибка


# import random
#
# a = [1, 2, 3, 4, '32423', False]
#
# # index = random.randint(0, len(a) - 1)
# # rand_element = a[index]
# # print(rand_element)
#
# print(random.choice(a))


# def testf(param: str) -> str:
#     return param
#
#
# a = testf('strddd')

from calc import add, sub, mul, div


class Calculator:
    def __init__(self) -> None:
        self.main()

    def main(self):
        print('Это калькулятор')
        while True:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            choice = int(input('Выберите необходимое действие:\n'
                               '1: +\n'
                               '2: -\n'
                               '3: *\n'
                               '4: /\n'
                               '0: Выход\n'))
            if choice == 0:
                input('Для завершения нажмите Enter')
                break
            elif choice == 1:
                print(add(num1, num2))
            elif choice == 2:
                print(sub(num1, num2))
            elif choice == 3:
                print(mul(num1, num2))
            elif choice == 4:
                print(div(num1, num2))
            else:
                print('Неверный выбор')


obj = Calculator()
