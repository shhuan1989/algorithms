# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    
    def dfs(x, y, a, b, l):
        if l == 1:
            return
        l >>= 1
        
        if x - a < l and y - b < l:
            print('{} {} 1'.format(a + l, b + l))
            dfs(x, y, a, b, l)
            dfs(a + l - 1, b + l, a, b + l, l)  # 递归做右上角
            dfs(a + l, b + l - 1, a + l, b, l)  # 递归做左下角
            dfs(a + l, b + l, a + l, b + l, l)  # 递归做右下角
        
        if x - a < l and y - b >= l:
            print('{} {} 2'.format(a + l, b + l - 1))
            dfs(a + l - 1, b + l - 1, a, b, l)  # 递归做左上角
            dfs(x, y, a, b + l, l)
            dfs(a + l, b + l - 1, a + l, b, l)  # 递归做左下角
            dfs(a + l, b + l, a + l, b + l, l)  # 递归做右下角
        
        if x - a >= l and y - b < l:
            print('{} {} 3'.format(a + l - 1, b + l))
            dfs(a + l - 1, b + l - 1, a, b, l)  # 递归做左上角
            dfs(a + l - 1, b + l, a, b + l, l)  # 递归做右上角
            dfs(x, y, a + l, b, l)
            dfs(a + l, b + l, a + l, b + l, l)  # 递归做右下角
        
        if x - a >= l and y - b >= l:
            print('{} {} 4'.format(a + l - 1, b + l - 1))
            dfs(a + l - 1, b + l - 1, a, b, l)  # 递归做左上角
            dfs(a + l - 1, b + l, a, b + l, l)  # 递归做右上角
            dfs(a + l, b + l - 1, a + l, b, l)  # 递归做左下角
            dfs(x, y, a + l, b + l, l)
    
    
    K = int(input().strip())
    X, Y = map(int, input().strip().split())
    dfs(X, Y, 1, 1, 1 << K)