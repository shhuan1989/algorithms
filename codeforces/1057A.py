# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/20/18

"""
import collections

N = int(input())
A = [-1, -1] + [int(x) for x in input().split()]

ans = []
s = N
while s > 0:
    ans.append(s)
    s = A[s]
    
print(' '.join(map(str, reversed(ans))))
