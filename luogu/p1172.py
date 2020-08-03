# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/27

"""

import collections


if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    N = int(input().strip())
    
    A = []
    for i in range(N):
        r, c = map(int, input().strip().split())
        A.append((r, c))
        
        
        
    def safe(a):
        rc = collections.defaultdict(list)
        cr = collections.defaultdict(list)
        for r, c in a:
            rc[r].append(c)
            cr[c].append(r)
            
        for r, c in a:
            # right
            if any([nc > c for nc in rc[r]]) and any([nr < r for nr in cr[c]]):
                return False
            
        return True
    
    if safe(A):
        print(0)
        exit(0)
    
    remove = []
    for i in range(N):
        # remove A[i]
        if safe(A[:i] + A[i+1:]):
            remove.append(i+1)
    
    if remove:
        print(1)
        print('\n'.join(map(str, remove)))
    else:
        print(-1)
    
    