# /usr/bin/python
# -*- coding:utf-8 -*-


def arrayMultiplied(arrayA, arrayB, arrayC, M, N, P):

    #print(arrayA, arrayB, arrayC, M, N, P)
    return arrayC

arrayA = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print("arrayA:" + str(arrayA))
arrayB = [[2, 4], [6, 8], [10, 12]]
print("arrayB:" + str(arrayB))
arrayC = [[0] * 2 for row in range(3)]
temp = 0
print("arrayC:" + str(arrayC))
M = 3
N = 3
P = 2
for x in range(3):
    for z in range(2):
        #print(z)
        temp = 0
        for y in range(3):
            temp = temp + int(arrayA[x][y]) * int(arrayB[y][z])
        arrayC[x][z] = temp
        #print(arrayC[x][z])
print(arrayC)

arrayMultiplied(arrayA, arrayB, arrayC, M, N, P)