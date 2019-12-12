# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        N = len(shifts)
        s = 0
        ans = ''
        for i in range(N-1, -1, -1):
            s += shifts[i]
            s %= 26
            ch = chr(((ord(S[i]) - ord('a')) + s) % 26 + ord('a'))
            ans += ch
        
        return ans[::-1]
    
s= Solution()
print(s.shiftingLetters('abc', [3, 5, 9]))