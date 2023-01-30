# for название переменной in range(количество повторений):
#     блок кода
# for i in range(5):
#     print('hi')

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')


# for number in range(10):
#     print(number + 1)

# range(начало, конец,  шаг)

# word = input()
# for char in word:
#     print(char)

# word = input()
# for i in range(len(word)):
#     print(word[i])

# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована;
# for i in range(1, 6):
#     print(str(i) + ' 0')

# Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
# sum = 0
# for i in range(14 + 1):
#     # print(i)
#     sum += i
#     # sum = sum + i
#
# print('sum:', sum)


# while условие:
#     блок кода
# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# while True:
#     num = int(input())
#     if num == 0:
#         break

# result = 0
# for i in range(3):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# n = int(input())
# flag = False
# n_copy = n
# while n_copy != 0:
#     last_digit = n_copy % 10
#     if last_digit == 7:
#         flag = True
#         break
#     n_copy //= 10
#     # n_copy = n_copy // 10
# if flag == True:
#     print('Число', n, 'содержит цифру 7')
# else:
#     print('Число', n, 'не содержит цифру 7')


# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# for i in range(1, 101):
#     if i != 7 and i != 17 and i != 29 and i != 78:
#         print(i)

# a = 10
# while a < 5:
#     print('условие верно')
#     a = a + 1
# else:
#     print('условие неверно')

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)


# for i in range(3):
#     print('i', i)
#     for j in range(4):
#         print('j', j)
#         if i == j:
#             break
#         print(i, j)

# flag = False
# for i in range(3):
#     for j in range(3):
#         if (j == 1) and (i == 2):
#             flag = True
#             break
#         print(i, j)
#     if flag == True:
#         break

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, ]
for x in numbers:
    if x == 237:
        break
    elif x % 2 == 0:
        print(x)
