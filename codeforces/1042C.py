# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""


N = int(input())
A = [int(x) for x in input().split()]

B = [abs(x) for x in A]

zeros = [i for i in range(N) if A[i] == 0]
positives = [i for i in range(N) if A[i] > 0]
negs = [(abs(A[i]), i) for i in range(N) if A[i] < 0]
idx = []

if len(negs) % 2 == 0:
    if len(zeros) > 1:
        print('\n'.join(['1 {} {}'.format(i+1, zeros[0] + 1) for i in zeros[1:]]))
        if len(zeros) < N:
            print('2 {}'.format(zeros[0] + 1))
    elif len(zeros) == 1:
        print('2 {}'.format(zeros[0] + 1))
    else:
        pass
    idx = [i for v, i in negs] + positives
    
else:
    negs.sort()
    negs = [i for v, i in negs]
    
    if len(zeros) > 0:
        print('\n'.join(['1 {} {}'.format(i + 1, zeros[0] + 1) for i in zeros[1:]]))
        print('1 {} {}'.format(zeros[0]+1, negs[0]+1))
        if len(zeros) + 1 < N:
            print('2 {}'.format(negs[0] + 1))
    else:
        print('2 {}'.format(negs[0] + 1))
        
    idx = positives + negs[1:]

if idx:
    mx = -1
    mxVal = float('-inf')
    for i in idx:
        if B[i] > mxVal:
            mxVal = B[i]
            mx = i
    
    print('\n'.join(['1 {} {}'.format(u + 1, mx + 1) for u in idx if u != mx]))
    
        
        
    
    


