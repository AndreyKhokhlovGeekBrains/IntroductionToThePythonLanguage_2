# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print("Введите число N: ")
n = int(input())

i, res = 0, 1

while True:
    res = 2**i
    if(res < n):
        print(res, end=', ')
    else:
        break
    i += 1