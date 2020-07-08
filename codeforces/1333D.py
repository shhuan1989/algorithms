# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def dfs(N, A):
    pairs = []
    for i in range(N-1):
        if A[i] == 1 and A[i+1] == 0:
            pairs.append((i, i+1))
    
    if not pairs:
        return 0, 0, []
    
    for a, b in pairs:
        A[a] = 0
        A[b] = 1
    
    a, b, c = 1, len(pairs), [pairs]
    d, e, f = dfs(N, A)
    
    return a+d, b+e, c+f


def bfs(N, A):
    a, b, pairs = 0, 0, []
    prep = []
    while True:
        p = []
        if prep:
            for i in prep:
                if i + 1 < N and A[i] == 1 and A[i+1] == 0:
                    p.append(i+1)
        else:
            for i in range(N - 1):
                if A[i] == 1 and A[i + 1] == 0:
                    p.append(i+1)
        if not p:
            break
        
        for j in p:
            A[j-1] = 0
            A[j] = 1
        b += len(p)
        a += 1
        pairs += [list(sorted(p))]
        
        changes = set()
        for i in p:
            if i-2 >= 0:
                changes.add(i-2)
            changes.add(i)
        prep = list(sorted(changes))
    
    return a, b, pairs
    
    
def solve(N, K, A):
    a, b, c = bfs(N, A)
    
    # print(a, b, c)
    if K < a or K > b:
        print(-1)
        return
    
    ans = []
    
    used = 0
    for ci, pairs in enumerate(c):
        rest = b - used
        if rest == K:
            for ps in c[ci:]:
                ans += [[p] for p in ps]
            break
        else:
            right = rest - len(pairs)
            # curr >= K - right
            curr = max(1, K-right)
            curr = min(len(pairs), curr)
            ans += [[p] for p in pairs[:curr - 1]]
            ans += [pairs[curr - 1:]]
            K -= curr
                    
        used += len(pairs)
    # print(ans)
    print('\n'.join(['{} {}'.format(len(pairs), ' '.join(map(str, pairs))) for pairs in ans]))
    

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [0 if v == 'L' else 1 for v in input()]
    # A = list(input())
    solve(N, K, A)