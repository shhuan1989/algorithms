# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MAXN = 1005
MARK= [-1 for _ in range(MAXN)]

if __name__ == '__main__':
    # sys.stdin = open('p1155.in', 'r')
    N = int(input())
    A = [int(x) for x in input().split()]
    
    minv = [v for v in A]
    for i in range(N-2, -1, -1):
        minv[i] = min(minv[i], minv[i+1])
    
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if A[i] < A[j] and (j+1 < N and minv[j+1] < A[i]):
                # A[i], A[j] can't be put in same stack
                G[i].append(j)
                G[j].append(i)
    
    for i in range(N):
        if MARK[i] < 0:
            MARK[i] = 0
            q = [i]
            while q:
                u = q.pop()
                w = MARK[u] ^ 1
                for v in G[u]:
                    if MARK[v] < 0:
                        MARK[v] = w
                        q.append(v)
                    elif MARK[v] != w:
                        print(0)
                        exit(0)
    
    stacks = [[], []]
    need = [1]
    
    def pop(si):
        if stacks[si] and stacks[si][-1] == need[0]:
            print(['b', 'd'][si], end=' ' if need[0] < N else '\n')
            stacks[si].pop()
            need[0] += 1
            return True
        
        return False
    
    def push(curr, si):
        if si == 1:
            while pop(0):
                pass
        while stacks[si] and stacks[si][-1] < curr:
            if not pop(si):
                pop(si ^ 1)
        
        if si == 1:
            while pop(0):
                pass
        
        stacks[si].append(curr)
        print(['a', 'c'][si], end=' ')
    
    
    for i in range(N):
        push(A[i], MARK[i])
        
    while stacks[0] or stacks[1]:
        while pop(0):
            pass
        while pop(1):
            pass
    
    # print('a a c a b b c a a b a b a b a b d d b b')