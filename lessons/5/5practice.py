# word = 'hello'
# for char in word:
#     print(char)


# word = 'hello'
# print(word + ' hello' + 'hi')

# word = 'hello'
# print(len(word))


# word = 'hello my name is john'
# if ' ' in word:
#     print('Yes')

# print('hello' * 3)

# word = 'hello'
# print(word[0])
# s = 'Python'
# print(s[-3])
# print(s[-2])
# print(s[len(s)])
# print(s[-1])


# s = 'abcdefg'
# print(s[0] + s[2] + s[4] + s[6])

# s = 'abcdefg'
# print(s[0] * 3 + s[-1] * 3 + s[3] * 2 + s[3] * 2)


# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i])
#
# print()
#
# s = 'abcdef'
# for value in s:
#     value += '!'
#     print(value)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')
# s = 'abcdef'
# print(s[3:])

# s = 'abcdefghij'
# print(s[-9:-4])
# print(s[-3:])
# print(s[:-3])

# s = 'abcdefghij'
# print(s[1:7:3])

# s = 'abcdefghij'
# print(s[-1:-11:-1])
# print(s[::-2])

# age = 15
# name = 'Иван'
# print(f'Привет меня зовут {name}, мне {24} лет')

# имя_объекта.имя_метода(параметры)
# функция(параметры)

# word = 'hello world'
# print(word.capitalize())

# word = 'hello wOrld'
# print(word.swapcase())

# word = 'hello world ddd'
# print(word.title())

# word = 'HELLO world'
# lower_word = word.lower()
# print(lower_word)
# print(word)

# word = 'HELLO world'
# print(word.upper())
# 'name'
# 'NAME'

# word = 'hello world'
# print(word.count('wll'))


# word = 'hello world'
# print(word.startswith('held'))

# word = 'hello world!'
# print(word.endswith('.'))

# word = 'hello world'
# print(word.find('o'))

# word = 'hello world'
# print(word.rfind('o'))

# word = 'hello world'
# print(word.index('o'))

# word = '   hello world   \n\t'
# word = word.strip().replace('l', '').replace(' ', '')
# print(word)

# word = 'hello world'
# print(word.replace('l', ''))

# name = input()
# last_name = input()
# correct_name = 'Иван'
# correct_last_name = 'Иванов'

# name = input()
# last_name = input()
# correct_name = 'иван'
# correct_last_name = 'иванов'
# if name == correct_name:
#     print('пользователь найден')
# else:
#     print('пользователь не найден')


name = input()
last_name = input()
correct_name = 'иван'
correct_last_name = 'иванов'
if name.lower() == correct_name and last_name.lower() == correct_last_name:
    print(f'Привет {name.title()} {last_name.title()}')
else:
    print('Вы кто такие? Я вас не звал!')
