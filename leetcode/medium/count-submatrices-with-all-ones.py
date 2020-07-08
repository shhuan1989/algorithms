# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        h = [0 for _ in range(m)]
        ans = 0
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    h[c] = 0
                else:
                    h[c] += 1
            c = 0
            while c < m:
                if h[c] == 0:
                    c += 1
                    continue
                s = [h[c]]
                cr = c + 1
                while cr < m and h[cr] != 0:
                    s.append(h[cr])
                    cr += 1
                
                for i in range(len(s)):
                    minh = s[i]
                    for j in range(i, len(s)):
                        minh = min(minh, s[j])
                        # a = minh
                        ans += minh
                
                c = cr
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSubmat([
        [1,0,1],
        [1,1,0],
        [1,1,0]]))
    
    print(s.numSubmat([
        [0,1,1,0],
        [0,1,1,1],
        [1,1,1,0]]))
    
    print(s.numSubmat([[1,1,1,1,1,1]]))
    print(s.numSubmat([[1,0,1],[0,1,0],[1,0,1]]))
    
    