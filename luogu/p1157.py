# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    
    
    def dfs(index, pre, vis):
        if index >= K:
            for v in pre:
                print('{:3}'.format(v), end='')
            print()
            return
        
        for i in range(pre[-1] if pre else 1, N+1):
            if i not in vis:
                dfs(index+1, pre+[i], vis | {i})
                
    
    dfs(0, [], set())