# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/13

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
    
    pii = [1] * 15
    for i in range(2, 15):
        pii[i] = i * pii[i-1]
    
    # print(pii)
    
    m = 1
    while pii[m] < K:
        m += 1
    
    # print(m)
    if N-m+1 <= 0:
        print(-1)
        exit(0)
    
    A = [i for i in range(N-m+1, N+1)]
    # print(A)
    # print(len(A))
    
    ret = []
    for i in range(m):
        j = K // pii[m-i-1] - 1 if K % pii[m-i-1] == 0 else K // pii[m-i-1]
        if j >= len(A):
            print(-1)
            exit(0)
        ret.append(A[j])
        A = A[:j] + A[j+1:]
        K -= j * pii[m-i-1]
    
    
    def islucky(x):
        while x > 0:
            y = x % 10
            if y != 4 and y != 7:
                return False
            x //= 10
            
        return True
    
    # print(ret)
    
    s = N-m+1
    ans = 0
    for i in range(m):
        index = s + i
        if islucky(index) and islucky(ret[i]):
            ans += 1
    
    
    def numlen(x):
        l = 0
        while x > 0:
            l += 1
            x //= 10
        return l
    
    maxv = N-m
    maxvlen = numlen(maxv)
    # ans += 2 ** (numlen(maxv) - 1)
    
    
    def dfs(index, val):
        if index >= maxvlen:
            return 1 if val <= maxv else 0
        return 1 + dfs(index+1, val * 10 + 4) + dfs(index+1, val*10 + 7)
    
    ans += dfs(0, 0) - 1
    
    print(ans)
