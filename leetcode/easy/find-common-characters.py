# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return list(itertools.chain(*[[ch] * min([w.count(ch) for w in A]) for ch in [ch for ch in [chr(i + ord('a')) for i in range(26)] if all([w.find(ch) >= 0 for w in A])]]))
    
s = Solution()
print(s.commonChars(["bella","label","roller"]))
