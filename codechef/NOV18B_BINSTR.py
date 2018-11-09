# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/7/18

5 4
100
101
1
1011
11
2 3 10
1 5 1100
3 5 1010
1 5 11100

"""

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())
Q = []
for i in range(M):
    l, r, v = input().split()
    Q.append((int(l), int(r), v))

# import random
# import time
# N, M = 10**5, 10**5
# A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))]) for _ in range(N)]
# Q = []
# for i in range(M):
#     l = random.randint(1, N // 2)
#     r = random.randint(l, N)
#     v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))])
#     Q.append((l, r, v))
#
# print('starting')
# import time
# t0 = time.time()

tree = {'c': [], 'v': ''}


def buildTree(num, idx, numLen):
    t = tree
    # left side should have x zeros
    x = numLen - len(num)

    for di in range(numLen):
        d = num[di - x] if di >= x else '0'
        t['c'].append(idx)

        if d in t:
            t = t[d]
        else:
            t[d] = {'c': [], 'v':''}
            t = t[d]

    t['c'].append(idx)


def compressTree(tree):
    if not tree:
        return

    c0 = tree['0'] if '0' in tree else None
    c1 = tree['1'] if '1' in tree else None
    if c0 and c1:
        compressTree(c0)
        compressTree(c1)
    elif c0:
        cc0 = c0['0'] if '0' in c0 else None
        cc1 = c0['1'] if '1' in c0 else None

        tree['v'] += '0' + c0['v']
        del tree['0']
        if cc0:
            tree['0'] = cc0
        if cc1:
            tree['1'] = cc1
        compressTree(tree)
    elif c1:
        cc0 = c1['0'] if '0' in c1 else None
        cc1 = c1['1'] if '1' in c1 else None

        tree['v'] += '1' + c1['v']
        del tree['1']
        if cc0:
            tree['0'] = cc0
        if cc1:
            tree['1'] = cc1
        compressTree(tree)
    else:
        pass






MXD = max([len(x) for x in A])
for i, v in enumerate(A):
    buildTree(v, i + 1, MXD)


# import json
# print(json.dumps(tree))

compressTree(tree)
# print(json.dumps(tree))

def check(l, r, idx):
    if not idx:
        return False

    if idx[0] > r or idx[-1] < l:
        return False

    if l <= idx[0] <= idx[-1] <= r:
        return True

    # idx is sorted
    a, b = 0, len(idx)
    while a < b:
        c = (a + b) // 2
        v = idx[c]
        if l <= v <= r:
            return True
        if v < l:
            a = c + 1
        elif v > r:
            b = c

    return False


def find(l, r, idx):
    a, b = 0, len(idx)

    while a < b:
        c = (a + b) // 2
        v = idx[c]
        if v < l:
            a = c + 1
        elif v > r:
            b = c
        else:
            b = c

    return idx[a]


def query(l, r, val, maxLen):
    vl = len(val)
    if vl > maxLen:
        val = val[vl - maxLen:]
    elif vl < maxLen:
        val = '0' * (maxLen-vl) + val

    vi = 0
    t = tree
    while vi < len(val):
        tidx = t['c']
        if len(tidx) <= 1:
            break

        v = val[vi]
        u = '1' if v == '0' else '0'
        tv = t['v']
        if tv:
            vi += len(tv) + 1
        else:
            if u in t and check(l, r, t[u]['c']):
                t = t[u]
                vi += 1
            else:
                if v in t and check(l, r, t[v]['c']):
                    t = t[v]
                else:
                    break
                vi += 1

    return find(l, r, t['c'])


ans = []
for l, r, v in Q:
    ans.append(query(l, r, v, MXD))

print('\n'.join(map(str, ans)))

# print(time.time() - t0)






