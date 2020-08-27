# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

if __name__ == '__main__':
    
    A = [[0 for _ in range(5)] for _ in range(5)]
    x, y = map(int, input().split())
    A[x][y] = 1
    
    used = [False for _ in range(17)]
    used[1] = True

    regions = [
        [(1, 1), (1, 4), (4, 1), (4, 4)],
        [(1, 1), (1, 2), (2, 1), (2, 2)],
        [(1, 3), (1, 4), (2, 3), (2, 4)],
        [(3, 1), (3, 2), (4, 1), (4, 2)],
        [(3, 3), (3, 4), (4, 3), (4, 4)],
        [(2, 2), (2, 3), (3, 2), (3, 3)],
        [(1, 1), (2, 2), (3, 3), (4, 4)],
        [(1, 4), (2, 3), (3, 2), (4, 1)]
    ]

    for x in range(1, 5):
        regions.append([(x, y) for y in range(1, 5)])
    for y in range(1, 5):
        regions.append([(x, y) for x in range(1, 5)])
    
    regionsbyr = collections.defaultdict(list)
    for r in range(1, 5):
        for rc in regions:
            if all([x <= r for x, y in rc]):
                regionsbyr[r].append(rc)
    
    def check(r):
        for a in regionsbyr[r]:
            if sum([A[x][y] for x, y in a]) != 34:
                return False
        
        return True
    
        
    def dfs(r, c):
        # if A[1][2] == 4 and A[1][3] == 13 and A[1][4] == 16 and A[2][1] == 14 and A[2][2] == 15 and A[2][3] == 2:
        #     print('='*80)
        #     for row in A:
        #         print(' '.join(map(str, row)))
        if r >= 5:
            
            if check(r):
                # print('=' * 80)
                return ['\n'.join([' '.join(map(str, row[1:])) for row in A[1:]])]
            
        if A[r][c] == 1:
            return dfs(r, c+1) if c < 4 else dfs(r+1, c)
    
        ans = []
        for v in range(2, 17):
            if not used[v]:
                A[r][c] = v
                if c < 4 or check(r):
                    used[v] = True
                    if c < 4:
                        ans += dfs(r, c+1)
                    else:
                        ans += dfs(r+1, 1)
                    used[v] = False
        A[r][c] = 0
        return ans
    
    
    print('\n\n'.join(dfs(1, 1)))
