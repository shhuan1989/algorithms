# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxValueAfterReverse(self, A: List[int]) -> int:
        # A[0], A[1], ... A[N]
        # A[0], ..., A[i-1], A[i], A[i+1], ..., A[j], A[j+1], ..., A[N]
        # A[0], ..., A[i-1], A[j], A[j-1], ..., A[i], A[j+1], ..., A[N]
        # abs(A[i]-A[i-1]) + abs(A[j+1]-A[j])
        # => abs(A[j]-A[i-1]) + abs(A[j+1]-A[i])
        # delta = abs(A[j]-A[i-1]) + abs(A[j+1]-A[i]) - abs(A[i]-A[i-1]) - abs(A[j+1]-A[j])
        # fix = abs(A[i]-A[i-1])
        # delta = abs(A[i]-A[i-1]) + abs(A[j+1]-A[i]) - abs(A[j+1]-A[j]) - fix
        # delat = max {
        #      A[j]+A[j+1]-A[i]-A[i-1]
        #      A[j]-A[j+1]+A[i]-A[i-1]，
        #      -A[j]+A[j+1]-A[i]+A[i-1]，
        #      -A[j]-A[j+1]+A[i]+A[i-1]，
        #   } - abs(A[j+1]-A[j]) - fix,
        
        
        def getdiff(a):
            return sum([abs(a[i]-a[i+1]) for i in range(len(a)-1)])
            
        def brutal(a):
            x = 0
            xi, xj = -1, -1
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    a[i:j+1] = a[i:j+1][::-1]
                    v = getdiff(a)
                    if v > x:
                        x = v
                        xi, xj = i, j
                    a[i:j+1] = a[i:j+1][::-1]
            
            return x, xi, xj
            
        # print(brutal(A))
        
        N = len(A)
        ans = 0
        diff = []
        for i in range(1, N):
            d = abs(A[i]-A[i-1])
            diff.append(d)
            ans += d
        
        maxright = [[float('-inf') for _ in range(4)] for _ in range(N)]
        for i in range(N-2, -1, -1):
            fix = abs(A[i + 1] - A[i])
            maxright[i][0] = max(maxright[i + 1][0], A[i] + A[i + 1] - fix)
            maxright[i][1] = max(maxright[i + 1][1], A[i] - A[i + 1] - fix)
            maxright[i][2] = max(maxright[i + 1][2], -A[i] + A[i + 1] - fix)
            maxright[i][3] = max(maxright[i + 1][3], -A[i] - A[i + 1] - fix)
        
        maxdelta = float('-inf')
        for i in range(1, N-1):
            fix = abs(A[i]-A[i-1])
            delta = [0 for _ in range(4)]
            delta[0] = -A[i] - A[i-1] - fix
            delta[1] = A[i] - A[i-1] - fix
            delta[2] = -A[i] + A[i-1] - fix
            delta[3] = A[i] + A[i-1] - fix
            for j in range(4):
                delta[j] += maxright[i+1][j]
            maxdelta = max(maxdelta, max(delta))
        
        
        if len(A) > 2:
            for k in range(1, N-1):
                # reverse first k items
                maxdelta = max(maxdelta, abs(A[k+1] - A[0]) - abs(A[k+1]-A[k]))
            
            for k in range(N-2, 0, -1):
                # reverse last k items
                maxdelta = max(maxdelta, abs(A[N-1]-A[k-1]) - abs(A[k]-A[k-1]))
            
            
        # print(ans)
        return max(ans + max(maxdelta, 0), 0)
    

if __name__ == '__main__':
    s = Solution()
    # print(s.maxValueAfterReverse([2]))
    # print(s.maxValueAfterReverse([3, 2]))
    # print(s.maxValueAfterReverse([1, 4, 2]))
    # print(s.maxValueAfterReverse([2,5,1,3,4]))
    # print(s.maxValueAfterReverse([2,3,1,5,4]))
    # print(s.maxValueAfterReverse([2,4,9,24,2,1,10]))
    print(s.maxValueAfterReverse([63674,-34608,86424,-52056,-3992,93347,2084,-28546,-75702,-28400]))
    
    
        
        
        