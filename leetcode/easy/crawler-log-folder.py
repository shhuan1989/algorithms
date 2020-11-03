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
    def minOperations(self, logs: List[str]) -> int:
        q = []
        
        for op in logs:
            if op == './':
                continue
            elif op == '../':
                if q:
                    q.pop()
            else:
                q.append(op)
        
        return len(q)
    
if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(["d1/","d2/","../","d21/","./"]))
    print(s.minOperations( ["d1/","d2/","./","d3/","../","d31/"]))
    print(s.minOperations(["d1/","../","../","../"]))