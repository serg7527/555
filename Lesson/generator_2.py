def get_list():
    for x in [1, 2, 3, 4]:
        yield x


a = get_list()
for x in a:
    print(x)






b = map(int,["1", "2", "3", "4"])

for x in b:
    print(x)



s = list(map(int, input().split()))

print(s)