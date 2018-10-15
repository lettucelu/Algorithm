# /usr/bin/python
# -*- coding:utf-8 -*-


arrayA = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print(arrayA)

def transpose(n):
    arrayB = [[None] * 3 for row in range(3)]
    print(arrayB)
    for x in range(3):
        for y in range(3):
            arrayB[y][x] = arrayA[x][y]
    print("arrayA 轉置後:" + str(arrayB))


transpose(arrayA)
