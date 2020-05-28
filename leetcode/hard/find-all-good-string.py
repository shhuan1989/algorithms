# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/26

https://oi-wiki.org/dp/number/

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
    
        # prefix function
        # https://cp-algorithms.com/string/prefix-function.html
        m, pi = len(evil), [0] * len(evil)
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j
        
        MOD = 10 ** 9 + 7
        
        ans = 1 if s2.find(evil) < 0 else 0
        
        def find_impl(s: List[int], es: List[int]) -> int:
            n = len(s)
            
            def find_prefix(wa, wb):
                for i in range(len(a), 0, -1):
                    if wa[-i:] == wb[:i]:
                        return i

                return 0
            
            @lru_cache(maxsize=None)
            def cal(wordlen: int, pre: int) -> int:
                if wordlen < 0 or pre >= len(es):
                    return 0
                
                if wordlen == 0:
                    return 1
                
                count = cal(wordlen-1, pre + 1)

                # for i in range(26):
                #     if i == es[pre]:
                #         continue
                #     sub = es[:pre] + [i]
                #     count += cal(wordlen - 1, find_prefix(sub, es))
                
                for i in range(26):
                    if i == es[pre]:
                        continue

                    # sub = es[:pre] + [i]
                    # p0 = find_prefix(sub, es)
                    if pre > 0:
                        p = pi[pre-1]
                        while p > 0 and es[p] != i:
                            p = pi[p-1]
                        p = p + 1 if es[p] == i else p
                        count += cal(wordlen-1, p)
                    else:
                        count += cal(wordlen-1, 0)
                
                return count
            
            def dfs(index: int, state: int, op: int) -> int:
                if index >= len(s) - 1:
                    return 1 if op and state < len(es) else 0
                
                if state >= len(es):
                    return 0
                
                if op == 1:
                    # less
                    return cal(n - index - 1, state)
                else:
                    # equal
                    count = dfs(index + 1,
                                (state + 1) if s[index + 1] == es[state] else (1 if s[index + 1] == es[0] else 0), 0)
                    for i in range(s[index + 1]):
                        count += dfs(index + 1, (state + 1) if i == es[state] else (1 if i == es[0] else 0), 1)
                        count %= MOD
                    
                    return count
            
            ans = dfs(0, 1 if s[0] == es[0] else 0, 0)
            for i in range(s[0]):
                ans += dfs(0, 1 if i == es[0] else 0, 1)
                ans %= MOD
            
            return ans % MOD
        
        a = [ord(v) - ord('a') for v in s1]
        b = [ord(v) - ord('a') for v in s2]
        es = [ord(v) - ord('a') for v in evil]
        
        # print(find_impl(a, es))
        # print(find_impl(b, es))
        # print(ans)
        # print(ans, find_impl(b, es), find_impl(a, es))
        ans += find_impl(b, es) + MOD - find_impl(a, es)
        ans %= MOD

        return max(ans, 0)
    
    def brutal_less(self, n, s, evil):
        def dfs(index, curr):
            if index >= n:
                return 1 if curr < s and curr.find(evil) < 0 else 0
        
            if curr.find(evil) >= 0:
                return 0
        
            ans = 0
            for i in range(26):
                ans += dfs(index + 1, curr + chr(ord('a') + i))
        
            return ans
        
        return dfs(0, '')
        
        
    
    def brutal(self, n: int, s1: str, s2: str, evil: str) -> int:
    
        # a = [ord(v) - ord('a') for v in s1]
        # b = [ord(v) - ord('a') for v in s2]
        # es = [ord(v) - ord('a') for v in evil]
        
        def dfs(index, curr):
            if index >= n:
                return 1 if s1 <= curr <= s2 and curr.find(evil) < 0 else 0
            
            if curr.find(evil) >= 0:
                return 0
            
            ans = 0
            for i in range(26):
                ans += dfs(index + 1, curr + chr(ord('a') + i))
                
            return ans
        
        
        return dfs(0, '')
        
        
        
        
        


s = Solution()

# print(s.brutal(7, "serssfw", "vabgoyt", "bmgld"))
print(s.findGoodStrings(7, "serssfw", "vabgoyt", "bmgld"))

print(s.findGoodStrings(67, "ioxczeqszwxlumokqaihefntzridiuqczuqalwjgpnvrzxigxyqctzsbogwurjxyurq", "ylmsbbpihskzljtrfevsdyxbdvwgcsucgfnspzhtholgpcnarmpmqsnlajwadqkrsjn", "qntusjojeqoseryfiuanxvsblnmjvyvacca"))

# import random
# for n in range(2, 5):
#     for _ in range(100):
#         s1 = ''.join([chr(ord('a') + random.randint(0, 25)) for _ in range(n)])
#         s2 = ''.join([chr(ord('a') + random.randint(0, 25)) for _ in range(n)])
#         en = random.randint(1, n)
#         eveil = ''.join([chr(ord('a') + random.randint(0, 25)) for _ in range(en)])
#
#         if s.brutal(n, s1, s2, eveil) != s.findGoodStrings(n, s1, s2, eveil):
#             print(s.brutal(n, s1, s2, eveil), s.findGoodStrings(n, s1, s2, eveil))
#             print(n, s1, s2, eveil)
#
#             exit(0)

# print(s.brutal_less(3, 'aea', 'hn'), s.brutal_less(3, 'jzd', 'hn'))
print(s.findGoodStrings(3, 'aea', 'jzd', 'hn'))
print(s.brutal(3, 'aea', 'jzd', 'hn'))
# print(s.findGoodStrings(8, "pzdanyao", "wgpmtywi", "sdka"))
# print(s.findGoodStrings(2, 'aa', 'da', 'b'))
# print(s.findGoodStrings(8, 'leetcode', 'leetgoes', 'leet'))
# print(s.findGoodStrings(2, 'gx', 'gz', 'x'))