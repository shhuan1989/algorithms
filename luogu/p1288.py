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
    # sys.stdin = open('P1288_4.in', 'r')
    N = int(input())
    A = [int(x) for x in input().split()]
    
    if sum(A) == 0:
        print('NO')
    else:
        
        start = 0
        
        def dfs(curr):
            right, left = curr, (N+curr-1) % N
            if A[left] == 0 and A[right] == 0:
                return False
            
            if A[left] > 0:
                if A[left] == 1:
                    A[left] = 0
                    if not dfs(left):
                        A[left] = 1
                        return True
                    A[left] = 1
                else:
                    pv = A[left]
                    for v in [0, 1]:
                        A[left] = v
                        if not dfs(left):
                            A[left] = pv
                            return True
                        A[left] = pv
            
            if A[right] > 0:
                if A[right] == 1:
                    A[right] = 0
                    if not dfs((right+1)%N):
                        A[right] = 1
                        return True
                    A[right] = 1
                else:
                    pv = A[right]
                    for v in [0, 1]:
                        A[right] = v
                        if not dfs((right+1) % N):
                            A[right] = pv
                            return True
                        A[right] = pv
            
            return False
        
        print('YES' if dfs(start) else 'NO')