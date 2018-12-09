# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/22/18

"""

import math

a, b = map(int, input().split())

total = a + b


def cal(t):
    # 1+...+n <= t
    
    n = max(0, int(math.sqrt(2*t)) - 1)
    
    while n * (n+1) // 2 <= t:
        n += 1
        
    return n-1

n = cal(total)

swap = False
if a > b:
    swap = True
    a, b = b, a
    
na = cal(a) + 1
ansa = {i for i in range(1, na+1)}
sa = na*(na+1)//2
ansa.discard(sa-a)
ansb = {i for i in range(1, n+1)} - ansa

if swap:
    ansa, ansb = ansb, ansa
    
# print(sum(ansa), sum(ansb), n, max(ansa))
print(len(ansa))
if ansa:
    print(' '.join(map(str, ansa)))
print(len(ansb))
if ansb:
    print(' '.join(map(str, ansb)))
