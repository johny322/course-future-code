__all__ = ['func', 'MyClass']

number = 35  # Не экспортируется


def func():  # Экспортируется
    print('Hello')


class MyClass:  # Экспортируется
    pass
