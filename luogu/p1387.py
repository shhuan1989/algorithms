# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    
    ans = 0
    h = [0 for _ in range(M)]
    for r in range(N):
        for c in range(M):
            h[c] = h[c] + 1 if A[r][c] == 1 else 0
        
        left, right = 0, 0
        height = h[0]
        while left < M and right < M:
            width = right-left+1
            height = min(height, h[right])
            ans = max(ans, min(width, height))
            if width > height:
                if left + 1 >= M:
                    break
                left += 1
                right = left
                height = h[left]
            else:
                right += 1
    
    print(ans)
        