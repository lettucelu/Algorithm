# /usr/bin/python
# -*- coding:utf-8 -*-

#print("尋找最小值")

num = [[ [33, 45, 67], [23, 71, 66], [55, 38, 66] ], [ [21, 9, 15], [38, 69, 18], [90, 101, 89]]]

print(num)

for x in range(2):
	for y in range(3):
		for z in range(3):
			#print("%d") %(num[x][y][z])
			if min >= num[x][y][z]:
				min = num[x][y][z]

print("三維陣列中最小值為：%d") %(min)