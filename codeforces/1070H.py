# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/3/18

"""

import collections

N = int(input())

subs = collections.defaultdict(int)
subi = collections.defaultdict(int)
files = []
for fi in range(N):
    f = input()
    files.append(f)
    ss = set()
    for i in range(len(f)):
        for j in range(i+1, len(f)+1):
            s = f[i: j]
            ss.add(s)
            subi[s] = fi
    for s in ss:
        subs[s] += 1
    
    
Q = int(input())
qs = [input() for _ in range(Q)]

ans = []
for s in qs:
    count = subs[s]
    af = files[subi[s]] if count > 0 else '-'
    ans.append('{} {}'.format(count, af))
    
print('\n'.join(ans))