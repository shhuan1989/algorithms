# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1333.in', 'r')
    id = [0]
    # mem = {}
    # def getid(s):
    #     if s in mem:
    #         return mem[s]
    #     id[0] += 1
    #     mem[s] = id[0]
    #     return id[0]
    
    
    trie = {}
    def getid(s):
        t = trie
        for ch in s:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        if '#' in t:
            return t['#']
        id[0] += 1
        t['#'] = id[0]
        return id[0]
    


    parent = [i for i in range(500010)]


    def find(u):
        pu = parent[u]
        if pu == u:
            return pu
        parent[u] = find(pu)
        return parent[u]


    def merge(u, v):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            return True
        return False
    
    degree = [0 for i in range(500010)]
    mc = 0
    for line in sys.stdin:
        s = line.strip().split()
        x = getid(s[0])
        y = getid(s[1])
        
        if merge(x, y):
            mc += 1
        degree[x] += 1
        degree[y] += 1
        
    
    if mc < id[0]-1:
        print('Impossible')
        exit(0)
    
    odd = len([x for x in degree if x % 2 == 1])
    if odd > 0 and odd != 2:
        print('Impossible')
    else:
        print('Possible')