# /usr/bin/python
# -*- coding:utf-8 -*-

n = int(input("請輸入要計算的階乘 n="))
#print(n)
global sum
sum = 1

for x in range(1, n+1, 1):
    sum = sum * x
    print("%d!=%d" %(x, sum))
