import sys
import itertools
import math

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    x_total = 0
    y_total = 0
    res = []
    ans = math.inf
    N = int(input())
    for _ in range(N):
        res.append(list(map(int, input().split())))
    for i in res:
        x_total += i[0]
        y_total += i[1]

    k = list(itertools.combinations(res, N//2))

    for i in k:
        x1 = 0
        y1 = 0
        for x, y in list(i):

            x1 += x
            y1 += y

        x2 = x_total - x1
        y2 = y_total - y1
        ans = min(ans, math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2))

    print(ans)