# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/3

"""


def ask(question):
    print('?', len(question), ' '.join(map(str, question)), flush=True)
    return int(input())


def main():
    T = int(input())
    for ti in range(T):
        N, K = map(int, input().split())
        exs = []
        for i in range(K):
            ex = [int(x) for x in input().split()][1:]
            exs.append(set(ex))
        # find the position of max val
        maxv = ask(list(range(1, N+1)))
        
        lo, hi = 1, N
        while lo < hi:
            m = (lo + hi) // 2
            # max val in [lo, m]
            a = ask(list(range(lo, m + 1)))
            if a >= maxv:
                # max val is in left section
                hi = m
            else:
                # max val is in right section
                lo = m + 1
        
        maxpos = lo
        
        # only one item will contains maxpos, the value of others are maxv
        ans = []
        for ex in exs:
            if maxpos not in ex:
                ans.append(maxv)
            else:
                # query for this section
                v = ask([i for i in range(1, N + 1) if i not in ex])
                ans.append(v)
        
        print('! {}'.format(' '.join(map(str, ans))), flush=True)
        result = input()
        if result != 'Correct':
            exit(0)


if __name__ == '__main__':
    main()