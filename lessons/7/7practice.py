# a = [1, 2, 3, 'a', True]
# for i in a:
#     print(i)
#
# a = [1, 2, 3, 'a', True]
# for i in range(len(a)):
#     print(a[i])
#
# print(a)

# a = [1, 2, 3, 'a', True]
# print(*a)  # распаковка списка(выводит без квадратных скобок)

# languages = 'Python C# Java'.split()
# print(languages)  # ['Python', 'C#', 'Java']
#
# numbers = '1 2 3 4 5'.split()
# print(numbers)    # ['1', '2', '3', '4', '5']

# words = 'To    be or not    to   be that is the     question'.split()
# print(words)      # ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']

# ip = '192.168.1.1'.split('.')
# print(ip)  # ['192', '168', '1', '1']
# #
# terms = '1 + 2 + 3 + 4 = 10'.split(' + ')
# print(terms)  # ['1', '2', '3', '4 = 10']

# ip = '192.168.1.1'.split(' ')
# print(ip)

# words = 'To    be or not    to   be that is the     question'.split(' ')
# print(words)  # ['To', '', '', '', 'be', 'or', 'not', '', '', '', 'to', '', '', 'be', 'that', 'is', 'the', '', '', '', '', 'question']

# languages = ' '.join(['Python', 'C#', 'Java'])
# print(languages)  # 'Python C# Java'
#
# numbers = ' '.join(['1', '2', '3', '4', '5'])
# print(numbers)  # '1 2 3 4 5'
# #
# words = '   '.join(['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'])
# print(words)  # 'To   be   or   not   to   be   that   is   the   question'
# #
# ip = '.'.join(['192', '168', '1', '1'])
# print(ip)  # '192.168.1.1'
#
# terms = ' + '.join(['1', '2', '3', '4 = 10'])
# print(terms)  # '1 + 2 + 3 + 4 = 10'

# my_list = ['work1', 'work2', 'work3']
# volue = '\n'.join(my_list)
# print(volue)
# print(type(volue))

# my_list = ['work1', False, 'work3']
# volue = ''.join(my_list)
# print(type(volue))

# type()
# type('john')  # <class 'str'>
# type(my_list)  # <class 'list'>


# data = input()
# Ввод: Иван 3Б
# Выход: 3Б

# user_data = input()
# user_list = input().split()
# print(user_list[-1])

# Есть список слов, необходимо составить из него строку через цикл, а также с помощью метода join
# a = ['hello', 'world']
# 'hello world'

# a = ['hello', 'world']
# b = ' '.join(a)
# c = ''
# for letter in a:
#     c += letter
#     if letter != a[-1]:
#         c += ' '
# print(b)
# print(c)


# a = {ключ: значение}
# a = {'key': 'value'}
# print(a)
# a = {}
# a = dict()
# print(a)
# print(type(a))

# a = {'a': 1, 'b': 2}
# print(a['a'])
# print(a['b'])

# a = dict([(1, 2), [4, 5]])
# print(a)  # {1: 2, 4: 5}

# a = {'a': 1}
# a['a'] = 4
# a['b'] = 2
# print(a)

# a = {2: 1}
# print(a)
# a.clear()
# print(a)

# a = {2: 1}
# b = a
# a['2'] = '22'
# print(b)

# a = {2: 1}
# b = a.copy()   # создаем копию
# a['2'] = '22'
# print(b)


# a = {2: 1}
# # a["3"]  # KeyError
# # print(a.get(3))  # None
# print(a.get(2, 3))
# print(a.get(1, 3))


# value1 = 1
# value2 = 2
# value3 = 3

# value1, value2, value3 = 1, 2, 3
# print(value1, value2, value3)

# a = {2: 1, 'a': 4}
# print(a.items())  # dict_items([(2, 1), ('a', 4)])
# for data in a.items():
#     kye, value = data
#     print(kye, value)
# for key, value in a.items():
#     print(f'{key=}, {value=}')

# a = {2: 1, 'a': 4}
# print(a.keys())
# for key in a.keys():
#     print(key)
#
# a = {2: 1, 'a': 2}
# print(a.values())


# a = {2: 1, 'a': 4}
# b = a.pop('a')
# print(b)
# print(a)

# a = {2: 1, 'a': 4}
# b = a.popitem()
# print(b)
# print(a)

#
# a = {2: 1, 'a': 4}
# d = a.setdefault(3, '3')
# print(d)
# print(a)

# a = {2: 1}
# a.update({'a': 2})
# print(a)

# a = {2: 1, 'a': 4, 'qwe': 'eee'}
# print(a)
# # for i in a:
# #     print(i)
#
# keys = a.keys()
#
# print(type(keys))
# keys = list(keys)
# keys[0] = 22
# print(type(keys))

# a = {1, 2, 3, 2, 3}
# print(a)
# a = set()
# print(a)

# a = {1, 2, 3, 2, 3, ['12']}
# print(a)


# set1 = {1, 3, 4}
# set1.add(2)
# set1.add(2)
# set1.add(2)
# print(set1)

# set2 = {1, 2, 3}
# set2.update([4, 5, 6])
# print(set2)  #  {1, 2, 3, 4, 5, 6}

# set1 = {1, 2, 3, 4, 'a', 'p'}
# set1.remove(2)
# print(set1)
# set1.remove(2)
# print(set1)

# set1 = {1, 3, 4, 'a', 'p'}
# set1.discard('a')
# print(set1)
# set1.discard('a')
# print(set1)

# set1 = {1, 3, 4, 'p'}
# d = set1.pop()
# print(d)
# print(set1)

# list1 = [1, 2, 1, 3]
# list1 = set(list1)
# print(list1)
# list1 = list(list1)
# print(list1)
#
# list1 = [1, 2, 1, 3]
# list1 = list(set(list1))
# print(list1)


# a = {
#     2: [1, 2, 3, False, [2, 3]],
#     'a': {
#         'name': 'john',
#         'age': 22,
#         'job': 'programer'
#     }
# }
#
# print(a[2][-1][1])
# print(a['a'].get('job', 'no job'))
#
# a['new key'] = {
#     'a': {
#         'a1': {
#             'a2': False
#         }
#     }
# }
# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())


dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
# Напишите программу для слияния нескольких словарей в один.
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)
