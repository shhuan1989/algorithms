# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

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
    s = input().strip()
    ns = len(s)
    
    
    def construct(index, size, pre):
        if index >= size:
            return [pre]
        
        ans = []
        for i in range(ord(pre[-1]) + 1 if pre else ord('a'), ord('z') + 1):
            ans += construct(index + 1, size, pre + chr(i))
        return ans
    
    
    #
    # a = []
    # for i in range(1, 5):
    #     a += construct(0, i, '')
    # a.sort(key=cmp_to_key(lambda a, b: len(a)-len(b) if len(a) != len(b) else (-1 if a <= b else 1)))
    # print(a)
    # wi = {v:i+1 for i, v in enumerate(a)}
    # print(wi)
    
    def check(v):
        return all(v[i] < v[i + 1] for i in range(len(v) - 1))
    
    
    #
    # print(all(check(v) for v in a))
    
    if not s or not check(s):
        print(0)
        exit(0)
    
    
    # print(fact)
    
    def dfs(index, st, op):
        if index >= ns:
            if op <= 0:
                return 1
            return 0
        
        if op == 0:
            ans = 0
            for i in range(ord(st[-1]) + 1 if st else ord('a'), ord(s[index])):
                ch = chr(i)
                ans += dfs(index + 1, st + [ch], -1)
            if not st or ord(st[-1]) < ord(s[index]):
                ans += dfs(index + 1, st + [s[index]], 0)
            
            if not st and index + 1 < ns:
                ans += dfs(index + 1, st, -1)
            return ans
        elif op < 0:
            ans = 0
            for i in range(ord(st[-1]) + 1 if st else ord('a'), ord('z') + 1):
                ans += dfs(index + 1, st + [chr(i)], -1)
            if not st and index + 1 < ns:
                ans += dfs(index + 1, st, -1)
            return ans
    
    
    print(dfs(0, [], 0))