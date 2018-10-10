# /usr/bin/python
# -*- coding:utf-8 -*-
print("| a1	b1 |")
print("| a2	b2 |")
a1 = raw_input("please input the a1:")
b1 = raw_input("please input the b1:")
a2 = raw_input("please input the a2:")
b2 = raw_input("please input the b2:")
result = int(a1)*int(b2) - int(b1)*int(a2)
print("| %s	%s |") %(a2, b2)
print("行列式值 = %d") %result