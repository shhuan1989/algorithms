# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/7/18

5 4
0100
0101
0001
0011
101100110001011
2 3 10
1 5 1100
3 5 1010
1 5 11100

"""

# N, M = map(int, input().split())
# A = []
# for i in range(N):
#     A.append(input())
# Q = []
# for i in range(M):
#     l, r, v = input().split()
#     Q.append((int(l), int(r), v))

# import random
# import time
# N, M = 10**5, 10**5
# A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1000 if i < 10 else 1, 2000 if i < 10 else 20))]) for i in range(N)]
# Q = []
# for i in range(M):
#     l = random.randint(1, N // 2)
#     r = random.randint(l, N)
#     v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1000 if i < 10 else 1, 20000 if i < 10 else 20))])
#     Q.append((l, r, v))


N, M = 5, 4
A = ['0100', '0101', '0001', '0011', '101100110001011']
Q = [(2, 3, '10'), (1, 5, '1100'), (3, 5, '1010'), (1, 5, '11100')]

print('starting')
import time
t0 = time.time()

tree = {'c': [], 'v': ''}


def buildTree(num, idx, numLen):
    t = tree
    ln = len(num)
    if ln < numLen:
        num = '0' * (numLen-ln) + num
    
    di = 0
    while di < numLen:
        u = num[di]
        ru = '1' if u == '0' else '0'
        tv = t['v']
        if tv:
            vi = 0
            while vi < len(tv) and tv[vi] == num[di+vi]:
                vi += 1
            if vi >= len(tv):
                di = di+len(tv)
                if di < len(num):
                    t['c'].append(idx)
                    u = num[di]
                    if u in t:
                        t = t[u]
                        di += 1
                    else:
                        t[u] = {'c': [idx], 'v': num[di+1:]}
                        return
            else:
                # split
                t['v'] = tv[:vi]
                
                c0 = t['0'] if '0' in t else None
                c1 = t['1'] if '1' in t else None
                tvi = tv[vi]
                t[tvi] = {'c': [x for x in t['c']], 'v': tv[vi+1:]}
                if c0:
                    t[tvi]['0'] = c0
                if c1:
                    t[tvi]['1'] = c1
                t[num[di+vi]] = {'c': [idx], 'v': num[di+vi+1:]}
                t['c'].append(idx)
                return
        else:
            t['c'].append(idx)
            if u in t:
                t = t[u]
                di += 1
            elif ru in t:
                t[u] = {'c': [idx], 'v': num[di+1:]}
                return
            else:
                t['v'] = num[di:]
                return
            

MXD = max([len(x) for x in A])
for i, v in enumerate(A):
    buildTree(v, i + 1, MXD)

print('tree built', time.time() - t0)

import json
print(json.dumps(tree))
# print(json.dumps(tree))
#


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


def query(l, r, num):
    ln = len(num)
    if ln > MXD:
        num = num[ln-MXD:]
    else:
        num = '0' * (MXD-ln) + num
    
    di = 0
    t = tree
    while di < MXD:
        if len(t['c']) <= 1:
            break
            
        tv = t['v']
        u = num[di]
        ru = '0' if u == '1' else '1'
        if tv:
            di += len(tv)
        else:
            if ru in t and check(l, r, t[ru]['c']):
                t = t[ru]
                di += 1
            elif u in t and check(l, r, t[u]['c']):
                t = t[u]
                di += 1
            else:
                break
    
    return find(l, r, t['c'])
    
    

def query2(l, r, num):
    t = tree
    x = MXD - len(num)
    for di in range(MXD):
        d = num[di - x] if di >= x else '0'
        rev = '0' if d == '1' else '1'
        
        t0 = t[d] if d in t else None
        t1 = t[rev] if rev in t else None
        
        if not t0 and not t1:
            break
        elif not t0:
            if check(l, r, t1['c']):
                t = t1
            else:
                break
        elif not t1:
            if check(l, r, t0['c']):
                t = t0
            else:
                break
        else:
            if check(l, r, t1['c']):
                # if some id in t1 between l and r
                t = t1
            elif check(l, r, t0['c']):
                # if some id in t0 between l and r
                t = t0
            else:
                break
    
    return find(l, r, t['c'])


ans = []
for l, r, v in Q:
    ans.append(query(l, r, v))

print('\n'.join(map(str, ans)))

print(time.time() - t0)
