# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(start, target):
            if start == target:
                return 0
            
            sa = [a for a, b in zip(start, target) if a != b]
            sb = [b for a, b in zip(start, target) if a != b]
            nsa = len(sa)
            
            match = set()
            for i in range(nsa):
                if i in match:
                    continue
                for j in range(i + 1, nsa):
                    if j not in match and sa[i] != sa[j] and (sa[i], sa[j]) == (sb[j], sb[i]):
                        match.add(i)
                        match.add(j)
                        break

            ans = len(match) // 2
            sa = [sa[i] for i in range(nsa) if i not in match]
            sb = [sb[i] for i in range(nsa) if i not in match]
            
            s, t = sa, sb
            sb = ''.join(sb)
            nsa = len(sa)
            minstep = nsa
            for i in range(nsa):
                for j in range(i+1, nsa):
                    if s[i] != s[j] and s[i] == t[j]:
                        s[i], s[j] = s[j], s[i]
                        minstep = min(minstep, 1 + dfs(''.join(s), sb))
                        s[i], s[j] = s[j], s[i]
                        
            return ans + minstep
        
        return dfs(A, B)
        

s = Solution()
print(s.kSimilarity('ab', 'ba'))
print(s.kSimilarity('abc', 'bca'))
print(s.kSimilarity('abac', 'baca'))
print(s.kSimilarity('aabc', 'abca'))
print(s.kSimilarity("abccaacceecdeea", "bcaacceeccdeaae"))
print(s.kSimilarity("abcdefabcdefabcdef",  "bebafcfeddaccdebfa"))
