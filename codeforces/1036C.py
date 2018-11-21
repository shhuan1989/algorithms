# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""

import math

def ncr(n, m):
    pass


def solve(l, r, x):
    if x <= 0:
        return 0
    
    if len(l) < len(r):
        l = '0' * (len(r) - len(l)) + l
        
    ans = 0
    a, b = int(l[0]), int(r[0])
    if x == 3:
        pass
    elif x == 2:
        ans += max(b-a-1, 0) * (len(l)-1) * 9
        if a == b:
            ans += solve(l[1:], r[1:], 1)
        else:
            pass
    elif x == 1:
        ans += max(b-a-1, 0)
        if a != b:
            if all([c == '0' for c in l[1:]]):
                ans += 1
            if all([c == '0' for c in r[1:]]):
                ans += 1
        else:
            if all([c == '0' for c in l[1:]]) and all([c == '0' for c in r[1:]]):
                ans += 1
    
    return ans
    



T = int(input())
for ti in range(T):
    l, r = input().split()
    print(solve(l, r))