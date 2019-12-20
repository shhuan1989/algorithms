# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class WordFilter:
    
    def __init__(self, words: List[str]):
        
        trie = {}
        
        def insert(word, val):
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = val
                
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                for k in range(len(w)+1):
                    insert(w[j:] + '#' + w[:k], i)
                
        self.trie = trie
        
    def f(self, prefix: str, suffix: str) -> int:
        w = suffix + '#' + prefix
        t = self.trie
        for ch in w:
            if ch not in t:
                return -1
            t = t[ch]
        return t['#'] if '#' in t else -1
        
        

# Your WordFilter object will be instantiated and called as such:
# words = ['apple']
# wf = WordFilter(words)
# print(wf.f('a', 'e'))
# print(wf.f('b', ''))


wf = WordFilter(['pop'])
ans = []
for a, b in [["",""],["","p"],["","op"],["","pop"],["p",""],["p","p"],["p","op"],["p","pop"],["po",""],["po","p"],["po","op"],["po","pop"],["pop",""],["pop","p"],["pop","op"],["pop","pop"],["",""],["","p"],["","gp"],["","pgp"],["p",""],["p","p"],["p","gp"],["p","pgp"],["pg",""],["pg","p"],["pg","gp"],["pg","pgp"],["pgp",""],["pgp","p"],["pgp","gp"],["pgp","pgp"]]:
    ans.append(wf.f(a, b))
print(ans)
print([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])