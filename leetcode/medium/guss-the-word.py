# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self, secret):
        self.secret = secret
        self.t = 0
        
    def guess(self, word: str) -> int:
        self.t += 1
        print('guess', word, self.t)
        match = len([1 for a, b in zip(word, self.secret) if a == b])
        if match == len(word):
            print('bingo', self.t)
        
        return match


class Solution:
    def findSecretWord(self, wordlist: List[str], master: Master) -> None:
        guessed = set()
        
        def diff(a, b):
            return len([1 for u, v in zip(list(a), list(b)) if v == u])
        
        def choose(words):
            n = len(words)
            distance = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    distance[i][j] = diff(words[i], words[j])
                    distance[j][i] = distance[i][j]
            
            wi, wc = -1, 10000
            for i in range(n):
                distance[i].sort()
                ds = len(collections.Counter(distance[i]))
                if ds < wc:
                    wc = ds
                    wi = i
                    
            return words[wi]
            
            
            
        
            
        
        
            
        def dfs(words):
            if not words:
                return False
            
            print(len(words))
            
            word = choose(words)
            nw = len(word)
            guessed.add(word)
            m = max(master.guess(word), 0)
            if m == nw:
                return True
            
            return dfs([w for w in words if diff(w, word) == m])
            
            
        dfs(wordlist)
        
    
    

# m = Master('acckzz')
# s = Solution()
# s.findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], m)

# m = Master("hbaczn")
# s = Solution()
# print(s.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], m))

# m = Master("hbaczn")
# s = Solution()
# t0 = time.time()
# print(s.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], m))
# print(time.time() - t0)

m = Master("cymplm")
s = Solution()
print(s.findSecretWord(["eykdft","gjeixr","eksbjm","mxqhpk","tjplhf","ejgdra","npkysm","jsrsid","cymplm","vegdgt","jnhdvb","jdhlzb","sgrghh","jvydne","laxvnm","xbcliw","emnfcw","pyzdnq","vzqbuk","gznrnn","robxqx","oadnrt","kzwyuf","ahlfab","zawvdf","edhumz","gkgiml","wqqtla","csamxn","bisxbn","zwxbql","euzpol","mckltw","bbnpsg","ynqeqw","uwvqcg","hegrnc","rrqhbp","tpfmlh","wfgfbe","tpvftd","phspjr","apbhwb","yjihwh","zgspss","pesnwj","dchpxq","axduwd","ropxqf","gahkbq","yxudiu","dsvwry","ecfkxn","hmgflc","fdaowp","hrixpl","czkgyp","mmqfao","qkkqnz","lkzaxu","cngmyn","nmckcy","alpcyy","plcmts","proitu","tpzbok","vixjqn","suwhab","dqqkxg","ynatlx","wmbjxe","hynjdf","xtcavp","avjjjj","fmclkd","ngxcal","neyvpq","cwcdhi","cfanhh","ruvdsa","pvzfyx","hmdmtx","pepbsy","tgpnql","zhuqlj","tdrsfx","xxxyle","zqwazc","hsukcb","aqtdvn","zxbxps","wziidg","tsuxvr","florrj","rpuorf","jzckev","qecnsc","rrjdyh","zjtdaw","dknezk"], m))