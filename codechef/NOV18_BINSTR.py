# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/7/18


5 4
0100
0101
0001
1011
0011
2 3 10
1 5 1100
3 5 1010
1 5 11100


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

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())
Q = []
for i in range(M):
    l, r, v = input().split()
    Q.append((int(l), int(r), v))

import random
# import time
def genInput(N, M, large=False):
    if large:
        A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in
                            range(random.randint(1000 if i < 10 else 1, 2000 if i < 10 else 20))]) for i in range(N)]
        Q = []
        for i in range(M):
            l = random.randint(1, N // 2)
            r = random.randint(l, N)
            v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in
                               range(random.randint(1000 if i < 10 else 1, 20000 if i < 10 else 20))])
            Q.append((l, r, v))
        return N, M, A, Q
    else:
        A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(1, random.randint(1, 20))]) for _ in range(N)]
        Q = []
        for i in range(M):
            l = random.randint(1, N // 2)
            r = random.randint(l, N)
            v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))])
            Q.append((l, r, v))
        return N, M, A, Q
        
# def readInput():
#     f = open('input.txt', 'r')
#     N, M = map(int, f.readline().split())
#     A, Q = [], []
#     for i in range(N):
#         A.append(f.readline().strip())
#
#     for i in range(M):
#         l, r, v = f.readline().strip().split()
#         Q.append((int(l), int(r), v))
#
#     f.close()
#
#     # print('{} {}'.format(N, M))
#     # print('\n'.join(A))
#     # for l, r, v in Q:
#     #     print('{} {} {}'.format(l, r, v))
#     # print('#' * 40)
#     return N, Q, A, Q
# N, M, A, Q = genInput(10, 10, False)
# print(N, M)
# print('\n'.join(A))
# for q in Q:
#     print(' '.join(map(str, q)))
# print('===============')

# N, M, A, Q = readInput()


# N, M = 5, 4
# A = ['0100', '0101', '0001', '0011', '101100110001011']
# Q = [(2, 3, '10'), (1, 5, '1100'), (3, 5, '1010'), (1, 5, '11100')]
#
# print('starting')
# t0 = time.time()

tree = {'c': [], 'v': [], 'vl': 0}


def compressStr(num, maxLen):
    ans = []
    ln = len(num)
    if ln < maxLen:
        ans.append((maxLen-ln, '0'))
    elif ln > maxLen:
        num = num[ln-maxLen:]
    
    i, j = 0, 0
    while j < len(num):
        if num[j] != num[i]:
            ans.append((j-i, num[i]))
            i = j
        j += 1
    ans.append((j-i, num[i]))
    if len(ans) > 1 and ans[0][1] == ans[1][1]:
        ans[:2] = [(ans[0][0] + ans[1][0], ans[0][1])]
    
    return ans


# print('===========compress==============')
# print(compressStr('101010100101', 100))
# print(compressStr('1111111', 100))
# print(compressStr('0000011111', 100))
# print(compressStr('00011001100011', 100))
# print(compressStr('00011001100011', 5))
# print(compressStr('11', 10))
# print('===========compress==============')


def diffCompressedStr(u, v):
    ui, vi = 0, 0
    same = []
    while ui < len(u) and vi < len(v):
        if u[ui][1] == v[vi][1]:
            if u[ui][0] == v[vi][0]:
                same.append((u[ui][0], u[ui][1]))
                ui += 1
                vi += 1
            elif u[ui][0] < v[vi][0]:
                same.append((u[ui][0], u[ui][1]))
                v[vi] = (v[vi][0]-u[ui][0], v[vi][1])
                ui += 1
            else:
                same.append((v[vi][0], v[vi][1]))
                u[ui] = (u[ui][0]-v[vi][0], u[ui][1])
                vi += 1
        else:
            break
    
    return same, u[ui:], v[vi:]


# print("============diff=============")
# print(diffCompressedStr([], [(8, '1'), (12, '0')]))
# print(diffCompressedStr([(2, '1')], [(8, '1'), (12, '0')]))
# print(diffCompressedStr([(2, '0')], [(8, '1'), (12, '0')]))
# print(diffCompressedStr([(10, '1'), (12, '0')], []))
# print(diffCompressedStr([(10, '1'), (12, '0')], [(2, '1')]))
# print(diffCompressedStr([(10, '1'), (12, '0')], [(2, '0')]))
# print(diffCompressedStr([(10, '1'), (12, '0')], [(8, '1'), (12, '0')]))
# print(diffCompressedStr([(10, '1'), (12, '0')], [(12, '1'), (12, '0')]))
# print(diffCompressedStr([(10, '1'), (12, '0'), (22, '1')], [(10, '1'), (12, '0'), (12, '1')]))
#
# print("============diff=============")


