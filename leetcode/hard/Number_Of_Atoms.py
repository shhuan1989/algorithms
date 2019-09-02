# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/25 20:29

"""


class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        wc = collections.defaultdict(int)

        def dfs(fm, times):
            if not fm:
                return

            li = fm.find('(')
            if li < 0:
                i = 0
                f = fm
                n = len(f)
                while i < n:
                    v = f[i]
                    if 'A' <= v <= 'Z':
                        j = i + 1
                        while j < n and 'a' <= f[j] <= 'z':
                            j += 1
                        elem = f[i:j]
                        k = j
                        while k < n and '0' <= f[k] <= '9':
                            k += 1
                        count = int(f[j: k]) if k > j else 1
                        wc[elem] += count * times
                        i = k
            else:
                dfs(fm[:li], times)
                i = li + 1
                c = 1
                n = len(fm)
                while i < n:
                    if fm[i] == '(':
                        c += 1
                    elif fm[i] == ')':
                        c -= 1

                    if c == 0:
                        break
                    i += 1
                j = i + 1
                while j < n and '0' <= fm[j] <= '9':
                    j += 1

                t = int(fm[i+1: j]) if j > i+1 else 1

                dfs(fm[li+1: i], times * t)
                dfs(fm[j:], times)

        dfs(formula, 1)

        ans = [(w, c) for w, c in wc.items()]
        ans.sort()

        return ''.join(['{}{}'.format(w, c if c > 1 else '') for w, c in ans])


s = Solution()
# print(s.countOfAtoms("H2O"))
# print(s.countOfAtoms("Mg(OH)2"))
# print(s.countOfAtoms("K4(ON(SO3)2)2"))
print(s.countOfAtoms("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"))
print("B18900Be18984C4200H5446He1386Li33894N50106O22638")
