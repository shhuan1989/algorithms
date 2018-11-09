# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/9/18

"""

import random


def genInput(N, M, large=False, fixtLen=True, fl=20):
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
    elif fixtLen:
        NUMLEN = fl
        A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(NUMLEN)]) for _
             in range(N)]
        Q = []
        for i in range(M):
            l = random.randint(1, max( N // 2, 1))
            r = random.randint(l, N)
            v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(NUMLEN)])
            Q.append((l, r, v))
        return N, M, A, Q
    else:
        A = ['1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(1, random.randint(1, 20))]) for _
             in range(N)]
        Q = []
        for i in range(M):
            l = random.randint(1, N // 2)
            r = random.randint(l, N)
            v = '1' + ''.join(['1' if random.randint(0, 10) > 4 else '0' for _ in range(random.randint(1, 20))])
            Q.append((l, r, v))
        return N, M, A, Q


def writeFile(N, M, A, Q, fname):
    with open(fname, 'w') as f:
        f.write('{} {}\n'.format(N, M))
        f.write('\n'.join(A))
        f.write('\n')
        for l, r, v in Q:
            f.write('{} {} {}\n'.format(l, r, v))
    f.close()


import subprocess

while True:
    N, M, A, Q = genInput(random.randint(1, 5), random.randint(1, 10), fl = 5)
    writeFile(N, M, A, Q, 'input.txt')
    writeFile(N, M, A, Q, 'input2.txt')
    
    p1 = subprocess.Popen(['python', 'NOV18_BINSTR.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output1, unused_err = p1.communicate()
    # print(output1)
    
    print('=========')
    p2 = subprocess.Popen(['python', 'NOV18_BINSTR2.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output2, unused_err = p2.communicate()
    # print(output2)
    
    output1 = output1.decode('utf-8')
    output2 = output2.decode('utf-8')
    if output1 != output2:
        print('{} {}'.format(N, M))
        print('\n'.join(A))
        for l, r, v in Q:
            print('{} {} {}'.format(l, r, v))
        print('x' * 40)
        print(output1)
        print('x'*40)
        print(output2)
        break
