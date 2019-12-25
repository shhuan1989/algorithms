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


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                k = j
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                    
                i += int(abbr[j: k])
                j = k
            else:
                return False
        
        return i == len(word) and j == len(abbr)
    
    
s = Solution()
print(s.validWordAbbreviation('internationalization', 'i12iz4n'))
print(s.validWordAbbreviation('apple', 'a23'))
print(s.validWordAbbreviation('apple', 'a2e'))
print(s.validWordAbbreviation('apple', 'a3e'))
print(s.validWordAbbreviation('a', '2'))
print(s.validWordAbbreviation('a', '01'))