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
import itertools

if __name__ == '__main__':
    A = [int(x) for x in input().strip().split()]
    
    
    def dfs(a, ops):
        if len(a) == 1 and a[0] == 24:
            print('\n'.join(ops))
            exit(0)
        if len(a) < 2:
            return
        if a[0] < a[1]:
            return
        
        for op in ['+', '-', '*']:
            v = a[0] + a[1]
            if op == '-':
                v = a[0] - a[1]
            elif op == '*':
                v = a[0] * a[1]
            if v <= 0:
                continue
            nops = ops + ['{}{}{}={}'.format(a[0], op, a[1], v)]
            na = [v] + a[2:]
            for nna in itertools.permutations(na):
                dfs(list(nna), nops)
        if a[0] >= a[1]  and a[1] != 0 and a[0] % a[1] == 0:
            na = [a[0] // a[1]] + a[2:]
            nops = ops + ['{}/{}={}'.format(a[0], a[1], a[0] // a[1])]
            for nna in itertools.permutations(na):
                dfs(list(nna), nops)
        
    for a in itertools.permutations(A):
        dfs(list(a), [])
        
    print('No answer!')