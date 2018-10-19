# /usr/bin/python
# -*- coding:utf-8 -*-


def factorial(n):
    if n == 1 or n == 0:
        #print(n)
        return n
    else:
        result = n * factorial(n-1)
        #print(result)
        return result

while True:
    x = int(input("請決定是否計算階乘結果: 1. 計算階乘 2. 退出程式 => "))

    if x == 1:
        n = int(input("請輸入要計算的階乘: "))
        print(factorial(n))
    else:
        break

