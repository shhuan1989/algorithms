# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/5/18

"""

import collections

def solve(N, A):
    vidx = collections.defaultdict(set)
    vs = set()
    for i, v in enumerate(A):
        if i > 0 and 1 <= v <= N:
            vidx[v].add(i)
            vs.add(v)
    
    for ai in A[1:]:
        if 0 <= ai < N:
            for aj in vidx[A[ai]] & vs:
                if ai != aj:
                    return True
    
    return False


T = int(input())
for ti in range(T):
    N = int(input())
    A = [0] + [int(x) for x in input().split()]
    if solve(N, A):
        print('Truly Happy')
    else:
        print('Poor Chef')