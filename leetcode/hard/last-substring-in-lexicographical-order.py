# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/9/19


Given a string s, return the last substring of s in lexicographical order.



"""

import collections
import time
import os
import sys
import bisect
import heapq


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j = 0, 1
        while j < n:
            k = 0
            while j+k < n and s[i+k] == s[j+k]:
                k += 1
            if j + k >= n:
                return s[i:]
            
            if s[i+k] < s[j+k]:
                i = j
                j = i + 1
            else:
                j = j+k+1
            
        return s[i:]
        
    
    def lastSubstring2(self, s: str) -> str:
        sa = self.build_suffix_array(s)
        return s[sa[-1]:]


    def build_suffix_array(self, anStr):
        """
        https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/
        :param anStr:
        :return:
        """
        if not anStr:
            return []
        
        chs = list(sorted(set(anStr)))
        ranks = {c: i for i, c in enumerate(chs)}
        
        # rank, prank, index
        n = len(anStr)
        suffix = [[ranks[v], ranks[anStr[i + 1]] if i < n - 1 else -1, i] for i, v in enumerate(anStr)]
        suffix.sort()
        
        k = 1
        ind = [0] * n
        while k < n:
            rank, prank = suffix[0][0], suffix[0][0]
            for i in range(1, n):
                if suffix[i][0] != prank or suffix[i][1] != suffix[i - 1][1]:
                    rank += 1
                prank = suffix[i][0]
                suffix[i][0] = rank
                ind[suffix[i][2]] = i
            
            for i in range(n):
                nextInd = suffix[i][2] + k
                suffix[i][1] = suffix[ind[nextInd]][0] if nextInd < n else -1
            
            suffix.sort()
            k *= 2
        
        return [v[2] for v in suffix]

s = Solution()
print(s.lastSubstring('cacacb'))
# print(s.lastSubstring('abab'))
# print(s.lastSubstring('leetcode'))
# print(s.lastSubstring('a'*(4*10**5)))