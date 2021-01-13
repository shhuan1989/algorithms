# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2021/1/11

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List

import itertools


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        def choose(jobs, cost, index, precost, previs):
            if index >= len(jobs):
                if precost <= cost:
                    return [[precost, previs]]
                else:
                    return [[0, set()]]
            
            ans = choose(jobs, cost, index + 1, precost, previs)
            if precost + jobs[index] <= cost:
                ans += choose(jobs, cost, index + 1, precost + jobs[index], previs | {index})
            
            return ans
        
        def check(jobs, cost, depth):
            if not jobs:
                return depth <= k
            
            if depth > k:
                return False
            
            chx = choose(jobs, 0, 0, 0, set())
            chx.sort(reverse=True)
            
            for _, x in chx:
                njobs = [jobs[i] for i in range(len(jobs)) if i not in x]
                if check(njobs, cost, depth + 1):
                    return True
            
            return False
        
                
        
        lo, hi = max(jobs), max(jobs) * len(jobs)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if (check(jobs, mid, 0)):
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimumTimeRequired([5,10,9,15,20,12,18,8,13,15], 5))