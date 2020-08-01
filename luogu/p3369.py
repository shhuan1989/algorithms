# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/16

"""
import sys
import random
import time
from memory_profiler import profile

INF = 10 ** 9 + 7
MAXN = 10**5+5

class Node:
    def __init__(self, key):
        self.key = key
        self.prior = random.randint(0, 10**9)
        self.left = 0
        self.right = 0
        self.size = 1


tre = [Node(i) for i in range(MAXN)]
tre[0].size = 0


def update(now):
    tre[now].size = tre[tre[now].left].size + tre[tre[now].right].size + 1


def split(now, key):
    if now <= 0:
        return 0, 0

    if tre[now].key > key:
        # split left
        l, r = split(tre[now].left, key)
        tre[now].left = r
        update(now)
        return l, now
    else:
        # split right
        l, r = split(tre[now].right, key)
        tre[now].right = l
        update(now)
        return now, r


def merge(t1, t2):
    if t1 == 0 or t2 == 0:
        return t1 + t2

    if tre[t1].prior <= tre[t2].prior:
        # t1 is root of merged tree
        tre[t1].right = merge(tre[t1].right, t2)
        update(t1)
        return t1
    else:
        # t2 is root of merged tree
        tre[t2].left = merge(t1, tre[t2].left)
        update(t2)
        return t2


def insert(now, node):
    if now <= 0:
        return node

    if tre[now].prior > tre[node].prior:
        # split current tree to L < x, and R > x;
        l, r = split(now, tre[node].key)
        tre[node].left = l
        tre[node].right = r
        update(node)
        return node
    else:
        if tre[now].key >= tre[node].key:
            tre[now].left = insert(tre[now].left, node)
            update(now)
            return now
        else:
            tre[now].right = insert(tre[now].right, node)
            update(now)
            return now


def erase(now, key):
    if now <= 0:
        return 0

    if tre[now].key == key:
        return merge(tre[now].left, tre[now].right)
    elif tre[now].key > key:
        tre[now].left = erase(tre[now].left, key)
        update(now)
        return now
    else:
        tre[now].right = erase(tre[now].right, key)
        update(now)
        return now


def search(now, key):
    if now <= 0:
        return 0

    if tre[now].key == key:
        return now
    elif tre[now].key > key:
        return search(tre[now].left, key)
    else:
        return search(tre[now].right, key)


def searchk(now, k):
    if now <= 0:
        return 0
    lc = (tre[tre[now].left].size if tre[now].left > 0 else 0)
    if lc >= k:
        return searchk(tre[now].left, k)
    elif lc + 1 == k:
        return now
    else:
        return searchk(tre[now].right, k-lc-1)


def searchpre(now, key):
    if now <= 0:
        return 0

    if tre[now].key >= key:
        return searchpre(tre[now].left, key)
    else:
        a = searchpre(tre[now].right, key)
        if a <= 0:
            return now
        else:
            return a

def searchafter(now, key):
    if now <= 0:
        return 0

    if tre[now].key <= key:
        return searchafter(tre[now].right, key)
    else:
        a = searchafter(tre[now].left, key)
        if a <= 0:
            return now
        else:
            return a

def getrank(now, key, add):
    if now <= 0:
        return add + 1

    lc = (tre[tre[now].left].size if tre[now].left > 0 else 0)
    # attention equal case
    if tre[now].key >= key:
        return getrank(tre[now].left, key, add)
    else:
        return getrank(tre[now].right, key, add + lc + 1)


def check(now):
    if now <= 0:
        return True

    if tre[now].left > 0 and tre[tre[now].left].prior < tre[now].prior:
        return False

    if tre[now].right > 0 and tre[tre[now].right].prior < tre[now].prior:
        return False



    return True


def checksize(now):
    if now <= 0:
        return tre[now].size == 0

    if tre[now].size != tre[tre[now].left].size + tre[tre[now].right].size + 1:
        return False

    return checksize(tre[now].left) and checksize(tre[now].right)


def inorder(now):
    if now <= 0:
        return []

    return inorder(tre[now].left) + [tre[now].key] + inorder(tre[now].right)


def main():
    sys.stdin = open('P3369_7.in', 'r')
    t0 = time.time()
    N = int(input())
    ans = []
    ansb = []
    id = 1
    root = 0
    for i in range(N):
        ops = [int(x) for x in input().strip().split()]
        op = ops[0]
        x = ops[1]
        if op == 1:
            tre[id].key = x
            root = insert(root, id)
            id += 1
        elif op == 2:
            root = erase(root, x)
        elif op == 3:
            ans.append(getrank(root, x, 0))
            ansb.append(op)
        elif op == 4:
            ans.append(tre[searchk(root, x)].key)
            ansb.append(op)
        elif op == 5:
            ans.append(tre[searchpre(root, x)].key)
            ansb.append(op)
        elif op == 6:
            ans.append(tre[searchafter(root, x)].key)
            ansb.append(op)

    print('\n'.join(map(str, ans)))
    print(time.time() - t0)

if __name__ == '__main__':
    import cProfile, pstats
    pr = cProfile.Profile()
    pr.enable()
    main()

    pr.disable()
    sortby = 'cumulative'
    out = sys.stdout
    ps = pstats.Stats(pr, stream=out).sort_stats(sortby)
    ps.print_stats()
    out.close()
