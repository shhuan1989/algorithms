# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

N = int(input())
S = [int(x) for x in list(input())]

wc = collections.Counter(S)

for v in [0, 1, 2]:
    if v not in wc:
        wc[v] = 0

counts = [(c, w) for w, c in wc.items()]
counts.sort()



d = N // 3

ca, a = counts[0]
cb, b = counts[1]
cc, c = counts[2]

ai = [i for i in range(N) if S[i] == a]
bi = [i for i in range(N) if S[i] == b]
ci = [i for i in range(N) if S[i] == c]

if ca == d and cb == d:
    print(''.join(map(str, S)))
elif ca <= d and cb <= d:
    s1 = [x for x in S]
    for i in ci[:d-ca]:
        s1[i] = a
    for i in ci[d-ca:2*d-ca-cb]:
        s1[i] = b
        
    s2 = [x for x in S]
    for i in ci[:d-cb]:
        s2[i] = b
    for i in ci[d-cb:2*d-ca-cb]:
        s2[i] = a
    
    s3 = [x for x in S]
    for i in ci[cc-d+ca:]:
        s3[i] = a
    for i in ci[cc-2*d+cb+ca:cc-d+ca]:
        s3[i] = b
        
    s4 = [x for x in S]
    for i in ci[cc-d+cb:]:
        s4[i] = b
    for i in ci[cc-2*d+cb+ca:cc-d+cb]:
        s4[i] = a
    
    s5 = [x for x in S]
    for i in ci[:d-ca]:
        s5[i] = a
    for i in ci[cc-d+cb:]:
        s5[i] = b
        
    s6 = [x for x in S]
    for i in ci[:d-cb]:
        s6[i] = b
    for i in ci[cc-d+ca:]:
        s6[i] = a
    
    ss = [''.join(map(str, s)) for s in [s1, s2, s3, s4, s5, s6]]
    ss.sort()
    print(ss[0])
    
else:
    # ca < d cb > d cc > d
    
    cmb = cb-d
    cmc = cc-d
    
    s1 = [x for x in S]
    for i in bi[:cmb]:
        s1[i] = a
    for i in ci[:cmc]:
        s1[i] = a

    s2 = [x for x in S]
    for i in bi[cb-cmb:]:
        s2[i] = a
    for i in ci[:cmc]:
        s2[i] = a

    s3 = [x for x in S]
    for i in bi[:cmb]:
        s3[i] = a
    for i in ci[cc-cmc:]:
        s3[i] = a

    s4 = [x for x in S]
    for i in bi[cb-cmb:]:
        s4[i] = a
    for i in ci[cc-cmc:]:
        s4[i] = a

    ss = [''.join(map(str, s)) for s in [s1, s2, s3, s4]]
    ss.sort()
    print(ss[0])
        
