# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        
        def check(state, target, word):
            for i in range(n):
                if state & (1 << i) == 0 and target[i] != word[i]:
                    return False
                
            return True
        
        def abbrev(state):
            s = []
            for i in range(n):
                if state & (1 << i) > 0:
                    if s and s[-1][1] == 2:
                        a, b = s.pop()
                        s.append((a+1, 2))
                    else:
                        s.append((1, 2))
                else:
                    s.append((target[i], 1))
                
            return ''.join([str(a) for a, b in s]), len(s)
        
        dictionary = [d for d in dictionary if len(d) == len(target)]
        if not dictionary:
            return str(len(target))
        
        ans, length = target, len(target)
        for s in range(1 << n):
            abb, abl = abbrev(s)
            if abl < length and all(not check(s, target, w) for w in dictionary):
                length = abl
                ans = abb
                    
        return ans
    
    
        
s = Solution()
print(s.minAbbreviation("apple", ["blade"]))
print(s.minAbbreviation("aaaaaxaaaaa", ["bbbbbxbbbbb"]))
print(s.minAbbreviation('apple', ['blade']))
print(s.minAbbreviation('apple', ["plain", "amber", "blade"]))
print(s.minAbbreviation("usaandchinaarefriends", []))

t0 = time.time()
print(s.minAbbreviation("internationalize", ["xnternationalize", "ixternationalize", "inxernationalize", "intxrnationalize", "intexnationalize", "interxationalize", "internxtionalize", "internaxionalize", "internatxonalize", "internatixnalize", "internatioxalize", "internationxlize", "internationaxize", "internationalxze", "internationalixe", "internationalizx"]))
print(time.time() - t0)