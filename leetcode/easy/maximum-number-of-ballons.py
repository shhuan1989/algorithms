# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        wc = collections.Counter(text)
        
        return min(min([wc[k] if k in wc else 0 for k in 'ban']), min([wc[k] // 2 if k in wc else 0 for k in 'lo']))
    
    
s = Solution()
print(s.maxNumberOfBalloons('nlaebolko'))
print(s.maxNumberOfBalloons('loonbalxballpoon'))
print(s.maxNumberOfBalloons('leetcode'))