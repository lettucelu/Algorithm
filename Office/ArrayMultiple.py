# /usr/bin/python
# -*- coding:utf-8 -*-


def arrayMultiplied(arrayA, arrayB, arrayC, M, N, P):

    print(arrayA, arrayB, arrayC, M, N, P)


arrayA = [['a11', 'a12', 'a13'], ['a21', 'a22', 'a23'], ['a31', 'a32', 'a33']]
print(arrayA)
arrayB = [['b11', 'b12', 'b13', 'b14'], ['b21', 'b22', 'b23', 'b24'], ['b31', 'b32', 'b33', 'b34'], ['b41', 'b42', 'b43', 'b44']]
print(arrayB)
arrayC = [[None] * 3 for row in range(4)]
print(arrayC)
for x in range(3):
    for y in range(3):
        #print(x, y)

        print("arrayA[%d]arrayA[%d]:%s" %(x, y, arrayA[x][y]))
        print("arrayA[%d]arrayA[%d]:%s" % (x, y, arrayB[x][y]))
        #arrayC[x][y] =

#arrayMultiplied()