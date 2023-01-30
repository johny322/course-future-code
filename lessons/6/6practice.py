# numbers = [2, 4, 6, 8, 10]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
#
# languages = ['Python', 'C#', 'C++', 'Java']

# info = ['Python', 2022, 24.2]
# print(info)
# print(info[0])
# print(info[1])
# print(info[2])

# mylist = []       # пустой список
# mylist = list()   # пустой список
# print(mylist)

# numbers = list(range(5))
# print(numbers)

# even_numbers = list(range(0, 10, 2))
# print(even_numbers)
# odd_numbers = list(range(1, 10, 2))
# print(odd_numbers)

# s = ['hello, world']

# s = 'hello, world'
# name = 'john'
# value = [s, 2, '', name]
# print(value[1], value[-2])
# print(value[0], value[-1])

# print(value)
# s = 'hello, world'
# chars = list(s)
# print(chars)

# valueBool = 3 > 5
# value = [valueBool, 2, '', 3.2222222222]
# # value = [True, 2, '', 3.2222222222]
#
# print(value)

# numbers = [
#     [1, 2, 3, ['1', 2, True]],
#     [4, 5, 6]
# ]
# print(numbers[0][-1][-2])
# value1 = [True, 2, '', 3.2222222222]
# value2 = [['1', 2, True], 2, '', 3.2222222222]
# print(len(value1) == len(value2))

# value1 = [True, 2, '', 3.2222222222]
# print(2 in value1)

# value1 = [['1', 2, True], 2, '', 3.2222222222]
# print(['1', 2, True] in value1)
# print('1' in value1)

# value1 = [True, 2, '', 3.2222222222]
# print(value1[::-1])

# value1 = [True, 2, '', 3.2222222222]
#
# print(value1 * 3)

# value1 = [True, 2, '', 3.2222222222]
# value2 = [False, '2', '', 3.2222222222]
#
# print(value1 + value2)

# my_list = [1, 2, 3, -5, 10, 120]
# print(min(my_list))
# print(max(my_list))
# my_list = [1, 2, 3, -1]
# print(sum(my_list))
# sum_value = 0
# for num in my_list:
#     sum_value += num
# print(sum_value)

# my_list = [1, 2, 3, -5, 10, 120]
# my_list[1] = 20
# my_list[0] = my_list[0] * 3
# my_list[-1] = my_list[0]
#
# print(my_list)

# имя_объекта.метод(параметры)

# a = [1, 2, 3]
# a.append(4)
# a.append(4)
# a.append([1, 2])
# a.append(True)
# print(a)

# a = [1, 2, 3, 2]
# a.remove(2)
# a.remove(2)
# # a.remove('2222')
# print(a)
#
# a = [1, 2, 3]
# value = a.pop(2)
# a.pop(-1)
# print(a, value)

# a = [1, 2, 3]
# a.clear()
# print(a)

# a = [2, 1, 3]
# a.sort()
# a.sort(reverse=True)
# print(a)
# a = ['aaaa', 'bbb', 'bbb', 'aabb', 'BBB', 'Bbb', 'ba', 'b']
# a.sort()
# print(a)

# a = [1, 2, 3]
# b = [3, 5, 6]
# a.extend(b)  # [1, 2, 3, 3, 5, 6]
# # a = a + b  # [1, 2, 3, 3, 5, 6]
# print(a)

# a = [1, 2, 3]
# b = [3, 5, 6]
# a.append(b)
# print(a)

# a = [2, 1, '3']
# print(a.index('3'))

# a = [2, 1, 3]
# a.insert(1, '4')
# print(a)

# a = ()   # для создания пустого кортежа
# a = (2,)  # для создания кортежа из одного элемента
# a = (2, 3, 4)
# # print(a[-1])
# a = list(a)
# # print(a)
# a[-1] = 22
# # print(a)
# a.append(-2)
# a = tuple(a)
# print(a)


# Сформировать возрастающий список из чётных чисел (количество элементов 45)
a = []
i = 0
while len(a) < 45:
    if i % 2 == 0:
        a.append(i)
    i += 1
print(a)
print(len(a))

