L = [1, 2, 3, 4, 5]
for x in L:
    print(x, end='')

print()

L = list(map(lambda x: x ** 2, L))
print(L)