# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            w, c = 'z', 0
            for u in word:
                if u == w:
                    c += 1
                elif u < w:
                    w = u
                    c = 1
            return c
            
        memo = [0] * 12
        for w in words:
            memo[f(w)] += 1
            
        for i in range(10, -1, -1):
            memo[i] += memo[i+1]
                
        return [memo[f(q)+1] for q in queries]
    
    
s = Solution()
print(s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
print(s.numSmallerByFrequency(["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"], ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]))
print(s.numSmallerByFrequency(["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"], ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]))