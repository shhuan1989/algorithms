# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/10 11:05

"""

from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def dfs(words, letters, scores, index, prescore):
            if index >= len(words):
                return prescore

            # combine word
            word = words[index]
            wc = collections.Counter(word)
            ans = 0
            if all([ch in letters and letters[ch] >= wc[ch] for ch in word]):
                scoreAdded = sum([scores[ch] for ch in word])
                nextLetters = {k: v-wc[k] for k, v in letters.items()}
                ans = dfs(words, nextLetters, scores, index+1, prescore+scoreAdded)
            ans = max(ans, dfs(words, letters, scores, index+1, prescore))

            return ans

        scores = {}
        for i in range(26):
            ch = chr(i+ord('a'))
            scores[ch] = score[i]

        ans = dfs(words, collections.Counter(letters), scores, 0, 0)

        return ans


s = Solution()
print(s.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
print(s.maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
print(s.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))