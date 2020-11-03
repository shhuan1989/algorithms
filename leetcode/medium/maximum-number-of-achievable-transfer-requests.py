# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        m = len(requests)

        def get(val):
            x = 0
            while val > 0:
                x += 1 if (val & 1 > 0) else 0
                val >>= 1
            return x

        ans = -1
        for s in range(1 << m):
            c = [0 for _ in range(n)]
            for i in range(m):
                if s & (1 << i) > 0:
                    u, v = requests[i]
                    c[u] -= 1
                    c[v] += 1

            if all(x == 0 for x in c):
                # print([requests[i] for i in [i for i in range(m) if s & (1 << i) > 0]])
                ans = max(ans, get(s))

        return ans
    


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumRequests(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
    # print(s.maximumRequests(3, [[0,0],[1,2],[2,1]]))
    # print(s.maximumRequests(4, [[0,3],[3,1],[1,2],[2,0]]))
    # print(s.maximumRequests(3, [[2,0],[2,1],[1,0],[0,2],[1,2]]))
    # print(s.maximumRequests(2, [[1,1],[1,0],[0,1],[0,0],[0,0],[0,1],[0,1],[1,0],[1,0],[1,1],[0,0],[1,0]]))
    print(s.maximumRequests(9, [[3,7],[6,0],[4,7],[4,0],[6,6],[0,6],[7,4],[6,7],[5,4],[1,8],[4,3]]))