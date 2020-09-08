# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N, K = map(int, input().split())
    
    A = []
    occ = [False for _ in range(N + 1)]
    for i in range(K):
        row = [int(x) for x in input().split()]
        A.append(row[1:])
        for j in row[1:]:
            occ[j] = True
    
    
    id = 0
    move = 0
    pre = [-1 for _ in range(N+1)]
    after = [-1 for _ in range(N+1)]
    for row in A:
        for i in row:
            id += 1
            if i != id:
                pre[i] = id
                after[id] = i
    
    # for i in range()
    # print(pre)
    # print(after)
    
    done = [False for _ in range(N+1)]
    
    for i in range(1, N+1):
        if done[i]:
            continue
        
        cycle = [i]
        pi = pre[i]
        hascycle = False
        while pi > 0:
            if pi in cycle:
                hascycle = True
                break
            cycle.append(pi)
            pi = pre[pi]
        
        ai = after[i]
        while ai > 0:
            if ai in cycle:
                hascycle = True
                break
            cycle.append(ai)
            ai = after[ai]
        
        for v in cycle:
            done[v] = True
        move += len(cycle) - 1
        # print(cycle, hascycle)
        if hascycle:
            move += 2
    
    if move > 0:
        print('We need {} move operations.'.format(move))
    else:
        print('No optimization needed.')
    
    
    
    
    