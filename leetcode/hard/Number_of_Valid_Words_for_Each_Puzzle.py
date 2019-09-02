# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 11:23




两个小写字符串puzzle和word，word合法是指：
    1. word包含puzzle得第一个字母
    2. word中得每个字母都在puzzle中
例子：
puzzle是"abcdefg"，那么 "faced", "cabbage", and "baggage"都是合法得；而"beefed"（不包含"a"）和"based"("s"不在puzzle中)不合法。


给出puzzle和word的列表puzzles和words，返回对于每个puzzle， 合法的word的数量。
words的长度小于10^5，puzzles的长度小于10^4

分析：
就是求下面的答案
for p in puzzles:
    sum([1 for w in words if w is valid respect to p])

要快速计算对于每个puzzle有多少个word合法，需要对words进行预处理。

构建以'a'-'z'每个字符为根的字典树，每棵树遍历所有word，如果word包含当前根则把它加到树中；把word中不等于根的字符（只处理不同的字符即可）排序，
叶子结点计数加一。

对于每个puzzle，找到以首字母为根的字典树，统计所有字母在puzzle中的word只需要对这颗字典树进行一起全部遍历，



"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        tries = {}
        for key in [chr(ord('a')+i) for i in range(26)]:
            trie = {}
            for w in words:
                if key not in w:
                    continue
                w = [key] + list(sorted(set(list(w))-{key}))
                t = trie
                for c in w:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                if 'count' in t:
                    t['count'] += 1
                else:
                    t['count'] = 1
            if len(trie):
                tries[key] = trie


        def dfs(trie, word):
            ans = trie['count'] if 'count' in trie else 0
            for w in word:
                if w in trie:
                    ans += dfs(trie[w], word)
            return ans

        ans = []
        for w in puzzles:
            key = w[0]
            w = set(list(w[1:]))
            if key in tries:
                trie = tries[key][key]
                ans.append(dfs(trie, w))
            else:
                ans.append(0)

        return ans


s = Solution()
print(s.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"],
                            puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))

print(s.findNumOfValidWords(["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))
