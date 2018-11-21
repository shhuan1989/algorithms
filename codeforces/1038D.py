# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""


N = int(input())
A = [int(x) for x in input().split()]
B = [abs(x) for x in A]

if N == 1:
    print(A[0])
    exit(0)

s = sum(B)

if any(x >= 0 for x in A) and any(x <= 0 for x in A):
    print(s)
else:
    print(s - 2*min(B))