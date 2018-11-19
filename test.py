# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""

import bisect
import collections
import heapq
import random
import time

import itertools

class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        N = len(A)
        dp = [['' for _ in range(N)] for _ in range(1 << N)]

        def merge(a, b):
            i = min(len(a), len(b))
            while i >= 0:
                if a[len(a) - i:] == b[:i]:
                    return a + b[i:]
                i -= 1

            return a + b


        shared = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if i != j:
                    s = merge(A[i], A[j])
                    shared[i][j] = len(A[i]) + len(A[j]) - len(s)

        for state in range(1 << N):
            for i in range(N):
                if state == 1 << i:
                    dp[state][i] = A[i]
                elif state & (1 << i) == 0:
                    continue
                else:
                    prevs = state ^ (1 << i)
                    for prei in range(N):
                        if prevs & (1 << prei) > 0:
                            # s = merge(dp[prevs][prei], A[i])
                            # no string is substring of other string
                            s = dp[prevs][prei] + A[i][shared[prei][i]:]
                            if dp[state][i] == '' or len(s) < len(dp[state][i]):
                                dp[state][i] = s

        ans = '*' * 1000
        for s in dp[(1 << N) - 1]:
            if len(s) < len(ans):
                ans = s

        return ans




s = Solution()
print(s.shortestSuperstring(["alex","loves","leetcode"]))
print(s.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]))
print(s.shortestSuperstring(["pqtifawzoessrpjwnjf","wnjfjehefpipubizjx","vpmafqkvixcumugp","tzucldkoizjhyat","umugpqtifawzoes","zjxtifiolejwstzuc","pjwnjfjehefpipub","ifiolejwstzucldko"]))

import time
t0 = time.time()
# print(s.shortestSuperstring(["ppgortnmsy","czmysoeeyugbiylso","nbfzpppvhbjydtx","rnzynedhoiunkpon","ornzynedhoiunkpo","ylsomoktkyfgljcf","jtvkrornzynedhoiunk","hvhhihwdffmxnczmyso","ktkyfgljcfbkqcpp","nzynedhoiunkponbfz","nedhoiunkponbfzpppvh"]))
print(s.shortestSuperstring(["vgrikrnwezryimj","umwgwvzpsfpmctzt","pjourlpgeemdjor","urlpgeemdjorpzbkbz","jorpzbkbzcqyewih","xuwkzvoczozhhvf","ihbumoogibirbsvch","nwezryimjivvpjourlp","kzvoczozhhvfwgeplv","ezryimjivvpjourlpgee","zhhvfwgeplvqngglu","rikrnwezryimjivvp"]))
print(time.time() - t0)