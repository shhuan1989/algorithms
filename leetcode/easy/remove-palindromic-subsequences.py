# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/26/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        
        ns = len(s)
        if all(s[i] == s[ns-i-1] for i in range(ns//2)):
            return 1

        wc = collections.Counter(s)
        return len(wc)
        
        
        
        
        
s = Solution()
print(s.removePalindromeSub('ababa'))
print(s.removePalindromeSub('abb'))
print(s.removePalindromeSub('baabb'))
print(s.removePalindromeSub(''))
print(s.removePalindromeSub("bbaabaaa"))