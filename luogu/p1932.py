# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List



class Heap:
    def __init__(self, cap):
        self.data = [0 for _ in range(cap)]
        self.index = 1
    
    def push(self, key):
        data = self.data
        i = self.index
        data[i] = key
        self.index += 1
        
        while i > 0:
            pi = i // 2
            if pi > 0 and data[pi] > data[i]:
                data[pi], data[i] = data[i], data[pi]
                i = pi
            else:
                break
    
    def pop(self):
        if self.index <= 1:
            return -1
        
        data = self.data
        ret = data[1]
        data[1], data[self.index-1] = data[self.index-1], data[1]
        self.index -= 1
        i = 1
        while i < self.index:
            lc, rc = i * 2, i * 2 + 1
            if rc < self.index:
                ci = lc if data[lc] < data[rc] else rc
                if data[ci] < data[i]:
                    data[i], data[ci] = data[ci], data[i]
                    i = ci
                else:
                    break
            elif lc < self.index:
                if data[lc] < data[i]:
                    data[lc], data[i] = data[i], data[lc]
                    i = lc
                else:
                    break
            else:
                break
                
        return ret
    
    def getmin(self):
        return self.data[1] if self.index > 1 else -1


if __name__ == '__main__':
    
    # qa = Heap(1000)
    # qb = []
    #
    # import random
    # a = [54, 614, 124, 48, 980, 933, 441, 349, 836, 22]
    # for v in a:
    #     # a.append(v)
    #     qa.push(v)
    #     heapq.heappush(qb, v)
    #     if qa.getmin() != qb[0]:
    #         print(a)
    #         print('error')
    #         exit(0)
    #
    # while qb:
    #     x = qa.pop()
    #     y = heapq.heappop(qb)
    #     if x != y:
    #         print(a)
    #         exit(0)
    #
    #
    # print('done')
    
    
    N, M, K = map(int, input().split())
    A = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        row.sort()
        A.append(row)
    
    
    def getk(a):
        # q = [(a[0][0] + a[1][0], 0, 0, False)]
        ret = []
        q = Heap(1000)
        q.push((a[0][0] + a[1][0], 0, 0, False))
        for _ in range(K):
            # u, i, j, p = heapq.heappop(q)
            u, i, j, p = q.pop()
            ret.append(u)
            if j+1 < M:
                q.push((u + a[1][j+1] - a[1][j], i, j+1, True))
                # heapq.heappush(q, (u + a[1][j+1] - a[1][j], i, j+1, True))
            if not p and i+1 < len(a[0]):
                q.push((u + a[0][i+1] - a[0][i], i+1, j, False))
                # heapq.heappush(q, (u + a[0][i+1] - a[0][i], i+1, j, False))
                
        return ret
    
    pre = A[0]
    for i in range(1, N):
        pre = getk([pre, A[i]])
    print(' '.join(map(str, pre)))
    