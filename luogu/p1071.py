# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(A, B, C):
    T = [-1 for _ in range(26)]
    
    for a, b in zip(A, B):
        if T[a] < 0:
            T[a] = b
        elif T[a] != b:
            return 'Failed'
        
    # print(T, len(set(T)))
    # t = [i for i in range(26) if T[i] < 0]
    # if len(t) > 1:
    #     return 'Failed'
    # elif len(t) == 1:
    #     for i in range(26):
    #         if i not in T:
    #             T[t[0]] = i
    #             break
    # print(T, len(set(T)))
    
    if T.count(-1) > 0:
        return 'Failed'
    
    if len(set(T)) < 26:
        return 'Failed'
    
    ans = [T[v] for v in C]
    return ''.join([chr(ord('A')+v) for v in ans])
    
    
if __name__ == '__main__':
    A = [ord(v) - ord('A') for v in input().strip()]
    B = [ord(v) - ord('A') for v in input().strip()]
    C = [ord(v) - ord('A') for v in input().strip()]
    print(solve(A, B, C))