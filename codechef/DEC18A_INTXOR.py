# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/11/18

"""
import sys

import collections
# import random
#
#
T = int(input())
# T = 1000000
for ti in range(T):
    N = int(input())
    # N = 11
    # N = random.randint(8, 1000)
    # N = ti + 8
    # vals = [0] + [random.randint(1, 1000) for _ in range(N)]
    ans = []
    
    count = 0
    scount = collections.defaultdict(int)
    mxn = 0
    if N == 11:
      mxn = 1
    elif N % 4 == 0:
        mxn = N // 4
    elif N % 4 == 1:
        mxn = max(N // 4 - 1, 0)
    elif N % 4 == 2:
        mxn = max(N // 4 - 2, 0)
    elif N % 4 == 3:
        mxn = max(N // 4 - 3, 0)
        
    for n in range(mxn):
        A = []
        for ijk in [(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)]:
            print('1 {}'.format(' '.join(map(str, [x + 4*n for x in ijk]))))
            sys.stdout.flush()
            count += 1
            for i in [x + 4*n for x in ijk]:
                scount[i] += 1
            v = int(input())
            if v == -1:
                exit(0)
            A.append(v)
            # a = [vals[x + 4*n] for x in ijk]
            # A.append(a[0] ^ a[1] ^ a[2])
            
        
        a3 = A[0] ^ A[1] ^ A[2]
        a12 = A[0] ^ a3
        a24 = A[1] ^ a3
        a14 = A[2] ^ a3
        a4 = a12 ^ A[3]
        a1 = a14 ^ a4
        a2 = a12 ^ a1
        ans.extend([a1, a2, a3, a4])
    if N == 11:
        ijks = []
        for i in range(5, 10):
            ijks.append((i, i + 1, i + 2))
        ijks.append((10, 11, 5))
        ijks.append((11, 5, 6))
        
        vis = {}
        for ijk in ijks:
            print('1 {}'.format(' '.join(map(str, ijk))))
            v = int(input())
            if v == -1:
                exit(0)
            vis[ijk] = v
            for i in ijk:
                scount[i] += 1
            count += 1
            # a = [vals[i] for i in ijk]
            # vis[ijk] = a[0] ^ a[1] ^ a[2]
    
        q = ijks
        while q:
            b = q.pop()
            add = {}
            for c in vis:
                d = tuple(set(b).symmetric_difference(set(c)))
                dv = vis[b] ^ vis[c]
            
                if d and d not in vis:
                    add[d] = dv
                    q.append(d)
            
            for d, v in add.items():
                vis[d] = v
        
        ans.extend([vis[(i, )] for i in range(5, 12)])
        
    elif N % 4 != 0:
        # n = mxn
        s = 4 * mxn
        n = 0
        for i in range((N-4*mxn) // 5):
            A = []
            for ijk in [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 1), (5, 1, 2)]:
                print('1 {}'.format(' '.join(map(str, [x + 5 * n + s for x in ijk]))))
                for i in [x + 5 * n + s for x in ijk]:
                    scount[i] += 1
                sys.stdout.flush()
                count += 1
                v = int(input())
                if v == -1:
                    exit(0)
                A.append(v)
                # a = [vals[x + 5 * n + s] for x in ijk]
                # A.append(a[0] ^ a[1] ^ a[2])
            
            a5 = A[0] ^ A[1] ^ A[3]
            a3 = A[4] ^ a5 ^ A[0]
            a4 = A[2] ^ a3 ^ a5
            a2 = A[1] ^ a3 ^ a4
            a1 = A[0] ^ a2 ^ a3
            ans.extend([a1, a2, a3, a4, a5])
            n += 1
            
    print('2 {}'.format(' '.join(map(str, ans))))
    ok = int(input())
    
    # print(ans)
    # print(vals[1:])
    # print(vals[1:] == ans)
    # print(ans)
    # print(ti)
    # if vals[1:] != ans:
    #     print(vals[1:])
    #     exit(0)
    # if count > N:
    #     print('{} greater than {}'.format(count, N))
    #     print(vals[1:])
    #     exit(0)
    # if any([x > 3 for x in scount.values()]):
    #     print('some thing great than 3')
    #     print(vals[1:])
    #     exit(0)
    