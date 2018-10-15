# /usr/bin/python
# -*- coding:utf-8 -*-


MAXSTACK = 100
global stack
stack = [None] * MAXSTACK
top = -1
print(MAXSTACK)
print(stack)
print(top)


def isEmpty():
    if top == -1:
        return True
    else:
        return False

def push(data):
    global top
    global MAXSTACK
    global stack

    if top >= MAXSTACK -1:
        print("堆疊已滿, 無法再加入")
    else:
        top  += 1
        stack[top] = data

def pop():
    global top
    global stack
    if isEmpty():
        print("堆疊是空")
    else:
        print("彈出的元素為: %d" %stack[top])
        top = top - 1

i = 2
count = 0

while True:
    i = int(input("要推入堆疊, 請輸入 1, 彈出請輸入 0, 停止操作請輸入 -1: "))
    if i == -1:
        break
    elif i == 1:
        value = int(input("請輸入要堆疊的數: "))
        push(value)
    elif i == 0:
        pop()
print("=" * 50)
if top <= 0:
    print("堆疊為空")
else:
    i = top
    while i >= 0:
        print("堆疊彈出的順序為:%d" %stack[i])
        count += 1
        i = i - 1
        print("")
print("=" * 50)



