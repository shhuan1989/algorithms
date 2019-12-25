# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        behaviorByName = collections.defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            behaviorByName[u].append((t, w))
        
        wc = collections.defaultdict(int)
        
        for k, v in behaviorByName.items():
            v.sort()
            nv = len(v)
            pattern = set()
            pa, pb = set(), set()
            for i in range(nv):
                a = v[i][1]
                if a in pa:
                    continue
                pa.add(a)
                for j in range(i+1, nv):
                    b = v[j][1]
                    if (a, b) in pb:
                        continue
                    pb.add((a, b))
                    for k in range(j+1, nv):
                        pattern.add((a, b, v[k][1]))
            for p in pattern:
                wc[p] += 1
                
        wc = list(sorted([(-v, k) for k, v in wc.items()]))
        
        return list(wc[0][1])
        
        
        
        
s = Solution()
# print(s.mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
#                            timestamp = [1,2,3,4,5,6,7,8,9,10],
#                            website = ["home","about","career","home","cart","maps","home","home","about","career"]))
#
# print(s.mostVisitedPattern(["u1","u1","u1","u2","u2","u2"],
#                            [1,2,3,4,5,6],
#                            ["a","b","a","a","b","c"]))
#
# print(s.mostVisitedPattern(
#     ["him","mxcmo","jejuvvtye","wphmqzn","uwlblbrkqv","flntc","esdtyvfs","nig","jejuvvtye","nig","mxcmo","flntc","nig","jejuvvtye","odmspeq","jiufvjy","esdtyvfs","mfieoxff","nig","flntc","mxcmo","qxbrmo"],
#     [113355592,304993712,80831183,751306572,34485202,414560488,667775008,951168362,794457022,813255204,922111713,127547164,906590066,685654550,430221607,699844334,358754380,301537469,561750506,612256123,396990840,60109482],
#     ["k","o","o","nxpvmh","dssdnkv","kiuorlwdcw","twwginujc","evenodb","qqlw","mhpzoaiw","jukowcnnaz","m","ep","qn","wxeffbcy","ggwzd","tawp","gxm","pop","xipfkhac","weiujzjcy","x"]))


print(s.mostVisitedPattern(
["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],
[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],
["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"],
))

t0 = time.time()
print(s.mostVisitedPattern(
["wg","xoyvzjbuzn","oiixbxpef","gkun","x","esyihndjg","lstgdb","dpssyx","fmj","s","olgqy","xgqspowmwj","owzqazkuwq","vfmvfpszde","n","egqfqtjs","tcnixa","mgam","ipddzonk","raav","tkgf","etpaauv","yf","luyt","byeehkbj","z","ulyhywvbtl","lgnqgyu","mb","vcygurmglw","zqctasfwct","egqfqtjs","cefzbh","nkbpxydcnq","ulyhywvbtl","uuhudi","xvlbbpr","zhorx","wbmgdzdc","wvusgl","jopx","wghx","ulyhywvbtl","qvrsyizu","orgxsqr","tcnixa","ll","wamcvtmw","omivknvsa","vy"],
[880580508,327947572,860469996,253202214,314231208,251383500,27336842,164311485,63132749,420110822,957334660,783883562,619742355,546371329,332455362,983298136,478967282,110515807,40798916,713843643,434895079,544202524,673983763,702894419,221502228,353376203,446299604,554900684,755363857,995023004,402591433,783528707,659688176,671748189,339202386,505856752,187369168,139774540,533708824,666585928,445919115,617270260,182115790,224647776,66571485,911899309,670,981055,11145784,148496215,638806483],
["gnopixcgor","otzo","crohg","tsgcxrk","i","vhfcahmowm","isdc","smd","tfr","qnucvwjnp","xwjsbky","xhuf","mhcj","w","wdat","hgnqswdmet","hfoudetjl","xxjcvminh","oupiwrm","zu","htki","vkxernxm","ofzx","phbbpbteof","dw","zs","qe","mvjg","jw","hyrp","prwwydmgnw","qe","x","gylgkv","iqxpdova","erqmeli","lyq","bthnbn","fu","kwcfgp","emithrtn","b","nxfm","bdxpeuhllz","iqxpdova","gylgkv","xvungbz","gdmtirynk","wef","koxjv"]
))
print(time.time() - t0)