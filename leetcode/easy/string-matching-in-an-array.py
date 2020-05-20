# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ans = []
        for w in words:
            for u in words:
                if u != w and u.find(w) >= 0:
                    ans.append(w)
                    break
        return ans
    
s = Solution()
print(s.stringMatching(["mass","as","hero","superhero"]))