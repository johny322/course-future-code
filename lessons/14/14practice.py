# def get_name(name='Иван'):
#     print(name)
#
#
# get_name()
# get_name('Петр')


# class Car:
#     def __init__(self, speed, color='Yellow'):
#         self.speed = speed
#         self.color = color
#
#
# car1 = Car(100)
# car2 = Car(90, 'Blue')
#
# print(f'{car1.color=}')
# print(f'{car2.color=}')

# class Car:
#     def __init__(self, speed, color='Yellow', owner=None):
#         self.speed = speed
#         self.color = color
#         self.owner = owner
#
#     def say_owner(self):
#         if self.owner:
#             print(f'Владелец {self.owner}')
#         else:
#             print('У данного автомобиля нет владельца')
#
#
# # car1 = Car(100, 'green', 'Иван')
# # car2 = Car(90, 'Blue')
# car1 = Car(speed=100, owner='Иван')
# car2 = Car(color='Blue', speed=15)
#
# car1.say_owner()
# car2.say_owner()


# class Person:
#     _age = 15
#
#
# person1 = Person()
# print(person1._age)
# person1._age = 14
# print(person1._age)


# class Person:
#     _age = 15
#     __volue = 0
#
#     def __say_hello(self):
#         print('Привет')
#
#     def say_hello(self):
#         self.__say_hello()
#
#
# person1 = Person()
# # person1.say_hello()
# print(person1._age)
# # print(person1.__volue)
# print(person1._Person__volue)
#
# # person1.__say_hello()
# person1._Person__say_hello()

# class MyClass:
#     def __init__(self, name):
#         self._secret = 'random'
#         self._name = name
#
#     @property
#     def name(self):
#         # self._name += self._secret
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if value:
#             self._name = value
#
#
# m = MyClass('john')
# # print(m._name)
# # m._name = 12
# # print(m._name)
# print(m.name)
# m.name = ''
# print(m.name)
# m.name = 'mike'
# print(m.name)
#
# class Api:
#     def __init__(self):
#         self._site_name = 'http://my.ste.ru/api'
#
#     def buy(self):
#         url = self._site_name + f'/buy'
#         self.make_request(url)
#
#     def make_request(self, url):
#         print(f'Делаю запрос на url {url}')
#
#
# api = Api()
# api.buy()
# api._site_name = 'hoho'
# api.buy()

class Animal:
    def __init__(self, name, breed='без породы'):
        self.name = name
        self.breed = breed

    def __say_breed(self):
        return self.breed

    def say_breed(self):
        print(self.__say_breed())


cat = Animal('Барсик', 'Сибирский')
cat.say_breed()
dog = Animal('Тузик')
dog.say_breed()
