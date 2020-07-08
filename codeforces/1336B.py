# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve_impl(nr, ng, nb, r, g, b):
    ans = float('inf')
    
    for y in g:
        i = bisect.bisect_left(r, y)
        # i = min(i, nr-1)
        x = r[i] if i < nr and r[i] == y else r[max(i-1, 0)]
        # x = r[max(i-1, 0)]
        j = bisect.bisect_right(b, y-1)
        j = min(j, nb-1)
        z = b[j]
        ans = min(ans, (x-y)**2 + (y-z)**2 + (z-x)**2)
    
    return ans
    
    
    
    


def solve(nr, ng, nb, r, g, b):
    r.sort()
    g.sort()
    b.sort()
    va = solve_impl(nr, ng, nb, r, g, b)
    vb = solve_impl(ng, nr, nb, g, r, b)
    vc = solve_impl(nb, nr, ng, b, r, g)
    vd = solve_impl(nr, nb, ng, r, b, g)
    ve = solve_impl(ng, nb, nr, g, b, r)
    vf = solve_impl(nb, ng, nr, b, g, r)
    
    return min(va, vb, vc, vd, ve, vf)


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        nr, ng, nb = map(int, input().split())
        r = [int(x) for x in input().split()]
        g = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        ans.append(solve(nr, ng, nb, r, g, b))
    
    print('\n'.join(map(str, ans)))