# через цикл
# list1 = []
# for i in range(1, 11):
#     list1.append(i)
#
# print(list1)

# list1 = [str(i) for i in range(1, 11)]
#
# print(list1)

# [выражение for элемент in последовательность]

# list1 = [val ** 2 for val in range(1, 11)]
#
# print(list1)

# list1 = [1 for i in range(1, 11)]
# print(list1)

# list1 = [float(i) for i in input().split()]
#
# print(list1)

# [выражение for элемент in последовательность if условие]

# list1 = [i for i in range(1, 101) if i % 2 == 0]
#
# print(list1)

# list1 = [(i, j) for i in range(1, 10) for j in [1, 2, 3]]
#
# print(list1)
#
# for i in range(1, 10):
#     for j in [1, 2, 3]:
#         print(i, j)

# list1 = [(i, j) for i in range(1, 10) if i % 2 == 0 for j in [1, 2, 3] if j != 2]
#
# print(list1)

# list1 = [i for i in range(1, 10) if i % 2 != 0]
# print(list1)
#
# tuple1 = tuple([i for i in range(1, 10) if i % 2 != 0])
#
# print(tuple1)
# print(type(tuple1))

# dict1 = {x: x**2 + 1 for x in range(5)}
# print(dict1)

# dict1 = {'h': x for x in range(5)}
# print(dict1)

# dict1 = {x: y for x in 'ABC' for y in 'XYZ'}
# print(dict1)
#
# dict1 = {x: 'Z' for x in 'ABC'}
# print(dict1)
#
# dict1 = {}.fromkeys('ABC', 'Z')
# print(dict1)

# dict1 = {x: y for x, y in [('A', 0), ('B', 1), ('C', 2)]}
#
# print(dict1)

# dict1 = {x: [y for y in range(x, x + 3)] for x in range(4)}
#
# print(dict1)

# dict1 = {x: [y % 2 for y in range(10)] for x in 'ABC'}
# print(dict1)


# dict1 = {'ABCDE'[i]: [i % 2] * 5 for i in range(5)}
# print(dict1)


# dict1 = {x: 1 if x in 'ACE' else 0 for x in 'ABCDEF'}
#
# print(dict1)

# set1 = {i ** 2 for i in range(10)}
# print(set1)

# set1 = {i for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if 'a' not in i}
# print(set1)

# set1 = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if i[1] == 'c'}
# print(set1)

# Написать списковое включение, которое добавляет в список все четные числа, разделенные нацело на 2,
# в диапазоне от 1 до 100
# print([i // 2 for i in range(1, 100) if i % 2 == 0])

# Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
# сформированную из отсортированных в лексикографическом порядке параметров.

# params = {'course': 'python', 'lesson': 2, 'challenge': 17}
# # challenge=17&course=python&lesson=2
# print('&'.join(sorted(f'{k}={v}' for k, v in params.items())))


def query(params):
    return '&'.join(sorted(f'{k}={v}' for k, v in params.items()))


params1 = {'course': 'python', 'lesson': 2, 'challenge': 17}
print(query(params1))
