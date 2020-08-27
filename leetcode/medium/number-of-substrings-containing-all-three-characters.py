# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        index = [[] for _ in range(3)]
        
        for i, v in enumerate(s):
            index[ord(v) - ord('a')].append(i)
        
        ii = [0, 0, 0]
        ans = 0
        ns = len(s)
        while all([i < len(index[t]) for t, i in enumerate(ii)]):
            ans += ns - max([index[t][i] for t, i in enumerate(ii)])
            print([index[t][i] for t, i in enumerate(ii)])
            st, si = -1, ns
            for t, i in enumerate(ii):
                if index[t][i] < si:
                    si = index[t][i]
                    st = t
            ii[st] += 1
        
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))