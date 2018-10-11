# /usr/bin/python
# -*- coding:utf-8 -*-

a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print(a)

b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(b)

c = [ [None] * 3 for row in range(3)]
print(c)

for x in range(3):
    for y in range(3):
        c[x][y] = a[x][y] + b[x][y]
        print(c[x][y])
print(c)