# /usr/bin/python
# -*- coding:utf-8 -*-

import random

global top
top = -1
k = 0

card = [ None ] * 52
card_new = [ None ] * 52
stack = [ 0 ] * 52

print(card)
print(card_new)
print(stack)

for i in range(52):
    card[i] = i + 1
    print(card)

def pop(stack):
    if top < 0:
        print("堆疊為空")
    else:
        top = top - 1
        return stack[top]

def shuffle(old):
    result = []
    while old:
        print("還有幾張未洗牌: %d" %len(old))
        p = random.randrange(0, len(old))
        print("P: %d" %p)
        result.append(old[p])
        old.pop(p)
        print("洗過牌的牌堆: %s" %result)
        print("未洗牌的牌堆: %s" %old)
    return result
def push(stack, Max, val):
    if top <= Max - 1:
        print("堆疊已滿")
    else:
        top = top + 1
        stack[top] = val

card_new = shuffle(card)
print("洗完牌的牌堆: %s" %card_new)

i = 51
print("東\t西\t南\t北\t")
for i in range(51, -1, -1):
    if card_new[i] % 4 == 0:
        style = "♠"
    elif card_new[i] % 4 ==1:
        style = "♥"
    elif card_new[i] % 4 ==2:
        style = "♦"
    elif card_new[i] % 4 ==3:
        style = "♣"

    print("%s%d\t" %(style, card_new[i]%13 + 1), end='')
    if  i % 4 == 0:
        print()
