a = [1, 4, 5, 8, 34, 56, 200]
a.append(300)

print(a)

a.reverse()

print(a)

a.insert(3, -2000)

print(a)

a.remove(56)

print(a)

a.pop()

print(a)

a.pop(3)

print(a)

c = a.copy()

print(id(c))
print(id(a))
c.sort(reverse=True)
print(c)
c.sort()
print(c)
