# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        ps = s
        s = [ord(v) - ord('a') for v in s]
        n = len(s)
        start, end = {}, {}

        presum = [[0 for _ in range(26)] for _ in range(n + 1)]
        chnum = [0 for _ in range(26)]
        for i, v in enumerate(s):
            chnum[v] += 1
            if v not in start:
                start[v] = i
                end[v] = i
            else:
                end[v] = i
            
            for j in range(26):
                presum[i+1][j] = presum[i][j]
            presum[i+1][v] += 1
        
        
        ans = []
        s = 0
        for e, c in sorted([(e, ch) for ch, e in end.items()]):
            if start[c] < s:
                continue
            
            for i in range(start[c], s-1, -1):
                find = True
                for ch in range(26):
                    d = presum[e+1][ch] - presum[i][ch]
                    if d != chnum[ch] and d != 0:
                        find = False
                        break
                if find:
                    ans.append((i, e+1))
                    s = e + 1
                    break
                
        
        # print(ans)
        return [ps[s:e] for s, e in ans]
            

if __name__ == '__main__':
    s = Solution()
    print(s.maxNumOfSubstrings("abab"))
    print(s.maxNumOfSubstrings("adefaddaccc"))
    print(s.maxNumOfSubstrings("abbaccd"))