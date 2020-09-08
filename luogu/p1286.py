# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def check(n, nums, a):
    b = []
    for i in range(n):
        for j in range(i+1, n):
            b.append(nums[i] + nums[j])
    b.sort()
    
    return b == a
    
def solve(n, a):
    a.sort()
    mina = a[0]
    for s in range(mina + 1):
        ca = collections.Counter(a)
        nums = [s]
        find = True
        for i in range(n-1):
            if not find:
                break

            curr = min([x for x in ca.keys() if ca[x] > 0]) - s
            for v in nums:
                u = v + curr
                if u not in ca or ca[u] <= 0:
                    find = False
                    break
                ca[u] -= 1
            
            nums.append(curr)
        if find and check(n, nums, a):
            return ' '.join(map(str, nums))
    
    return 'Impossible'
    

if __name__ == '__main__':
    # sys.stdin = open('p1286.in', 'r')
    for line in sys.stdin:
        a = [int(x) for x in line.split()]
        print(solve(a[0], a[1:]))