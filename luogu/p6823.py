# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def solve(N, M, ops):
    A = [i + 1 for i in range(N)]
    flip = 0
    for op in ops:
        if op[0] == 1:
            pass
        elif op[0] == 2:
            flip ^= 1
        elif op[0] == 4:
            flip ^= 1
        else:
            x, y = op[1] - 1, op[2] - 1
            if flip == 1:
                x, y = N - x - 1, N - y - 1
            A[x], A[y] = A[y], A[x]
    
    if flip == 0:
        print(' '.join(map(str, A)))
    else:
        print(' '.join(map(str, reversed(A))))
    sys.stdout.flush()
        
        
if __name__ == '__main__':
    
    # N, M = 10**6, 10**6
    # ops = []
    # import random
    # for _ in range(M):
    #     if random.randint(1, 10) > 3:
    #         x = random.randint(0, N-1)
    #         y = random.randint(0, N-1)
    #         ops.append((3, x, y))
    #     else:
    #         ops.append([4])
    # t0 = time.time()
    # solve(N, M, ops)
    # print(time.time() - t0)
    
    
    N, M = map(int, input().split())
    ops = []
    for _ in range(M):
        line = [int(x) for x in input().strip().split()]
        if line[0] == 1 or line[0] == 2:
            ops = [line]
        else:
            ops.append(line)
    
    solve(N, M, ops)
    
    

