# circle = [-2, 3, 10]
#
#
# def func():
#     pass
#
#
# class Test:
#     pass
#
#
# print(type(5))
# print(type('a'))
# print(type(5.5))
# print(type(True))
# print(type([1, 2]))
# print(type((5, 4)))
# print(type({1, 2}))
# print(type({'a': 2}))
# print(type(Test))
# print(type(func))

# class Person:
#     name = 'Иван'
#     age = 12
#
#     def say(self):
#         print('Hello')


# person1 = Person()
# print(person1.name)
# person1.say()

# person2 = Person()
# print(person2.name)
# person2.name = 'Василий'
# print(person2.name)

# class Person:
#     # Инициализирующий метод (специальный метод с __)
#     def __init__(self):
#         print('Метод init')
#
#
# person1 = Person()

# class Person:
#     person_type = 'human'
#
#     def __init__(self, name1, age):
#         self.name = name1
#         self.age = age
#         print(f'отработал метод __init__ c {name1=}, {age=}')
#
#     def __str__(self):
#         print(f'{self.age=}')
#         return f'Меня зовут {self.name}'
#
#     def say(self):
#         print('Hello')
#
#
# person1 = Person('Иван', 15)
# person2 = Person('Петр', 14)
# # print(person1.name)
# # print(person1.age)
# # print(person1.person_type)
# # print(person2.name)
# # print(person2.age)
# # print(person2.person_type)
#
# print(person1)
# print(person2)

# Написать класс ученика класса.
# Описать в классе все возможные свойства, которые можно обобщить для каждого ученика,
# а также создать несколько методов.

class Person:
    school_num = 20

    def __init__(self, name, surname, age, num_class):
        self.name = name
        self.surname = surname
        self.fullname = f'{name} {surname}'
        self.age = age
        self.num_class = num_class

    def do_hw(self):
        print('Делаю дз...')

    def read_book(self):
        print(f'Я, {self.name}, сейчас читаю книгу')

    def __str__(self):
        return f'Меня зовут {self.fullname}. Я учусь в {self.num_class} классе, в {self.school_num} школе.'


person1 = Person('Иван', 'Иванов', 10, 3)
person2 = Person('Макс', 'Семенов', 17, 10)
print(person1)
print(person2)
person1.do_hw()
person2.read_book()
