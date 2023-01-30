# class MyClass:
#     def __init__(self, my_param):
#         self.my_param = my_param
#
#     def my_method(self):
#         print('my_method')
#
#
# my_class = MyClass('123')
# print(my_class.my_param)
# my_class.my_method()
#
# my_class1 = MyClass('12')

class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def beep(self):
        print(f'beep {self.color}')


class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner

    def beep(self):
        print('beeeeeeeeeeeep')

    def say_owner(self):
        print('hi ' + self.owner)


class Bus(Transport):
    def __init__(self, speed, color, seeds):
        super().__init__(speed, color)
        self.seeds = seeds

    def say_seeds(self):
        print(f'Мест: {self.seeds}')

    def beep(self):
        print('beeeeeep beep beep')
        super().beep()
        print('beeeeeep beep beep')


class SportCar(Car, Transport):
    pass


# transport = Transport(61, 'black1')
# transport.beep()
#
# car = Car(60, 'black', 'john')
# print(car.owner)
# car.beep()
# car.say_owner()

# bus = Bus(45, 'white', 23)
# print(bus.speed)
# print(bus.seeds)
# bus.beep()
# bus.say_seeds()


# sport_car = SportCar(54, 'white', 'john')
# sport_car.beep()


# sport_car.say_owner()

# Написать родительский человека и дочерний класс ученика.
# class Chelovek:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_name(self):
#         print(self.name)
#
#     def print_age(self):
#         print(self.age, 'лет')
#
#
# class Uchenik(Chelovek):
#     def __init__(self, name, age, _school, _class):
#         super().__init__(name, age)
#         self._school = _school
#         self._class = _class
#
#     def print_school(self):
#         print(self._school)
#
#     def print_class(self):
#         print(self._class)
#
#
# a = Uchenik('Даниил', 1000, 'школа №...', 'класс ...')
# a.print_name()
# a.print_age()
# a.print_school()
# a.print_class()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def name(self):
#         print(f'Меня зовут {self.name}')
#
#
# class Student(Person):
#     def __init__(self, name, age, class1):
#         super().__init__(name, age)
#         self.class1 = class1
#
#     def say_class1(self):
#         print(self.class1)
#
#
# s = Student('john', 12, '6А')
# print(s.name)
# s.say_class1()

# class Human:
#     def __init__(self, age, name, surname):
#         self.age = age
#         self.name = name
#         self.surname = surname
#
#     def read(self):
#         print("Читаю")
#
#
# class Student(Human):
#     def __init__(self, age, name, surname, school):
#         super().__init__(age, name, surname)
#         self.school = school
#
#     def study(self):
#         print("Сижу на уроке")
#
#
# s = Student(12, 'john', 'smith', 12)
# s.read()
# s.study()

# class Person:
#     def __init__(self, name, lname, age):
#         self.name = name
#         self.lname = lname
#         self.age = age
#
#     def say_name(self):
#         print(f'Привет меня зовут {self.lname} {self.name}')
#
#     def say_age(self):
#         print(f'Мой возраст {self.age}')
#
#
# class Student(Person):
#     def __init__(self, name, lname, age, class_num):
#         super().__init__(name, lname, age)
#         self.class_num = class_num
#
#     def say_class_num(self):
#         print(f'Я учюсь в {self.class_num} классе')
#
#
# student1 = Student('Иван', 'Петров', 14, 9)
# student1.say_class_num()
