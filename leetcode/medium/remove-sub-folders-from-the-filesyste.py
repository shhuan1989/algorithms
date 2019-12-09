# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/7 17:59

"""

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        fs = set(folder)

        ans = []
        for f in folder:
            valid = True
            for i in range(1, len(f)):
                if f[i] == '/' and f[:i] in fs:
                    valid = False
                    break
            if valid:
                ans.append(f)

        return ans

s = Solution()
# print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
print(s.removeSubfolders(["/a/b/c","/a/b/d","/a/b/ca"]))