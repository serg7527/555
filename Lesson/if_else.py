a = int(input("Введите a:"))
b = int(input("Введите b:"))
с = int(input("Введите c:"))

d = (a if a > с else с) if a > b else (b if b > с else с)

print(d)

# if a > b:
#     if a > с:
#         print("a - max")
#     else:
#         print("c - max")
# else:
#     if b > с:
#         print('b - max')
#     else:
#         print("c -max")