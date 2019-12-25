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
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        g = collections.defaultdict(set)
        for a, b in pairs:
            g[a].add(b)
            g[b].add(a)
        
        for i in range(len(words1)):
            a, b = words1[i], words2[i]
            if a != b and b not in g[a]:
                return False
        
        return True
