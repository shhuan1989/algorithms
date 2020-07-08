
def solve(D1, C, D2, P, N, A):
    cost = 0
    oil = 0
    i = 0
    while i < N-1:
        to = i + 1
        for j in range(i + 1, N):
            if A[j][0] - A[i][0] > C * D2:
                break
            if A[j][1] < A[i][1]:
                to = j
                break

        dist = A[to][0] - A[i][0]
        if C * D2 < dist:
            return 'No Solution'

        # add = min(max(0, (dist/D2 - oil)) if A[to][1] < A[i][1] else min((C-oil), (A[-1][0]-A[i][0])/D2), C-oil)
        add = max(dist/D2-oil, 0) if A[i][1] > A[to][1] else min(C-oil, max((A[-1][0]-A[i][0])/D2-oil, 0))

        oil += add
        cost += A[i][1] * add
        i = to
        oil -= dist / D2
        if oil < 0:
            return 'No Solution'

    return '{:.2f}'.format(cost)


if __name__ == '__main__':

    D1, C, D2, P, N = map(float, input().split())
    A = [(0, P)]
    for i in range(int(N)):
        d, p = map(float, input().split())
        A.append((d, p))
    A.append((D1, float('inf')))
    A.sort()

    print(solve(D1, C, D2, P, int(N)+2, A))