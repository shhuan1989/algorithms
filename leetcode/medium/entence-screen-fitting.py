# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/23/19

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
    
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        if rows <= 0:
            return 0

        slen = [len(x) for x in sentence]
        if any([x > cols for x in slen]):
            return 0
            
        st = sum(slen) + len(slen)
        
        @lru_cache(maxsize=None)
        def layout(used):
            count, lines = 0, 0 if used > 0 else 1
            rest = cols - used
            
            if rest < slen[0]:
                return layout(0)
            
            if rest >= st:
                count = rest // st
                used += count * st
                return count, lines, used

            rest = cols - used
            if rest == st - 1:
                return count + 1, lines, 0
            
            count += 1
            for x in slen:
                used += x
                if used > cols:
                    used = x + 1
                    lines += 1
                elif used == cols:
                    used = 0
                    lines += 1
                else:
                    used += 1

            if used == 0:
                lines -= 1

            if cols - used < slen[0]:
                used = 0
            
            return count, lines, used
        
        
        cl = []
        c, l, i = layout(0)
        lines, times = 0, 0
        while True:
            lines += l
            if lines > rows:
                return times
            
            times += c
            cl.append((c, l))
            if i == 0:
                break
            c, l, i = layout(i)
        
        ans = sum([c for c, l in cl])
        l = sum([l for c, l in cl])
        ans *= rows // l
        l = rows % l
        t, v = 0, 0
        for i in range(len(cl)):
            t += cl[i][1]
            v += cl[i][0]
            if t > l:
                ans += v - cl[i][0]
                break
        return ans
        
        
        
            
            
            
            
            
                
            
        
    
s = Solution()
print(s.wordsTyping(["hello","leetcode"], 1, 20) == 1)
print(s.wordsTyping(["hello", "world"], 2, 8) == 1)
print(s.wordsTyping(["hello","leetcode"], 1, 10) == 0)
print(s.wordsTyping(["f","p","a"], 8, 7) == 10)
print(s.wordsTyping(["a", "bcd", "e"], 3, 6) == 2)
print(s.wordsTyping(["I", "had", "apple", "pie"], 4, 5) == 1)
print(s.wordsTyping(["ab","cde","f"], 3, 5) == 1)
print(s.wordsTyping(["a"], 10000, 10000))
print(s.wordsTyping(["a","bcd"], 20000, 20000))

print(s.wordsTyping(["abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r"], 19948, 19994), 848587)