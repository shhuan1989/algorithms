# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if not num:
            return ''
        
        num = [int(x) for x in num]
        num_len = len(num)
        num_index = collections.defaultdict(list)
        for i, v in enumerate(num):
            num_index[v].append(i)
        
        uniq_nums = list(sorted(num_index.keys()))
        fenwick_bits = [0 for _ in range(num_len)]
        
        def update(index, val):
            while index < num_len:
                fenwick_bits[index] += val
                index |= index + 1
        
        def query(index):
            s = 0
            while index >= 0:
                s += fenwick_bits[index]
                index = (index & (index + 1)) - 1
                
            return s
        
        for i in range(num_len):
            update(i, 1)
        
        ans = []
        step = 0
        removed = [False for _ in range(num_len)]
        for v in uniq_nums:
            for i in num_index[v]:
                nstep = step + query(i-1)
                if nstep <= k:
                    step = nstep
                    ans.append(v)
                    update(i, -1)
                    removed[i] = True
                else:
                    k -= step
                    rest = [num[j] for j in range(num_len) if not removed[j]]
                    while k > 0:
                        min_num, min_num_index = 9, -1
                        for j in range(k+1):
                            if min_num_index < 0 or rest[j] < min_num:
                                min_num = rest[j]
                                min_num_index = j
                        ans.append(min_num)
                        rest = rest[:min_num_index] + rest[min_num_index+1:]
                        k -= min_num_index
                    ans += rest
                    return ''.join(map(str, ans))
        
        return ''.join(map(str, ans))
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minInteger('4321', 4))
    print(s.minInteger('100', 1))
    print(s.minInteger('36789', 1000))
    print(s.minInteger('22', 22))
    print(s.minInteger('9438957234785635408', 23) == '0345989723478563548')
    
                
        