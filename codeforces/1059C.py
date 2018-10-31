# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys





def gcd_list(vals, start):
    
    res = collections.defaultdict(list)
    l = 0
    for v in vals:
        if v <= start:
            continue
        
        res[v] = [u for u in vals if u % v == 0]
        
        if l > 0 and l > len(res[v]):
            break
        
        l = max(l, len(res[v]))
        
    
    return res



def solve(n):
    vals = [i for i in range(1, n+1)]
    
    res = []
    gcd = 1
    
    while vals:
        if len(vals) == 1:
            res.append(vals[0])
            break
            
        gcds = gcd_list(vals, gcd)
        
        v = gcd+1
        l = gcds[v]
        for k, s in gcds.items():
            if (len(s) > len(l) and k > gcd) or (len(s) == len(l) and k > v):
                l = s
                v = k
        if not l:
            v = gcd
            l = gcds[v]
        
        res.extend([vals[0]] * (len(vals) - len(l)))
        vals = l
        gcd = v
        
    return ' '.join(map(str, res))
        
# solve(4)
#
# for i in range(1, 100):
#     print(solve(i))

N = int(input())
print(solve(N))