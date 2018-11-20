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


tree = {'c': [], 'v': [], 'vl': 0}


def compressStr(num, maxLen):
    """
    压缩字符串,例如'11100111' 压缩成[(3,'1'), (2,'0'), (3,'1')]
    :param num:
    :param maxLen:
    :return:
    """
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


def diffCompressedStr(u, v):
    """
    比较两个压缩后的字符串，返回相同的前缀，和各自剩余的不同的部分
    :param u:
    :param v:
    :return:
    """
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


def popLeft(num, count=1):
    """
    从压缩过的字符串中移除前count个字符
    :param num:
    :param count:
    :return:
    """
    c = 0
    for i in range(len(num)):
        if c + num[i][0] > count:
            return [(num[i][0]-count+c, num[i][1])] + num[i+1:]
        else:
            c += num[i][0]
    
    return []


def rev(val):
    """
    取反
    :param val:
    :return:
    """
    return '1' if val == '0' else '0'


def buildTree(num, idx, numLen):
    """
    创建前缀树
    :param num:
    :param idx:
    :param numLen:
    :return:
    """
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
            # 如果当前节点的值和插入的值有不完全相同，分裂当前节点
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
    """
    计算每个节点中的字符串的长度
    :param t:
    :return:
    """
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


def check(l, r, idx):
    """
    检查递增的数组idx中是否有值介于[l, r]之间
    :param l:
    :param r:
    :param idx:
    :return:
    """
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
    """
    在递增数组idx中查找最小的介于[l,r]之间的值，假设必定存在
    :param l:
    :param r:
    :param idx:
    :return:
    """
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
    """
    在前缀树中查询
    :param l:
    :param r:
    :param num:
    :return:
    """
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
    

MXD = max([len(x) for x in A])
for i, v in enumerate(A):
    buildTree(v, i + 1, MXD)
computeTreeValLen(tree)

ans = []
for l, r, v in Q:
    ans.append(query(l, r, v))

print('\n'.join(map(str, ans)))
