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

# N, M = map(int, input().split())
# A = []
# for i in range(N):
#     A.append(input())
# Q = []
# for i in range(M):
#     l, r, v = input().split()
#     Q.append((int(l), int(r), v))


def readInput():
    f = open('input2.txt', 'r')
    N, M = map(int, f.readline().strip().split())
    A, Q = [], []
    for i in range(N):
        A.append(f.readline().strip())
    
    for i in range(M):
        l, r, v = f.readline().strip().split()
        Q.append((int(l), int(r), v))
    
    f.close()
    
    return N, Q, A, Q


# N, M, A, Q = genInput(10, 10, False)
# print(N, M)
# print('\n'.join(A))
# for q in Q:
#     print(' '.join(map(str, q)))
# print('===============')

N, M, A, Q = readInput()


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

tree = {'c': []}


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
            t[d] = {'c': []}
            t = t[d]
    
    t['c'].append(idx)


MXD = max([len(x) for x in A])
for i, v in enumerate(A):
    buildTree(v, i + 1, MXD)


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

# print(time.time() - t0)






