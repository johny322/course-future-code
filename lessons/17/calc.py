def add(num1: float, num2: float) -> float:
    return num1 + num2


def sub(num1: float, num2: float) -> float:
    return num1 - num2


def mul(num1: float, num2: float) -> float:
    return num1 * num2


def div(num1: float, num2: float) -> float:
    if num2 == 0:
        return 'На ноль делить нельзя'
    return num1 / num2


if __name__ == '__main__':
    print('Я запущен как самостоятельная программа')
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    choice = int(input('Выберите необходимое действие:\n'
                       '1: +\n'
                       '2: -\n'
                       '3: *\n'
                       '4: /\n'))
    if choice == 1:
        print(add(num1, num2))
    elif choice == 2:
        print(sub(num1, num2))
    elif choice == 3:
        print(mul(num1, num2))
    elif choice == 4:
        print(div(num1, num2))
    else:
        print('Неверный выбор')
