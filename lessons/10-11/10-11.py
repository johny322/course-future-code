# file = open('example.txt', 'r')
#
# print(file.read())
# file.close()

# file = open('example.txt', 'a')
# file.write('python')
# file.close()
#
# file = open('example.txt', 'r')
# print(file.read())
# file.close()

# file = open('example.txt', 'w')
# file.write('\npython')
# file.close()
#
# file = open('example.txt', 'r')
# print(file.read())
# file.close()


# file = open('example.txt')
# print(file.read())
# file.close()

# with функция open() as переменная:
#     что-то делаем с переменной переменная

# with open('example.txt', 'r') as my_file1:
#     print(my_file1.read())
#     print()
#
# print('with end')

# f = open('example.txt','r')
# v = f.read(7)  # чтение 7 символов из example.txt
# print(v)
# f.close()

# f = open('example.txt','r')
# print(f.read(7))  # чтение 7 символов из example.txt
# print(f.read(7))  # чтение следующих 7 символов
# f.close()

# x = open('example.txt','r')
# # print(x.readline())  # прочитать первую строку
# # print(x.readlines(2))  # прочитать вторую строку
# print(x.readlines())  # прочитать все строки
# x.close()

# f = open('example2.txt', 'w')  # открытие в режиме записи
# # f.write('Hello \n World')  # запись Hello World в файл
# f.writelines(['hello\n', 'world\n', 'how\n', 'are\n', 'you', '?'])
# f.close()  # закрытие файла


filename = "test.txt"

# # 1. Чтение из файла (в одну строку)
# with open(filename, encoding="utf-8") as file:
#     data = file.read()
#     print(data)
#
# # 2. Чтение из файла (в список)
# with open(filename, encoding="utf-8") as file:
#     data = file.readlines()
#     print(data)
#
# # 3. Чтение из файла (построчно)
# lines = []
# with open(filename, encoding="utf-8") as file:
#     for line in file:
#         lines.append(line.strip())
# print(lines)

# import os
#
# os.rename("example2.txt", "example3.txt")

# import os
#
# file_name = input()
# new_file_name = input()
#
#
# def read_file(file_name, new_file_name):
#     with open(file_name, 'r') as lines:
#         line = lines.readlines()
#     os.rename(file_name, new_file_name)
#     return line
#
#
# print(read_file(file_name, new_file_name))

# import os
#
# os.system('файлы.png')

# import os
#
# os.system('mkdir test')

# with open('1.txt') as file:
#     str1 = file.readlines()
#
# print(str1)

# with open('1.txt') as file:
#     str1 = file.read()
#
# word_list = str1.split()
# result = ','.join(word_list)
# print(result)


# import json
#
# filename = "file.json"
# info = {
#     "ФИО": "Иванов Иван Иванович",
#     "Оценки": {
#         "Математика": 4,
#         "Физика": 5,
#         "Информатика": 5
#     },
#     "Хобби": ["Программирование", "Плавание"],
#     "Возраст": 14,
#     "Играет в футбол": False,
#     "ДомЖивотные": None
# }
# # print(json.dumps(info, ensure_ascii=False, indent=4))
# # # Запись структуры в файл в JSON-формате
# # with open(filename, "w", encoding="utf-8") as file:
# #     file.write(json.dumps(info, ensure_ascii=False, indent=4))
#
# # Чтение из файла JSON-формата
# with open(filename, encoding="utf-8") as file:
#     # print(type(file.read()))
#     info_2 = json.loads(file.read())
#
# print(type(info_2))
# print(info_2['ФИО'])

import csv

filename = "test.csv"

shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}

# Запись в файл
# with open(filename, "w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#     writer.writerow(["Наименование", "Вес", "Цена/кг."])  # Заголовки столбца
#     for name, values in sorted(shop_list.items()):
#         writer.writerow([name, *values])
#     writer.writerow(["мука", "4", "70"])  # Допишем произвольную запись

# # Чтение файла
# with open(filename, "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк
#
# print(rows)
# for row in rows:
#     print(row)

# import csv
#
# filename = "test.csv"
# # список покупок
# shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}
#
# # # Запись в файл
# # with open(filename, "w", encoding="utf-8", newline="") as file:
# #     writer = csv.DictWriter(file, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
# #     writer.writeheader()  # Записывает заголовки в файл
# #     for name, values in sorted(shop_list.items()):
# #         writer.writerow(dict(weight=values[0], name=name, price=values[1]))
#
# # # Чтение файла
# with open(filename, "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк
#     print(rows)
#
# for row in rows:
#     print(row)


# import pickle
#
# filename = "test_pickle.txt"
#
# shop_list = {"овощи": ["картофель", "капуста"],
#              "бакалея": ["мука"],
#              "бюджет": 500}
#
# # # Запись в файл
# # with open(filename, "wb") as file:
# #     pickle.dump(shop_list, file)  # помещаем объект в файл
#
# # Считываем из хранилища
# with open(filename, "rb") as file:
#     shop_list_2 = pickle.load(file)  # загружаем объект из файла
# print(type(shop_list_2))
# print(shop_list_2)


# Написать программу, которая запрашивает у пользователя имя и возраст и записывает в словарь.
# Ввод продолжается до тех пор, пока количество пар(ключ/значение) в словаре не равно 3.
# Если пользователь ввел повторное имя, то программа должна вывести соответствующее сообщение.
# После окончания ввода данные записываются в файл test.txt в формате json.

import json

dict_person = {}
while len(dict_person) != 3:
    name = input('Введите имя: ')
    if name not in dict_person:
        age = input('Введите возраст: ')
        dict_person[name] = age
    else:
        print('Данное имя уже существует')

with open('text.json', "w", encoding="utf-8") as file:
    file.write(json.dumps(dict_person, ensure_ascii=False, indent=4))
