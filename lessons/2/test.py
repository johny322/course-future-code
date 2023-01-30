x = 35
length = len(str(x))
max_val = 10 ** (length - 1)
print(x // max_val)
max_val = int(max_val / 10)
while max_val >= 10:
    print(x // max_val % 10)
    max_val = int(max_val / 10)
print(x % 10)