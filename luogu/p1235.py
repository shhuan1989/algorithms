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
from functools import lru_cache



class Num:
    def __init__(self, inte: int, fract: List[int]):
        self.inte = inte
        fract = fract[:300]
        fract = fract + [0] * (300 - len(fract))
        self.fract = fract
        
    def __add__(self, other: 'Num'):
        da, db = self.fract, other.fract
        cap = 0
        dc = [0] * 300
        for i in range(299, -1, -1):
            v = da[i] + db[i] + cap
            dc[i] = v % 10
            cap = v // 10
        
        inte = self.inte + other.inte + cap
        
        return Num(inte, dc)
    
    def div2(self):
        inte = self.inte // 2
        
        cap = self.inte % 2
        data = [0] * 300
        for i in range(300):
            v = 10 * cap + self.fract[i]
            data[i] = v // 2
            cap = v % 2
        
        return Num(inte, data)
    
    def out(self):
        v = self.fract.copy()
        while v and v[-1] == 0:
            v.pop()
        
        a = self.inte * 100
        if v:
            a += 10 * v[0]
        if v and len(v) > 1:
            a += v[1]
        
        if len(v) > 2:
            b = ''.join(map(str, v[2:]))
            return '{}.{}'.format(a, b)
        else:
            return '{}'.format(a)
        

# a = Num(1, [2, 3, 4])
# b = Num(2, [8, 9, 1])
# c = a + b
# print(c.out())
# d = c.div2()
# print(d.out())
    

if __name__ == '__main__':
    N, K = map(int, input().split())
    pa = [-1 for _ in range(N + 1)]
    ma = [-1 for _ in range(N + 1)]
    son = [[] for _ in range(N + 1)]
    
    for i in range(K):
        a, b, c = map(int, input().split())
        pa[a] = b
        ma[a] = c
        son[b].append(a)
        son[c].append(a)
    
    dep = [-1 for _ in range(N + 1)]
    q = [i for i in range(1, N+1) if pa[i] < 0]
    for v in q:
        dep[v] = 1
    while q:
        nq = []
        for u in q:
            for v in son[u]:
                if dep[v] < 0:
                    dep[v] = dep[u] + 1
                    nq.append(v)
        q = nq
        
    # print(dep)
    
    @lru_cache(maxsize=None)
    def sim(i, j):
        if i == j:
            return Num(1, [])
        
        if dep[i] == 1 and dep[j] == 1:
            return Num(0, [])
        
        if dep[i] > dep[j]:
            return sim(j, i)
        
        c = sim(i, pa[j]) + sim(i, ma[j])
        return c.div2()
    
    
    K = int(input())
    for i in range(K):
        i, j = map(int, input().split())
        s = sim(i, j)
        print('{}%'.format(s.out()))