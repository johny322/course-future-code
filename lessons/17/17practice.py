# from calc import add, sub, mul, div
#
#
# class Calculator:
#     def __init__(self) -> None:
#         self.main()
#
#     def main(self):
#         print('Это калькулятор')
#         while True:
#             num1 = int(input('Введите первое число: '))
#             num2 = int(input('Введите второе число: '))
#             choice = int(input('Выберите необходимое действие:\n'
#                                '1: +\n'
#                                '2: -\n'
#                                '3: *\n'
#                                '4: /\n'
#                                '0: Выход\n'))
#             if choice == 0:
#                 input('Для завершения нажмите Enter')
#                 break
#             elif choice == 1:
#                 print(add(num1, num2))
#             elif choice == 2:
#                 print(sub(num1, num2))
#             elif choice == 3:
#                 print(mul(num1, num2))
#             elif choice == 4:
#                 print(div(num1, num2))
#             else:
#                 print('Неверный выбор')
#
#
# if __name__ == '__main__':
#     obj = Calculator()
#     # import calc
#     # print('__name__', calc.__name__)
#     # print('__doc__', calc.__doc__)
#     # print('__dict__', calc.__dict__)
#     # print('__file__', calc.__file__)
#     # print('__package__', calc.__package__)

# __init__.py
# from my_package.subpackage_one.file_one import func_file_one
#
# func_file_one()

# import my_package.subpackage_two.file_two as ft
#
# ft.func_file_two()
# o = ft.MyClass()
#
# import my_package.subpackage_one as so
#
# so.func_file_one()
# # so.func_file_two()

# import my_package_two as mpt

# mpt.number  # ошибка
# mpt.func()

# import my_package_two as mpt
# mpt.test_func()

# import pack.subpack.test_file as pst

# pst.test_func_subpack()

# from pack import pack_file as pf
#
# pf.func_pack_file()


# pip

# n посчитайте n + nn + nnn.
# 3: 3 + 33 + 333 + 3333 + 33333
def my_func(n: int, n_max: int) -> int:
    res = 0
    for i in range(1, n_max+1):
        n_str = str(n) * i
        print(n_str)
        n_res = int(n_str)
        res += n_res
    return res


print(my_func(3, 5))
