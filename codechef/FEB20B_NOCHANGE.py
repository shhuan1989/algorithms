# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def gcd(x, y):
    while y:
        x, y = y, x%y
    
    return x



def brutal(N, P, D):
    
    
    def dfs(index, curr, coef):
        if index >= N:
            
            s = sum([D[i] * coef[i] for i in range(N)])
            # print(s, coef)
            if s > P and all([s-D[i] < P for i in range(N) if coef[i] > 0]):
                return True, coef
            
            return False, []
        
        if index == N-1:
            coef[index] = curr//D[index] + 1
            d, e = dfs(index+1, 0, coef)
            return d, e
        
        for c in range(curr//D[index] + 2):
            coef[index] = c
            d, e = dfs(index+1, curr-c*D[index], coef)
            if d:
                return d, e
        
        return False, []
    
    
    a, b = dfs(0, P, [0 for _ in range(N)])
    if a:
        return 'YES {}'.format(' '.join(map(str, b)))
    
    return 'NO'
    


def solve(N, P, D):
    ans = [0 for _ in range(N)]
    for i, v in enumerate(D):
        if P % v != 0:
            ans[i] = P // v + 1
            return 'YES {}'.format(' '.join(map(str, ans)))
    
    for i in range(N):
        for j in range(i+1, N):
            a, b = D[i], D[j]
            if a > b:
                ca = max(1, P // a - 1)
                cb = max(1, (P-ca * a) // b + 1)
            else:
                cb = max(1, P // b - 1)
                ca = max(1, (P-cb*b)//a + 1)
                
            if ca * a + cb * b > P and (ca-1) * a + cb * b < P and ca * a + (cb-1) * b < P:
                ans[i] = ca
                ans[j] = cb

                return 'YES {}'.format(' '.join(map(str, ans)))

    return 'NO'


# import random
# for i in range(1000):
#     N = random.randint(1, 5)
#     P = random.randint(1, 22)
#     D = [random.randint(1, 10) for _ in range(N)]
#     D.sort()
#
#     sa = brutal(N, P, D)
#     sb = solve(N, P, D)
#     if sa == 'NO' or sb == 'NO':
#         if sa != sb:
#             print(N, P)
#             print(' '.join(map(str, D)))
#             print('=' * 40)
#             print(sa)
#             print(sb)
#             exit(0)
    




T = int(input())
ans = []
for ti in range(T):
    N, P = map(int, input().split())
    D = [int(x) for x in input().split()]
    ans.append(solve(N, P, D))
    
print('\n'.join(ans))