# numbers = [1, 2, 3, 4]
# result = (x * x for x in numbers)
# print(result)

# for num in result:
#     print(num)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result, 100))
# print(next(result, 101))

# __next__()

# print(result.__next__())

# numbers = [1, 2, 3, 4]
# result = (x * x for x in numbers)
# print(result)
# print(list(result))

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# for num in result:
#     print(num)


# f = open('test.txt')
# lines = (t.strip() for t in f)
# comments = (t for t in lines if t[0] == '#')
# for c in comments:
#     print(c)
#
# comment_list = list(comments)


# def func(num):
#     while num > 0:
#         # print('pre yield')
#         yield num
#         # print('under yield')
#         num -= 1


# for num in func(5):
#     print(num)

# result = func(5)
# print(result)
# print(next(result))
# print(next(result))
# print(result.__next__())

# for num in func(5):
#     print(num)
#
# # или например
# a = sum(func(5))
# print(a)

# def func(num):
#     while num > 0:
#         # print('pre yield')
#         yield num
#         # print('under yield')
#         num -= 1
#         yield num
#         # print('under under yield')
#
#
# result = func(5)
# print(result)
# print('next', next(result))
# # print(next(result))
# # print(next(result))
#
# for i in result:
#     print(f'{i=}')
#     if i == 3:
#         break
#
# for j in result:
#     print(f'{j=}')

# 1, 1, 2(1 + 1), 3(2+1), 5(3+2), 8(5+3)...
def fib(n):
    fib0 = 1
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n - 2):
        # 1 вариант (надо больше переменных)
        # fib0_old = fib0
        # fib0 = fib1
        # fib1 = fib0_old + fib1
        # 2 вариант
        fib0, fib1 = fib1, fib0 + fib1
        yield fib1


for num in fib(10):
    print(num)
# l = list(fib(10000))
# print(l)
