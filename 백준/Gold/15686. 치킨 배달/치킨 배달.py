import sys
from itertools import combinations
input = sys.stdin.readline

dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 0 빈칸 1 집 2 치킨집|| 치킨거리는 집과 치킨집 사이의 거리 최솟값의 합

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
ans = 10e9
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i, j))

for li in combinations(chicken, len(chicken)-M):
    l = 0
    chic = []
    for k in chicken:
        if k not in li:
            chic.append(k)
    for i in range(N):
        for j in range(N):
            cnt = []
            if arr[i][j] == 1:
                for dy, dx in chic:
                    cnt.append(abs(dy-i) + abs(dx-j))
                l += min(cnt)
    ans = min(ans, l)
print(ans)