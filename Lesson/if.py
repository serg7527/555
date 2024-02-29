x = int(input())

if x % 2 == 0:
    if 0 <= x <= 9:
        print("x - цифра")
    else:
        print("x - число")
else:
    print("x - нечетное число")
    