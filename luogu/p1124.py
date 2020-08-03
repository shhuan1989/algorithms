# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = list(input().strip())
    first = int(input())
    B = list(sorted(A))
    
    now = -1
    for i in range(N):
        if B[i] == A[first-1]:
            now = i
            B[i] = '-'
            break
            
    ans = [A[now]]
    
    bci = collections.defaultdict(list)
    for i, c in enumerate(B):
        bci[c].append(i)
    
    for i in range(1, N):
        now = bci[A[now]].pop()
        ans.append(A[now])
    
    print(''.join(ans[::-1]))