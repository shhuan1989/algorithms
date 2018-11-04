# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""

import bisect
import collections
import heapq
import random
import time

class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """


        ans = []
        N, M = len(target), len(stamp)

        target = list(target)
        stamp = list(stamp)

        left = {i for i in range(N)}

        def count(start):
            ok, cnt = True, 0
            for j in range(M):
                if target[start + j] == '.':
                    continue
                if target[start + j] != stamp[j]:
                    ok = False
                    break
                cnt += 1

            return cnt if ok else 0

        mxCounts = [count(i) for i in range(N-M+1)]
        while any(target[i] != '.' for i in range(N)):
            mxIdx, mxCount = -1, 0
            for i, v in enumerate(mxCounts):
                if v > mxCount:
                    mxCount = v
                    mxIdx = i

            if mxCount == 0:
                return []
            for i in range(M):
                target[i + mxIdx] = '.'
                left.discard(i+mxIdx)

            for i in range(max(0, mxIdx-M-1), min(N-M+1, mxIdx+M+1)):
                mxCounts[i] = count(i)

            ans.append(mxIdx)

        return list(reversed(ans))









s = Solution()
# print(s.movesToStamp("ffebb", "fffeffebbb"))
# print(s.movesToStamp("aaca", "aaaacaaaca"))
# print(s.movesToStamp('a', 'vc'))
# print(s.movesToStamp(stamp = "abc", target = "ababc"))
# print(s.movesToStamp(stamp = "abca", target = "aabcaca"))

t0 = time.time()
print(s.movesToStamp("dcba", "dcbababdcdcbaacbadcdcbdcbadcdcbaabaacdcdcdcbabadcbabacbddcbadcbadcbacbadcbabdcbdcdcbabdddcbaadcbaabdcbdcdcbabdcbaaddcbdcbadcbadcbaaadcbdcbadcbabacbabaddcbaadcbaacbddcbabacbdcbacbadcbaddcbdcbacbaadcdcbadcbaaadcbaddcdcbacdcbabddcbdcdcbadcdcbacbddcbaabababadcbadcbaabaabadcbabaadcbdcbacbabadcbababdcddcbabadcdcbacbadcbadcbabdcbddcbabaaddcdcbabdcbaaddcbdcbaddcbacbababdcdcbadcbacddcbabacbadcbadcbaacdcbaabacbaaadcdcdcbaaadcbadcbacbdcbaadcbacbaddcdcbadcbaababaddcbaababadcdcbababdcbadcbacbabdcbadcbabaadcbdcbabdcbaaadcbadcbadcddcbdcbabacbaadcdcbabaddcdcbacdcdcbaababdcdcbababaacddcbdcdcbacbadcbadcbabdcbaacdcbdcbaaddcdcbaddcbadcdcdcbaaadcbaacdcbacdcbabadcdcbdcbaadcbdcdcbabacbdcbababacbadcdcbacdcbdcbacbadcbadcdcbaadcbabadcbdcbabadddcbabaadcbaadcbaaaabaaddddcbadcbdcbacbadcbadddcddcbaaacbaadcbabadcdcbadcbadcbdddcbacbaddcbacbabaaacdddcbadcbdcbadcdcbaadcbabaddcbabadcbadcbadcbabdcbabadcbdcbaadcbacbadcbdcbacbacbdcbaacdcbadcdcbacbadcbadcbacdcbabadcbdcdcbacbacdcbabadcbaabaddcdcbabadcbadcbaadcbabaabddcbaaaaa"))
print(time.time() - t0)
