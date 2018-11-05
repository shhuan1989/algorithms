# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/5/18

"""


TN = [int(x) for x in input().split()]


def gcd(x, y):
    while y:
        x, y = y, x%y
    
    return x

def fold(n):
    la, lb, ra, rb = 0, 1, 1, 1
    
    moveRight = True
    for i in range(n):
        
        a, b = ra*lb-la*rb+2*la*rb, 2*lb*rb
        
        if moveRight:
            ra, rb = a, b
        else:
            la, lb = a, b
        
        moveRight = not moveRight
    
    lc, rc = gcd(lb, la), gcd(rb, ra)
    
    return [la // lc, lb // lc] if moveRight else [ra // rc, rb // rc]

ans = []
for n in TN[1:]:
    ans.extend(fold(n))

print(' '.join(map(str, ans)))