def popLeft(num, count=1):
    c = 0
    for i in range(len(num)):
        if c + num[i][0] > count:
            return [(num[i][0]-count+c, num[i][1])] + num[i+1:]
        else:
            c += num[i][0]
    
    return []


# print('=' * 80)
#
# print(popLeft([(3, '0'), (4, '1')], 1))
# print(popLeft([(3, '0'), (4, '1')], 3))
# print(popLeft([(3, '0'), (4, '1')], 5))
# print(popLeft([(3, '0'), (4, '1')], 10))
# print(popLeft([(3, '0'), (4, '1')], 0))
# print(popLeft([(3, '0'), (4, '1')], 20))
#
# print('=' * 80)

def rev(val):
    return '1' if val == '0' else '0'


def buildTree(num, idx, numLen):
    t = tree
    num = compressStr(num, numLen)
    while num:
        tv = t['v']
        same, vleft, num = diffCompressedStr(tv, num)
        if not vleft:
            if num:
                u = num[0][1]
                ru = rev(u)
                if u in t:
                    t['c'].append(idx)
                    t = t[u]
                    num = popLeft(num, 1)
                elif ru in t:
                    t[u] = {'c': [idx], 'v': popLeft(num, 1)}
                else:
                    t['c'].append(idx)
                    t['v'] = num
                    return
            else:
                t['c'].append(idx)
                return
        else:
            # split
            c0 = t['0'] if '0' in t else None
            c1 = t['1'] if '1' in t else None

            v0 = vleft[0][1]
            n0 = num[0][1]

            t[n0] = {'c': [idx], 'v': popLeft(num, 1)}
            t[v0] = {'c': [x for x in t['c']], 'v': popLeft(vleft, 1)}

            if c0:
                t[v0]['0'] = c0
            if c1:
                t[v0]['1'] = c1

            t['v'] = same
            t['c'].append(idx)
            return
    t['c'].append(idx)

def computeTreeValLen(t):
    if not t:
        return
    
    if 'v' in t:
        t['vl'] = sum([x[0] for x in t['v']] or [0])
    else:
        t['vl'] = 0
        
    if '0' in t:
        computeTreeValLen(t['0'])
    if '1' in t:
        computeTreeValLen(t['1'])
    

MXD = max([len(x) for x in A])
for i, v in enumerate(A):
    buildTree(v, i + 1, MXD)

computeTreeValLen(tree)


# print('tree built', time.time() - t0)

import json
# print(json.dumps(tree))
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

# print('=======check===========')
# print(check(1, 3, [1, 3, 4, 6]))
# print(check(1, 3, [3, 4, 6]))
# print(check(1, 3, [2, 4, 6]))
# print(check(1, 3, [1, 2]))
# print(check(1, 3, [1, 2, 4]))
# print(check(1, 10, [11, 12]))
# print(check(1, 10, [9, 12]))
# print(check(4, 10, [1, 3]))
# print(check(4, 10, [1, 5]))
# print(check(4, 10, [9, 11]))
# print(check(4, 10, [5, 7]))
# print('=======check===========')


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


# print('=======find===========')
# print(find(1, 3, [1, 3, 4, 6]))
# print(find(1, 3, [3, 4, 6]))
# print(find(1, 3, [2, 4, 6]))
# print(find(1, 3, [1, 2]))
# print(find(1, 3, [1, 2, 4]))
# print(find(1, 10, [9, 12]))
# print(find(4, 10, [1, 5]))
# print(find(4, 10, [9, 11]))
# print(find(4, 10, [5, 7]))
# print('=======find===========')

def query(l, r, num):
    num = compressStr(num, MXD)
    
    t = tree
    while num:
        if len(tree['c']) <= 1:
            break
        if t['v']:
            num = popLeft(num, t['vl'])
            if not num:
                break
                
        a = num[0][1]
        ra = rev(a)
        if ra in t and check(l, r, t[ra]['c']):
            t = t[ra]
            num = popLeft(num, 1)
        elif a in t and check(l, r, t[a]['c']):
            t = t[a]
            num = popLeft(num, 1)
        else:
            break
                
    return find(l, r, t['c'])
    

ans = []
for l, r, v in Q:
    ans.append(query(l, r, v))

print('\n'.join(map(str, ans)))

# print(time.time() - t0)
