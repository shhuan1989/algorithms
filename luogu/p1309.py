# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import cmp_to_key

if __name__ == '__main__':
    # sys.stdin = open('P1309_2.in', 'r')
    # t0 = time.time()
    N, R, Q = map(int, input().strip().split())
    scores = [int(x) for x in input().split()]
    power = [int(x) for x in input().split()]
    
    curr = [i for i in range(2 * N)]
    curr.sort(key=cmp_to_key(lambda a, b: scores[b]-scores[a] if scores[b] != scores[a] else a-b))
    win = [0 for _ in range(N)]
    lose = [0 for _ in range(N)]
    # print(time.time() - t0)
    for _ in range(R):
        k = 0
        for i in range(0, 2*N, 2):
            a, b = curr[i], curr[i+1]
            if power[a] < power[b]:
                scores[b] += 1
                win[k] = b
                lose[k] = a
            else:
                scores[a] += 1
                win[k] = a
                lose[k] = b
            k += 1
        # curr.sort(key=cmp_to_key(lambda a, b: scores[b] - scores[a] if scores[b] != scores[a] else a - b))
        iwin, ilose, ic = 0, 0, 0
        while iwin < N and ilose < N:
            if scores[win[iwin]] > scores[lose[ilose]]:
                curr[ic] = win[iwin]
                iwin += 1
            elif scores[win[iwin]] == scores[lose[ilose]]:
                if win[iwin] < lose[ilose]:
                    curr[ic] = win[iwin]
                    iwin += 1
                else:
                    curr[ic] = lose[ilose]
                    ilose += 1
            else:
                curr[ic] = lose[ilose]
                ilose += 1
            ic += 1
        while iwin < N:
            curr[ic] = win[iwin]
            ic += 1
            iwin += 1
        while ilose < N:
            curr[ic] = lose[ilose]
            ic += 1
            ilose += 1
    
    print(curr[Q-1]+1)
    # print(time.time() - t0)
        